"""Add initial tables

Revision ID: 09f7da264602
Revises: 
Create Date: 2024-04-16 19:45:59.524806

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '09f7da264602'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('balance', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_accounts_user_id'), 'accounts', ['user_id'], unique=False)
    


def downgrade() -> None:
    op.drop_index(op.f('ix_accounts_user_id'), table_name='accounts')
    op.drop_table('accounts')
