"""8

Revision ID: 7e51ed7e999b
Revises: aee615d56af4
Create Date: 2023-01-20 16:32:02.863801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e51ed7e999b'
down_revision = 'aee615d56af4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('submenu', sa.Column('menu_id', sa.Integer(), nullable=True))
    op.drop_constraint('submenu_menu_fkey', 'submenu', type_='foreignkey')
    op.create_foreign_key(None, 'submenu', 'menu', ['menu_id'], ['id'])
    op.drop_column('submenu', 'menu')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('submenu', sa.Column('menu', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'submenu', type_='foreignkey')
    op.create_foreign_key('submenu_menu_fkey', 'submenu', 'menu', ['menu'], ['id'])
    op.drop_column('submenu', 'menu_id')
    # ### end Alembic commands ###
