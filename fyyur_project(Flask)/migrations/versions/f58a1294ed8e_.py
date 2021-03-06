"""empty message

Revision ID: f58a1294ed8e
Revises: fb6002607c0b
Create Date: 2020-12-22 11:38:40.856208

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f58a1294ed8e'
down_revision = 'fb6002607c0b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_description', sa.String(length=600), nullable=True))
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'seeking_venue')
    op.drop_column('Artist', 'seeking_description')
    # ### end Alembic commands ###
