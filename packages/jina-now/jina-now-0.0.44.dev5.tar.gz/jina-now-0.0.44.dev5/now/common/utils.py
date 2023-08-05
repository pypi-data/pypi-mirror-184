import json
import os
import pathlib
import time
from os.path import expanduser as user
from typing import Dict, List, Optional, Tuple

import hubble
from docarray import DocumentArray
from jina import __version__ as jina_version
from jina.helper import random_port

from now.app.base.app import JinaNOWApp
from now.constants import (
    EXECUTOR_PREFIX,
    EXTERNAL_CLIP_HOST,
    MODALITIES_MAPPING,
    NOW_AUTOCOMPLETE_VERSION,
    NOW_ELASTIC_INDEXER_VERSION,
    NOW_PREPROCESSOR_VERSION,
    PREFETCH_NR,
    TAG_INDEXER_DOC_HAS_TEXT,
    Modalities,
)
from now.demo_data import DEFAULT_EXAMPLE_HOSTED
from now.deployment.deployment import cmd
from now.executor.name_to_id_map import name_to_id_map
from now.now_dataclasses import UserInput

cur_dir = pathlib.Path(__file__).parent.resolve()

MAX_RETRIES = 20


def common_get_flow_env_dict(
    encoder_uses: str,
    encoder_with: Dict,
    encoder_uses_with: Dict,
    pre_trained_embedding_size: int,
    indexer_uses: str,
    indexer_resources: Dict,
    user_input: UserInput,
    tags: List,
    deployment_type: str,
    data_class,
):
    """Returns dictionary for the environments variables for the clip flow.yml files."""
    use_high_performance_flow = (
        get_email().split('@')[-1] == 'jina.ai' and deployment_type == 'remote'
    )
    if use_high_performance_flow:
        print(
            f"🚀🚀🚀 As employee of Jina, you are using a high performance flow.\n"
            f"Therefore, your deployment will be faster.\n"
            f"But make sure to scale it down after deployment."
        )
    if data_class:
        index_field_names = list(data_class.__dataclass_fields__.keys())
    else:
        index_field_names = user_input.index_fields
    config = {
        'JINA_VERSION': jina_version,
        'ENCODER_NAME': f'{EXECUTOR_PREFIX}{encoder_uses}',
        'CAST_CONVERT_NAME': f'{EXECUTOR_PREFIX}CastNMoveNowExecutor/v0.0.3',
        'N_DIM': pre_trained_embedding_size,
        'PRE_TRAINED_EMBEDDINGS_SIZE': pre_trained_embedding_size,
        'INDEXER_NAME': f'{EXECUTOR_PREFIX}{indexer_uses}',
        'PREFETCH': PREFETCH_NR,
        'PREPROCESSOR_NAME': f'{EXECUTOR_PREFIX}{name_to_id_map.get("NOWPreprocessor")}/{NOW_PREPROCESSOR_VERSION}',
        'PREPROCESSOR_REPLICAS': 15
        if use_high_performance_flow and 'NOW_CI_RUN' not in os.environ
        else 1,
        'AUTOCOMPLETE_EXECUTOR_NAME': f'{EXECUTOR_PREFIX}{name_to_id_map.get("NOWAutoCompleteExecutor2")}/{NOW_AUTOCOMPLETE_VERSION}',
        'COLUMNS': tags,
        'DOCUMENT_MAPPINGS': json.dumps(
            [
                ('encoderclip', 512, ','.join(index_field_names)),
            ]
        ),
        'ADMIN_EMAILS': user_input.admin_emails or [] if user_input.secured else [],
        'USER_EMAILS': user_input.user_emails or [] if user_input.secured else [],
        'API_KEY': [user_input.api_key]
        if user_input.secured and user_input.api_key
        else [],
        **encoder_with,
        **indexer_resources,
    }

    if encoder_uses_with.get('pretrained_model_name_or_path'):
        config['PRE_TRAINED_MODEL_NAME'] = encoder_uses_with[
            "pretrained_model_name_or_path"
        ]

    config['CUSTOM_DNS'] = ''
    if 'NOW_EXAMPLES' in os.environ:
        is_demo_ds = user_input.dataset_name in DEFAULT_EXAMPLE_HOSTED
        if is_demo_ds:
            config[
                'CUSTOM_DNS'
            ] = f'now-example-{user_input.app_instance.app_name}-{user_input.dataset_name}.dev.jina.ai'
            config['CUSTOM_DNS'] = config['CUSTOM_DNS'].replace('_', '-')

    return config


