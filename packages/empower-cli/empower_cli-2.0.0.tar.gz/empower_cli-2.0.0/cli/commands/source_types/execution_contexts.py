from typing import Optional

import typer
from cli.commands.source_types.source_types import ENDPOINT as SOURCE_TYPE
from cli.common.command_help import CRUD_FILE_PATH_HELP
from cli.common.command_util import handle_request_command
from cli.common.crud_command_base import CRUDCommandBase
from cli.common.service_type import ServiceType
from cli.common.util import get_json_data, read_yaml_file

ENDPOINT = f"execution-context"
app = typer.Typer()


class ExecutionContextCRUD(CRUDCommandBase):
    def __init__(
        self,
        service_type: ServiceType = ServiceType.SOURCE_TYPE,
        endpoint: str = ENDPOINT,
    ) -> None:
        super().__init__(service_type, endpoint)


@app.command("get", help="Get All Execution Contexts")
@handle_request_command
def get_execution_context(
    ctx_name: Optional[str] = typer.Option(None, "--name"),
    ctx_type: Optional[str] = typer.Option(None, "--type")
):
    typer.echo(
        ExecutionContextCRUD().get_by_id({"context_name": ctx_name, "context_type": ctx_type}))


@app.command("create", help="Create Execution Context")
@handle_request_command
def create_execution_context(
    json_: Optional[str] = typer.Option(None, "--json"),
    file_path: Optional[typer.FileText] = typer.Option(
        None,
        mode="r",
        encoding="utf-8",
        callback=get_json_data,
        help=CRUD_FILE_PATH_HELP,
    ),
    yaml_file: Optional[str] = typer.Option(None, "--yaml"),
):
    typer.echo(
        ExecutionContextCRUD().create(json_ or file_path or read_yaml_file(yaml_file))
    )


@app.command("update", help="Execution Context")
@handle_request_command
def update_execution_context(
    name: str = typer.Argument(
        ...,
        metavar="Execution Context Name",
    ),
    json_: Optional[str] = typer.Option(None, "--json"),
    file_path: Optional[typer.FileText] = typer.Option(
        None,
        mode="r",
        encoding="utf-8",
        callback=get_json_data,
        help=CRUD_FILE_PATH_HELP,
    ),
    yaml_file: Optional[str] = typer.Option(None, "--yaml"),
):
    typer.echo(
        ExecutionContextCRUD().update(
            data=json_ or file_path or read_yaml_file(yaml_file),
            endpoint=f"{ENDPOINT}/{name}",
        )
    )


@app.command("delete", help="Execution Context")
@handle_request_command
def delete_execution_context(
    name: str = typer.Argument(
        ...,
        metavar="Execution Context Name",
    ),
):
    typer.echo(ExecutionContextCRUD().delete(name))


@app.command("filter", help="Get Execution Contexts By Type And Source Type Name")
@handle_request_command
def get_execution_context_by_context_type_and_source_type_name(
    source_type_name: str = typer.Option(None, "--source-type"),
    exec_ctx_type: str = typer.Option(None, "--context-type"),
):
    if source_type_name and exec_ctx_type:
        endpoint = f"{SOURCE_TYPE}/{source_type_name}/execution-context/{exec_ctx_type}"
    else:
        endpoint = f"{SOURCE_TYPE}/{source_type_name}/execution-contexts"
    typer.echo(
        ExecutionContextCRUD().get(
            endpoint=endpoint,
        )
    )
