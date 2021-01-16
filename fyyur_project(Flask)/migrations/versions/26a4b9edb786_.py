"""empty message

Revision ID: 26a4b9edb786
Revises: 702291e5fa4c
Create Date: 2020-12-21 09:27:15.095972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26a4b9edb786'
down_revision = '702291e5fa4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('venue_id', sa.Integer(), nullable=False))
    op.drop_constraint('shows_venu_id_fkey', 'shows', type_='foreignkey')
    op.create_foreign_key(None, 'shows', 'Venue', ['venue_id'], ['id'])
    op.drop_column('shows', 'venu_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shows', sa.Column('venu_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'shows', type_='foreignkey')
    op.create_foreign_key('shows_venu_id_fkey', 'shows', 'Venue', ['venu_id'], ['id'])
    op.drop_column('shows', 'venue_id')
    # ### end Alembic commands ###
