"""Cluster monitoring commands."""

from rich.console import Console

console = Console()


async def find_underutilized_gpus(
    days: int,
    max_util: float,
    min_duration: float,
    output_format: str,
    save_path: str = None
) -> None:
    """Find underutilized GPU jobs.

    Args:
        days: Days to look back
        max_util: Maximum GPU utilization threshold
        min_duration: Minimum job duration in hours
        output_format: Output format (table, json, csv)
        save_path: Optional file path to save results
    """
    console.print(f"\n[bold]GPU Utilization Analysis[/bold]")
    console.print(f"Looking back {days} days for jobs with <{max_util}% GPU usage\n")

    console.print("[yellow]⚠️  Cluster monitoring integration coming soon![/yellow]")
    console.print("\nThis will integrate ClusterCockpit API to:")
    console.print("  • Query job data from clusters")
    console.print("  • Analyze GPU utilization metrics")
    console.print("  • Generate waste reports")
    console.print(f"  • Export to {output_format}\n")


async def rank_worst_users(
    days: int,
    top_n: int,
    output_format: str,
    save_path: str = None
) -> None:
    """Rank users by GPU waste.

    Args:
        days: Days to analyze
        top_n: Number of users to show
        output_format: Output format (table, json)
        save_path: Optional file path to save results
    """
    console.print(f"\n[bold]GPU Waste Ranking[/bold]")
    console.print(f"Analyzing last {days} days, showing top {top_n} users\n")

    console.print("[yellow]⚠️  Cluster monitoring integration coming soon![/yellow]")
    console.print("\nThis will calculate waste scores based on:")
    console.print("  • GPU-hours wasted")
    console.print("  • GPU type weighting (H200/H100/A100/A40)")
    console.print("  • Utilization penalties")
    console.print(f"  • Export to {output_format}\n")
