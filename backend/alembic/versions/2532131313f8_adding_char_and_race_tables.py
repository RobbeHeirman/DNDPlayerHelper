"""adding char and race tables

Revision ID: 2532131313f8
Revises: e77393c032cf
Create Date: 2023-10-17 21:23:50.313685

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2532131313f8'
down_revision: Union[str, None] = 'e77393c032cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character_sheet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_name', sa.String(), nullable=False),
    sa.Column('lvl', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('class',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('race',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('race')
    op.drop_table('class')
    op.drop_table('character_sheet')
    # ### end Alembic commands ###
