"""add journal entries column to user table

Revision ID: 01e190b17189
Revises: cb76836f4e47
Create Date: 2023-02-07 11:19:52.932356

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '01e190b17189'
down_revision = 'cb76836f4e47'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('journal_entries', postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'[]'::jsonb"), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'journal_entries')
    # ### end Alembic commands ###
