import typer
from cli.commands.empower_api import (
    data_model_config,
    environment_databricks,
    file_object_match,
    processing_step_command,
    source,
    source_list,
    source_object_list,
)

empower_api_typer = typer.Typer()

empower_api_typer.add_typer(source.app, name="source")
empower_api_typer.add_typer(data_model_config.app, name="data-model-config")
empower_api_typer.add_typer(source_list.app, name="source-list")
empower_api_typer.add_typer(environment_databricks.app, name="environment-databricks")
empower_api_typer.add_typer(file_object_match.app, name="file-object-match")
empower_api_typer.add_typer(source_object_list.app, name="source-object-list")
empower_api_typer.add_typer(processing_step_command.app, name="processing-step-command")
