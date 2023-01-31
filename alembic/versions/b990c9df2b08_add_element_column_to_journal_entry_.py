"""add element column to journal entry table

Revision ID: b990c9df2b08
Revises: 346edf6dd42c
Create Date: 2023-01-28 21:20:44.222042

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b990c9df2b08'
down_revision = '346edf6dd42c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('journalEntries', sa.Column('elements', postgresql.ARRAY(postgresql.JSONB(astext_type=sa.Text())), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('journalEntries', 'elements')
    # ### end Alembic commands ###