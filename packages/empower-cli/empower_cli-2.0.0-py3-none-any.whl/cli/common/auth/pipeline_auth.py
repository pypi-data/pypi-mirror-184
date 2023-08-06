import os

import requests
from cli.common.file_utils import write_credentials_to_json

from .config import PIPELINE_FLOW_CREDENTIALS_FILE


def credentials_flow_auth(
    token_request_url: str,
    file_name: str = PIPELINE_FLOW_CREDENTIALS_FILE
) -> None:
    """
    Get keycloak client credentials.

    :param file_name: credentials storage file name
    :return: keycloak client credentials json
    """
    params = {
        "client_id": os.environ["EMPOWER_CLI_CLIENT_ID"],
        "client_secret": os.environ["EMPOWER_CLI_CLIENT_SECRET"],
        "grant_type": "client_credentials",
    }


    response = requests.post(token_request_url, data=params)
    response.raise_for_status()
    credentials = response.json()
    write_credentials_to_json(credentials, file_name)
