"""create_table_transactions

Revision ID: 027f029a644f
Revises: 09f7da264602
Create Date: 2024-11-04 22:17:29.142048

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '027f029a644f'
down_revision: Union[str, None] = '09f7da264602'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('DEPOSIT', 'WITHDRAWAL', name='transaction_types'), nullable=False),
    sa.Column('amount', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('timestamp', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['accounts.id'], ),
    sa.PrimaryKeyConstraint('id'))


def downgrade() -> None:
    op.drop_table('transactions')
