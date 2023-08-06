import requests
import typer
from typing import Optional
from cli.common.auth import AuthAPIClient, credentials_flow_auth, browse, get_auth_uri
from cli.common.service_type import ServiceType
from cli.common.validation import validate_domain
from cli.common.schemas import OauthDomain
from typer import Argument
from cli.common.store_client import store
from cli.commands.empower_discovery.enterprise import EnterpriseCRUD

app = typer.Typer()
ENDPOINT = "auth"
SERVICE_TYPE = ServiceType.EMPOWER_AUTH


def get_api_response(domain) -> dict:
    api_client = AuthAPIClient(domain)
    return api_client.get_domain_auth_url()


def set_api_responses_to_store(domain_auth_url_response):
    oauth_domain = OauthDomain(**domain_auth_url_response)
    store.save("auth", **oauth_domain.dict())


def print_oauth_discovery_data():
    typer.echo(f"Fetching discovery data")
    typer.echo(EnterpriseCRUD().get_oauth_domain())


def print_oauth_discovery_data_for_admin():
    try:
        if store.empower_api_url and store.empower_discovery_url:
            print_oauth_discovery_data()
    except ValueError:
        typer.secho(
            "Not showing discovery output, "
            "because 'empower_api_url' or 'empower_discovery_ulr' is not being set",
        fg="yellow")


def get_empower_urls(prod_mode: Optional[bool]):
    if prod_mode:
        auth_server_url = "https://auth.empoweranalytics.io"
        user_service_url = "https://user.empoweranalytics.io"
    else:
        auth_server_url = "https://auth-dv.empoweranalytics.io"
        user_service_url = "https://dv.user.empoweranalytics.io"
    return auth_server_url, user_service_url


@app.command(help="Login user within an opened browser tab.")
def login(domain: str = Argument(..., callback=validate_domain)) -> None:
    typer.echo("Processing login. Wait for the browser window to open.")

    domain_auth_url_response = get_api_response(domain)

    auth_url = get_auth_uri(domain_auth_url_response)

    try:
        set_api_responses_to_store(domain_auth_url_response)
        browse(auth_url)
        typer.echo("Logged in successfully.")
        print_oauth_discovery_data()
    except RuntimeError as e:
        typer.echo(e)
    except Exception as e:
        typer.echo(f"Authentication error: {e}")


@app.command(help="Login empower admin within an opened browser tab.")
def empower_login(
        prod_mode: bool = typer.Option(
            None, help="Use production token on endpoints"
        )
    ) -> None:

    auth_server_url, user_service_url = get_empower_urls(prod_mode)

    typer.echo("Processing login. Wait for the browser window to open.")

    url_data = {
        "authServerUrl": auth_server_url,
        "authRealm": "empower-shared",
        "clientId": "empower"
    }

    auth_url = get_auth_uri(url_data)
    url_data["userServiceUrl"] = user_service_url

    try:
        set_api_responses_to_store(url_data)
        browse(auth_url)
        typer.echo("Logged in successfully.")
    except RuntimeError as e:
        typer.echo(e)
    except Exception as e:
        typer.echo(f"Authentication error: {e}")


# TODO add when client based(domain based) command will be needed
# @app.command(help="Pipeline authentication using 'client_credentials' flow.")
# def login_pipeline(domain) -> None:
#      pass


@app.command(help="Pipeline authentication using 'client_credentials' flow.")
def empower_login_pipeline(
        prod_mode: bool = typer.Option(
            None, help="Use production token on endpoints"
        )
    ) -> None:
    typer.echo("Processing login.")

    auth_server_url, user_service_url = get_empower_urls(prod_mode)

    url_data = {
        "authServerUrl": auth_server_url,
        "authRealm": "empower-shared",
        "clientId": "empower",
        "userServiceUrl": user_service_url
    }

    token_request_url = f"{auth_server_url}/auth/realms/empower-shared/protocol/openid-connect/token"
    try:
        credentials_flow_auth(token_request_url)
        set_api_responses_to_store(url_data)
        typer.echo("Logged in successfully.")
        print_oauth_discovery_data_for_admin()
    except requests.HTTPError:
        typer.echo("Error occurred while getting authentication credentials.")
        typer.Abort(1)
