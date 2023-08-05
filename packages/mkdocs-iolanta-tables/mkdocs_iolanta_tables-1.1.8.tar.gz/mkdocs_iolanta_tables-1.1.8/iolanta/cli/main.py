import logging
from typing import Optional

from rdflib import URIRef
from rich.console import Console
from rich.table import Table
from typer import Argument, Context, Option, Typer, echo
from urlpath import URL

from iolanta.conversions import url_to_path
from iolanta.graph_providers.find import (
    construct_graph_from_installed_providers,
)
from iolanta.iolanta import Iolanta
from iolanta.renderer import render
from mkdocs_iolanta.cli.formatters.choose import cli_print
from mkdocs_iolanta.storage import load_graph
from mkdocs_iolanta.types import QueryResultsFormat

app = Typer()


logger = logging.getLogger(__name__)


@app.callback()
def callback(
    context: Context,
    graph: Optional[str] = None,
    log_level: str = 'info',
):
    logger.setLevel(
        {
            'info': logging.INFO,
            'debug': logging.DEBUG,
        }[log_level],
    )

    if graph is None:
        graph = construct_graph_from_installed_providers()

        if graph is not None:
            logger.info('Using graph from provider.')
            context.obj = Iolanta(logger=logger, graph=graph)
        else:
            logger.info('Using an in-memory transient graph.')
            context.obj = Iolanta(logger=logger)

    else:
        url = URL(graph)
        if url.scheme == 'file+shelve':
            path = url_to_path(url)
            logger.info(f'Loading pickled graph from `{path}`')
            context.obj = Iolanta(graph=load_graph(path), logger=logger)

        else:
            raise ValueError(f'Unknown path for a graph: {url}')


@app.command(name='render')
def render_command(
    context: Context,
    url: str,
    environment: str = Option(
        'https://en.wikipedia.org/wiki/CLI',
        '--as',
    ),
):
    """Render a given URL."""
    iolanta: Iolanta = context.obj

    echo(
        render(
            node=URIRef(url),
            iolanta=iolanta,
            environments=[
                URIRef(environment),
            ],
        ),
    )


@app.command()
def namespaces(
    context: Context,
):
    """Registered namespaces."""
    iolanta: Iolanta = context.obj

    table = Table(
        'Namespace',
        'URL',
        show_header=True,
        header_style="bold magenta",
    )

    for namespace, url in iolanta.graph.namespaces():
        table.add_row(namespace, url)

    Console().print(table)


@app.command()
def query(
    context: Context,
    fmt: QueryResultsFormat = Option(
        default=QueryResultsFormat.PRETTY,
        metavar='format',
    ),
    query_text: Optional[str] = Argument(
        None,
        metavar='query',
        help='SPARQL query text. Will be read from stdin if empty.',
    ),
    use_qnames: bool = Option(
        default=True,
        help='Collapse URLs into QNames.',
    ),
):
    """Query Iolanta graph with SPARQL."""
    iolanta: Iolanta = context.obj

    cli_print(
        query_result=iolanta.query(query_text),
        output_format=fmt,
        display_iri_as_qname=use_qnames,
        graph=iolanta.graph,
    )

