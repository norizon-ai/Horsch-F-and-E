"""Initial migration - create users table

Revision ID: 001_initial
Revises:
Create Date: 2026-03-01 22:00:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import uuid

# revision identifiers, used by Alembic.
revision: str = '001_initial'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create users table with indexes."""
    # NOTE: uuid-ossp is not available on Azure PostgreSQL Flexible Server without allow-listing.
    # Using gen_random_uuid() (available natively since Postgres 13) instead.
    # The allow-listing is done separately via: az postgres flexible-server parameter set --name azure.extensions --value uuid-ossp

    # Create users table
    op.create_table(
        'users',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()'), default=uuid.uuid4),
        sa.Column('auth0_subject', sa.String(255), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('name', sa.String(255), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('last_login', sa.DateTime(timezone=True), nullable=True),
    )

    # Create indexes
    op.create_index(op.f('ix_users_auth0_subject'), 'users', ['auth0_subject'], unique=True)
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=False)


def downgrade() -> None:
    """Drop users table and indexes."""
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_index(op.f('ix_users_auth0_subject'), table_name='users')
    op.drop_table('users')
