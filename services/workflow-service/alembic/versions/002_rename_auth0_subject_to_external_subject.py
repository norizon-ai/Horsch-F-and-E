"""Rename auth0_subject to external_subject for provider-agnostic auth.

Revision ID: 002_rename_auth0
Revises: edef795911c6
Create Date: 2026-03-11
"""
from alembic import op

# revision identifiers
revision = '002_rename_auth0'
down_revision = 'edef795911c6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('users', 'auth0_subject', new_column_name='external_subject')
    op.drop_index('ix_users_auth0_subject', table_name='users')
    op.create_index('ix_users_external_subject', 'users', ['external_subject'], unique=True)


def downgrade() -> None:
    op.alter_column('users', 'external_subject', new_column_name='auth0_subject')
    op.drop_index('ix_users_external_subject', table_name='users')
    op.create_index('ix_users_auth0_subject', 'users', ['auth0_subject'], unique=True)