def common_setup(
    app_instance: JinaNOWApp,
    user_input: UserInput,
    dataset: DocumentArray,
    encoder_uses: str,
    encoder_uses_with: Dict,
    indexer_uses: str,
    pre_trained_embedding_size: int,
    kubectl_path: str,
    data_class,
    encoder_with: Optional[Dict] = {},
    indexer_resources: Optional[Dict] = {},
) -> Dict:
    tags = _extract_tags_for_indexer(user_input)
    env_dict = common_get_flow_env_dict(
        encoder_uses=encoder_uses,
        encoder_with=encoder_with,
        encoder_uses_with=encoder_uses_with,
        pre_trained_embedding_size=pre_trained_embedding_size,
        indexer_uses=indexer_uses,
        indexer_resources=indexer_resources,
        user_input=user_input,
        tags=tags,
        deployment_type=user_input.deployment_type,
        data_class=data_class,
    )
    app_instance.set_flow_yaml(dataset_len=len(dataset))
    return env_dict


def get_email():
    try:
        with open(user('~/.jina/config.json')) as fp:
            config_val = json.load(fp)
            user_token = config_val['auth_token']
            client = hubble.Client(token=user_token, max_retries=None, jsonify=True)
            response = client.get_user_info()
        if 'email' in response['data']:
            return response['data']['email']
        return ''
    except FileNotFoundError:
        return ''


def get_indexer_config(
    elastic: Optional[bool] = False,
    kubectl_path: str = None,
    deployment_type: str = None,
) -> Dict:
    """Depending on the number of samples, which will be indexed, indexer and its resources are determined.

    :param num_indexed_samples: number of samples which will be indexed; should incl. chunks for e.g. text-to-video app
    :param elastic: hack to use NOWElasticIndexer, should be changed in future.
    :param kubectl_path: path to kubectl binary
    :param deployment_type: deployment type, e.g. 'remote' or 'local'
    :return: dict with indexer and its resource config
    """

    config = {
        'indexer_uses': f'{name_to_id_map.get("NOWElasticIndexer")}/{NOW_ELASTIC_INDEXER_VERSION}',
        # 'hosts': setup_elastic_service(kubectl_path),
        'indexer_resources': {'INDEXER_CPU': 0.5, 'INDEXER_MEM': '8G'},
    }
    return config


def _extract_tags_for_indexer(user_input: UserInput):
    final_tags = []
    for tag, value in user_input.filter_fields_modalities.items():
        if tag in user_input.filter_fields:
            final_tags.append([tag, value])

    for field, modality in user_input.filter_fields_modalities.items():
        if modality in [
            MODALITIES_MAPPING[Modalities.IMAGE],
            MODALITIES_MAPPING[Modalities.VIDEO],
        ]:
            final_tags.append([TAG_INDEXER_DOC_HAS_TEXT, str(bool.__name__)])
    return final_tags


def setup_elastic_service(
    kubectl_path: str,
) -> str:
    """Setup ElasticSearch service and return a connection string to connect to the service with.

    :param kubectl_path: path to kubectl binary
    :return: connection string for connecting to the ElasticSearch service.
    """
    cur_dir = pathlib.Path(__file__).parent.resolve()
    cmd(
        f'{kubectl_path} create -f https://download.elastic.co/downloads/eck/2.4.0/crds.yaml'
    )
    cmd(
        f'{kubectl_path} apply -f https://download.elastic.co/downloads/eck/2.4.0/operator.yaml'
    )
    cmd(f'{kubectl_path} create ns nowapi')
    cmd(f'{kubectl_path} apply -f {cur_dir}/../deployment/elastic_kind.yml')
    num_retries = 0
    es_password, error_msg = '', b''
    while num_retries < MAX_RETRIES:
        es_password, error_msg = cmd(
            [
                kubectl_path,
                "get",
                "secret",
                "quickstart-es-elastic-user",
                "-o",
                "go-template='{{.data.elastic | base64decode}}'",
            ]
        )
        if es_password:
            es_password = es_password.decode("utf-8")[1:-1]
            break
        else:
            num_retries += 1
            time.sleep(2)
    if not es_password:
        raise Exception(error_msg.decode("utf-8"))
    host = f"https://elastic:{es_password}@quickstart-es-http.default:9200"
    return host


def _get_clip_apps_with_dict(user_input: UserInput) -> Tuple[Dict, Dict]:
    """Depending on whether this app will be remotely deployed, this function returns the with
    dictionary for the CLIP executor."""
    is_remote = user_input.deployment_type == 'remote'
    encoder_with = {
        'ENCODER_HOST': EXTERNAL_CLIP_HOST if is_remote else '0.0.0.0',
        'ENCODER_PORT': 443 if is_remote else random_port(),
        'IS_REMOTE_DEPLOYMENT': is_remote,
    }
    return encoder_with
