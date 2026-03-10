"""Seed initial workflow types

Revision ID: edef795911c6
Revises: 2e50be0cc046
Create Date: 2026-03-01 21:52:40.714990

"""
from typing import Sequence, Union
import uuid

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision: str = 'edef795911c6'
down_revision: Union[str, None] = '2e50be0cc046'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Insert initial workflow types."""
    workflows_table = sa.table(
        'workflows',
        sa.column('id', UUID(as_uuid=True)),
        sa.column('name', sa.String),
        sa.column('description', sa.String),
    )

    # Define workflow types with fixed UUIDs for consistency
    workflow_types = [
        {
            'id': uuid.UUID('00000000-0000-0000-0000-000000000001'),
            'name': 'Search',
            'description': 'Knowledge search and chat-based interactions'
        },
        {
            'id': uuid.UUID('00000000-0000-0000-0000-000000000002'),
            'name': 'Meeting Documentation',
            'description': 'AI-powered meeting transcription and documentation workflow'
        },
        {
            'id': uuid.UUID('00000000-0000-0000-0000-000000000003'),
            'name': 'Offboarding',
            'description': 'Employee offboarding and knowledge transfer workflow'
        }
    ]

    op.bulk_insert(workflows_table, workflow_types)


def downgrade() -> None:
    """Remove seeded workflow types."""
    op.execute(
        """
        DELETE FROM workflows
        WHERE id IN (
            '00000000-0000-0000-0000-000000000001',
            '00000000-0000-0000-0000-000000000002',
            '00000000-0000-0000-0000-000000000003'
        )
        """
    )
