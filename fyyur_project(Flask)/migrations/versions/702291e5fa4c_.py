"""empty message

Revision ID: 702291e5fa4c
Revises: c10ed58d29f0
Create Date: 2020-12-21 08:50:55.654005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '702291e5fa4c'
down_revision = 'c10ed58d29f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('website', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'website')
    # ### end Alembic commands ###