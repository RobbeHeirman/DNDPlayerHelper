"""add Resistances

Revision ID: 2b03739cbcec
Revises: f6e564e57a57
Create Date: 2023-10-19 16:59:26.927929

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b03739cbcec'
down_revision: Union[str, None] = 'f6e564e57a57'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('damage_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_damage_type'))
    )
    op.create_table('character_resistance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_sheet_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['character_sheet_id'], ['character_sheet.id'], name=op.f('fk_character_resistance_character_sheet_id_character_sheet')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_character_resistance'))
    )
    with op.batch_alter_table('character_sheet', schema=None) as batch_op:
        batch_op.add_column(sa.Column('strength', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('dexterity', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('intelligence', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('wisdom', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('charisma', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character_sheet', schema=None) as batch_op:
        batch_op.drop_column('charisma')
        batch_op.drop_column('wisdom')
        batch_op.drop_column('intelligence')
        batch_op.drop_column('dexterity')
        batch_op.drop_column('strength')

    op.drop_table('character_resistance')
    op.drop_table('damage_type')
    # ### end Alembic commands ###
