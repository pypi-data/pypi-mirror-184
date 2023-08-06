import typer
import json

from typing import Optional

from cli.common.command_help import CRUD_FILE_PATH_HELP
from cli.common.command_util import handle_request_command
from cli.common.crud_command_base import CRUDCommandBase
from cli.common.service_type import ServiceType
from cli.common.util import get_json_data
from cli.common.enums import RequestMethods

app = typer.Typer()


class EnterpriseCRUD(CRUDCommandBase):
    def __init__(
        self,
        service_type: ServiceType = ServiceType.EMPOWER_DISCOVERY,
        endpoint: str = "enterprise",
    ) -> None:
        super().__init__(service_type, endpoint)

    def get_oauth_domain(self) -> str:
        """Make a GET request to the API.

        :return: serialized response data.
        """
        url = self.default_url(f"{self.endpoint}/oauth-domain/")
        response = self._make_request(RequestMethods.GET, url)
        typer.echo(f"request made to: {url}")
        return json.dumps(response.json(), indent=2)


@app.command()
@handle_request_command
def show(id_: str):
    typer.echo(EnterpriseCRUD().get_by_id(id_))


# todo: allow to take key value pairs as query parameters
@app.command("list")
@handle_request_command
def list_(
    domain: Optional[str] = typer.Option(None, help="Filter enterprises by domain")
):
    typer.echo(EnterpriseCRUD().get())


@app.command()
@handle_request_command
def create(
    json_: Optional[str] = typer.Option(None, "--json"),
    file_path: Optional[typer.FileText] = typer.Option(
        None,
        mode="r",
        encoding="utf-8",
        callback=get_json_data,
        help=CRUD_FILE_PATH_HELP,
    ),
):
    typer.echo(EnterpriseCRUD().create(json_ or file_path))


@app.command()
@handle_request_command
def update(
    json_: Optional[str] = typer.Option(None, "--json"),
    file_path: Optional[typer.FileText] = typer.Option(
        None,
        mode="r",
        encoding="utf-8",
        callback=get_json_data,
        help=CRUD_FILE_PATH_HELP,
    ),
):
    typer.echo(EnterpriseCRUD().update(json_ or file_path))


@app.command()
@handle_request_command
def delete(id_: str):
    typer.echo(EnterpriseCRUD().delete(id_))
