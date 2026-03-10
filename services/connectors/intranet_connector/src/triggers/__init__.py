"""
Trigger implementations for the Intranet Connector.

Available triggers:
- CLITrigger: Command-line interface for manual execution
- QueueTrigger: Message queue listener for automated execution
- CronTrigger: Scheduled execution based on cron expressions
- APITrigger: REST API for remote execution
"""

from triggers.base import TriggerBase
from triggers.cli import CLITrigger
from triggers.queue import QueueTrigger
from triggers.cron import CronTrigger

__all__ = [
    'TriggerBase',
    'CLITrigger', 
    'QueueTrigger',
    'CronTrigger'
]