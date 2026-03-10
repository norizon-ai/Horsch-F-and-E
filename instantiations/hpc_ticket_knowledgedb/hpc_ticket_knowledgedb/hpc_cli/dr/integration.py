"""Deep Research integration for CLI."""

from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.live import Live

from .client import DRClient, DRResult, check_dr_connection


console = Console()


async def run_research(
    query: str,
    detailed: bool = False,
    brief: bool = True,
    max_iterations: int = None,
    stream: bool = True
) -> None:
    """Run deep research and display results.

    Args:
        query: Research query
        detailed: Show full report (not just concise answer)
        brief: Request brief answer from DR
        max_iterations: Override max iterations
        stream: Use streaming mode
    """
    client = DRClient()

    # Check connection first
    is_healthy = await client.health_check()
    if not is_healthy:
        console.print(f"[red]Error:[/red] Cannot connect to DR API at {client.base_url}")
        console.print("Make sure the DR service is running.")
        return

    console.print(f"\n[bold cyan]Deep Research:[/bold cyan] {query}\n")

    if stream:
        await _run_streaming(client, query, brief, detailed)
    else:
        await _run_sync(client, query, brief, detailed)


async def _run_streaming(
    client: DRClient,
    query: str,
    brief: bool,
    detailed: bool
) -> None:
    """Run DR with streaming output."""
    full_response = ""
    progress_status = ""

    with Live(console=console, refresh_per_second=10) as live:
        def on_progress(status: str):
            nonlocal progress_status
            progress_status = status
            live.update(Panel(
                f"[dim]{progress_status}[/dim]\n\n{full_response}",
                title="[bold]Researching...[/bold]",
                border_style="cyan"
            ))

        try:
            async for chunk in client.query_stream(query, brief=brief, on_progress=on_progress):
                full_response += chunk
                live.update(Panel(
                    f"[dim]{progress_status}[/dim]\n\n{full_response}",
                    title="[bold]Researching...[/bold]",
                    border_style="cyan"
                ))
        except Exception as e:
            console.print(f"\n[red]Error during research:[/red] {e}")
            return

    # Final display
    console.print()
    console.print(Panel(
        Markdown(full_response),
        title="[bold green]Research Complete[/bold green]",
        border_style="green"
    ))


async def _run_sync(
    client: DRClient,
    query: str,
    brief: bool,
    detailed: bool
) -> None:
    """Run DR synchronously with spinner."""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:
        task = progress.add_task("Researching...", total=None)

        try:
            result = await client.query(query, brief=brief)
        except Exception as e:
            console.print(f"\n[red]Error during research:[/red] {e}")
            return

        progress.remove_task(task)

    _display_result(result, detailed)


def _display_result(result: DRResult, detailed: bool) -> None:
    """Display DR result."""
    console.print()

    # Always show concise answer
    console.print(Panel(
        Markdown(result.concise_answer),
        title="[bold green]Answer[/bold green]",
        border_style="green"
    ))

    # Show confidence
    confidence_color = "green" if result.confidence_score >= 0.7 else "yellow" if result.confidence_score >= 0.5 else "red"
    console.print(f"\n[{confidence_color}]Confidence: {result.confidence_score:.0%}[/{confidence_color}] | Iterations: {result.iterations_count}")

    # Show full report if detailed
    if detailed and result.final_report:
        console.print()
        console.print(Panel(
            Markdown(result.final_report),
            title="[bold]Full Report[/bold]",
            border_style="blue"
        ))

    # Show sources if available
    if result.sources:
        console.print("\n[bold]Sources:[/bold]")
        for source in result.sources[:5]:
            console.print(f"  - {source}")


async def run_search(
    query: str,
    index: str = "docs",
    max_results: int = 10
) -> None:
    """Run direct search and display results.

    Args:
        query: Search query
        index: 'docs' or 'tickets'
        max_results: Maximum results
    """
    client = DRClient()

    # Check connection
    is_healthy = await client.health_check()
    if not is_healthy:
        console.print(f"[red]Error:[/red] Cannot connect to DR API at {client.base_url}")
        return

    console.print(f"\n[bold]Searching {index}:[/bold] {query}\n")

    try:
        results = await client.search(query, index, max_results)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        return

    if not results:
        console.print("[yellow]No results found.[/yellow]")
        return

    for i, result in enumerate(results, 1):
        title = result.get("title", "Untitled")
        text = result.get("text", result.get("problem_description", ""))[:200]
        score = result.get("score", 0)

        console.print(Panel(
            f"{text}...",
            title=f"[bold]{i}. {title}[/bold] [dim](score: {score:.2f})[/dim]",
            border_style="dim"
        ))
