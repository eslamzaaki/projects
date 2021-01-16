"""empty message

Revision ID: e0a6d3a191bb
Revises: 371b67c44964
Create Date: 2020-12-19 11:58:40.039009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0a6d3a191bb'
down_revision = '371b67c44964'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todolists', sa.Column('completed', sa.Boolean(), nullable=True))
    op.drop_constraint('todos_list_id_fkey', 'todos', type_='foreignkey')
    op.create_foreign_key(None, 'todos', 'todolists', ['list_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todos', type_='foreignkey')
    op.create_foreign_key('todos_list_id_fkey', 'todos', 'todolists', ['list_id'], ['id'], ondelete='CASCADE')
    op.drop_column('todolists', 'completed')
    # ### end Alembic commands ###