#!/usr/bin/env python3
"""
HPC CLI - Main command-line interface.

Provides both:
1. Interactive chat UI (Claude Code-like interface)
2. Direct commands for quick operations
"""

import click
import sys
from rich.console import Console
from pathlib import Path

from .version import __version__
from .config import get_config, reload_config

console = Console()


@click.group(invoke_without_command=True)
@click.version_option(version=__version__)
@click.pass_context
def cli(ctx):
    """HPC CLI - AI-powered HPC support and cluster monitoring.

    Run without commands to start interactive chat mode.
    Use subcommands for specific operations.
    """
    # If no subcommand, launch chat UI
    if ctx.invoked_subcommand is None:
        from .ui.app import run_chat_ui
        run_chat_ui()


@cli.command()
@click.argument('query', required=False)
@click.option('--interactive', '-i', is_flag=True, help='Start interactive chat mode')
def chat(query, interactive):
    """Start chat interface or send a single query.

    Examples:
        hpc chat "How do I submit a SLURM job?"
        hpc chat --interactive
    """
    from .ui.app import run_chat_ui

    if query and not interactive:
        # Single query mode - start UI with initial query
        run_chat_ui(initial_query=query)
    else:
        # Interactive mode
        run_chat_ui()


@cli.command()
@click.argument('query')
@click.option('--detailed', '-d', is_flag=True, help='Show full research iterations and sources')
@click.option('--brief/--no-brief', '-b', default=True, help='Brief or detailed answer (default: brief)')
@click.option('--max-iterations', '-n', type=int, help='Maximum research iterations (default: 3)')
@click.option('--no-stream', is_flag=True, help='Disable streaming (wait for full response)')
def research(query, detailed, brief, max_iterations, no_stream):
    """Perform deep research on HPC questions.

    Uses multi-agent system to research documentation and support tickets.

    Examples:
        hpc research "GPU performance optimization best practices"
        hpc research "Why is my CUDA code slow?" --detailed
        hpc research "How do I use SLURM?" --no-stream
    """
    import asyncio
    from .dr.integration import run_research

    try:
        asyncio.run(run_research(
            query=query,
            detailed=detailed,
            brief=brief,
            max_iterations=max_iterations,
            stream=not no_stream
        ))
    except KeyboardInterrupt:
        console.print("\n[yellow]Research cancelled by user[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)


@cli.command()
@click.argument('query')
@click.option('--index', '-i', type=click.Choice(['docs', 'tickets']), default='docs', help='Index to search')
@click.option('--limit', '-n', default=10, type=int, help='Maximum results (default: 10)')
def search(query, index, limit):
    """Direct search in documentation or tickets (bypasses DR pipeline).

    Examples:
        hpc search "SLURM job submission"
        hpc search "GPU error" --index tickets
        hpc search "module load" --limit 5
    """
    import asyncio
    from .dr.integration import run_search

    try:
        asyncio.run(run_search(query=query, index=index, max_results=limit))
    except KeyboardInterrupt:
        console.print("\n[yellow]Search cancelled by user[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)


@cli.group()
def cluster():
    """Cluster monitoring and analysis tools.

    Access GPU utilization data, job statistics, and user analytics
    from ClusterCockpit monitoring system.
    """
    pass


@cluster.command('gpu-usage')
@click.option('--days', default=3, type=int, help='Days to look back (default: 3)')
@click.option('--max-util', default=70, type=float, help='Maximum GPU utilization threshold (default: 70)')
@click.option('--min-duration', default=2, type=float, help='Minimum job duration in hours (default: 2)')
@click.option('--output', '-o', type=click.Choice(['table', 'json', 'csv']), default='table', help='Output format')
@click.option('--save', '-s', type=click.Path(), help='Save results to file')
def gpu_usage(days, max_util, min_duration, output, save):
    """Find underutilized GPU jobs.

    Queries ClusterCockpit for jobs with low GPU utilization.

    Examples:
        hpc cluster gpu-usage --days 7
        hpc cluster gpu-usage --max-util 50 --output json
        hpc cluster gpu-usage --save results.json
    """
    from .cluster.commands import find_underutilized_gpus

    try:
        find_underutilized_gpus(
            days=days,
            max_util=max_util,
            min_duration=min_duration,
            output_format=output,
            save_path=save
        )
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)


@cluster.command('worst-users')
@click.option('--days', default=7, type=int, help='Days to analyze (default: 7)')
@click.option('--top', default=10, type=int, help='Number of users to show (default: 10)')
@click.option('--output', '-o', type=click.Choice(['table', 'json']), default='table', help='Output format')
@click.option('--save', '-s', type=click.Path(), help='Save results to file')
def worst_users(days, top, output, save):
    """Rank users by GPU waste.

    Analyzes GPU resource waste based on:
    - GPU-hours wasted (underutilized time)
    - GPU type weighting (H200 > H100 > A100 > A40)
    - Utilization penalties (lower usage = higher penalty)

    Examples:
        hpc cluster worst-users --days 30 --top 20
        hpc cluster worst-users --output json --save waste-report.json
    """
    from .cluster.commands import rank_worst_users

    try:
        rank_worst_users(
            days=days,
            top_n=top,
            output_format=output,
            save_path=save
        )
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)


@cli.group(name='config')
def config_group():
    """Manage HPC CLI configuration.

    Configuration is stored in ~/.config/hpc-cli/config.toml
    Sensitive data (API keys, JWT tokens) are stored in system keyring.
    """
    pass


