"""change phone numer column name in user table

Revision ID: 1631ca3b6477
Revises: b1054339df31
Create Date: 2023-01-25 19:19:07.279287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1631ca3b6477'
down_revision = 'b1054339df31'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    op.drop_column('users', 'phoneNumber')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phoneNumber', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