@config_group.command('show')
def config_show():
    """Show current configuration."""
    config = get_config()
    console.print(config.to_rich_table())


@config_group.command('set')
@click.argument('key')
@click.argument('value')
def config_set(key, value):
    """Set configuration value.

    Use dot notation: section.key

    Examples:
        hpc config set llm.url "http://localhost:11434/v1"
        hpc config set llm.model "llama3"
        hpc config set dr.max_iterations 5
        hpc config set clustercockpit.jwt "YOUR_JWT_TOKEN"
    """
    config = get_config()

    try:
        config.set(key, value)

        # Special message for JWT token
        if key == "clustercockpit.jwt":
            console.print("[green]✓[/green] JWT token stored securely in system keyring")
        else:
            console.print(f"[green]✓[/green] Set {key} = {value}")

        console.print(f"[dim]Config saved to {config.get_config_path()}[/dim]")
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        sys.exit(1)


@config_group.command('path')
def config_path():
    """Show configuration file path."""
    config = get_config()
    path = config.get_config_path()

    console.print(f"Configuration file: [cyan]{path}[/cyan]")

    if path.exists():
        console.print(f"[green]✓[/green] File exists")
    else:
        console.print(f"[yellow]⚠[/yellow] File does not exist (will be created on first config change)")


@config_group.command('init')
def config_init():
    """Initialize configuration with default values."""
    config = get_config()
    config.save()

    console.print(f"[green]✓[/green] Configuration initialized")
    console.print(f"[dim]Location: {config.get_config_path()}[/dim]")
    console.print("\nNext steps:")
    console.print("1. Set your LLM endpoint: [cyan]hpc config set llm.url YOUR_LLM_URL[/cyan]")
    console.print("2. Set Elasticsearch URL: [cyan]hpc config set elasticsearch.url http://localhost:9200[/cyan]")
    console.print("3. Set ClusterCockpit JWT: [cyan]hpc config set clustercockpit.jwt YOUR_JWT[/cyan]")


@cli.command()
def version():
    """Show version information."""
    console.print(f"HPC CLI version [cyan]{__version__}[/cyan]")
    console.print("\nComponents:")
    console.print("  • Interactive chat UI (Textual)")
    console.print("  • Deep Research (multi-agent system)")
    console.print("  • Cluster monitoring (ClusterCockpit)")


@cli.command()
def doctor():
    """Check system health and configuration.

    Verifies:
    - Configuration file exists and is valid
    - LLM endpoint is reachable
    - Elasticsearch is accessible
    - ClusterCockpit credentials are configured
    """
    from rich.table import Table

    console.print("[bold]HPC CLI System Check[/bold]\n")

    config = get_config()
    checks = []

    # Check config file
    config_path = config.get_config_path()
    if config_path.exists():
        checks.append(("Config file", "✓", "green", str(config_path)))
    else:
        checks.append(("Config file", "✗", "red", "Not found - run 'hpc config init'"))

    # Check LLM endpoint
    try:
        import httpx
        response = httpx.get(f"{config.llm.url}/models", timeout=5)
        if response.status_code == 200:
            checks.append(("LLM endpoint", "✓", "green", config.llm.url))
        else:
            checks.append(("LLM endpoint", "⚠", "yellow", f"Returned {response.status_code}"))
    except Exception as e:
        checks.append(("LLM endpoint", "✗", "red", f"Not reachable: {str(e)[:50]}"))

    # Check Elasticsearch
    try:
        from elasticsearch import Elasticsearch
        es = Elasticsearch([config.elasticsearch.url], request_timeout=5)
        if es.ping():
            checks.append(("Elasticsearch", "✓", "green", config.elasticsearch.url))
        else:
            checks.append(("Elasticsearch", "✗", "red", "Not responding"))
    except Exception as e:
        checks.append(("Elasticsearch", "✗", "red", f"Not reachable: {str(e)[:50]}"))

    # Check DR API
    try:
        import httpx
        response = httpx.get(f"{config.dr.api_url}/health", timeout=5)
        if response.status_code == 200:
            checks.append(("DR API", "✓", "green", config.dr.api_url))
        else:
            checks.append(("DR API", "⚠", "yellow", f"Returned {response.status_code}"))
    except Exception as e:
        checks.append(("DR API", "✗", "red", f"Not reachable: {str(e)[:50]}"))

    # Check ClusterCockpit JWT
    jwt = config.get_clustercockpit_jwt()
    if jwt:
        checks.append(("ClusterCockpit JWT", "✓", "green", "Configured in keyring"))
    else:
        checks.append(("ClusterCockpit JWT", "✗", "red", "Not set - run 'hpc config set clustercockpit.jwt YOUR_JWT'"))

    # Display results
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Component", style="cyan")
    table.add_column("Status", justify="center")
    table.add_column("Details", style="dim")

    for name, status, color, details in checks:
        table.add_row(name, f"[{color}]{status}[/{color}]", details)

    console.print(table)

    # Overall status
    all_ok = all(status == "✓" for _, status, _, _ in checks)
    if all_ok:
        console.print("\n[green]✓ All systems operational[/green]")
    else:
        console.print("\n[yellow]⚠ Some issues detected - see above[/yellow]")


def main():
    """Main entry point."""
    try:
        cli()
    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted by user[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[red]Fatal error:[/red] {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
