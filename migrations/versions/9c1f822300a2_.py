"""empty message

Revision ID: 9c1f822300a2
Revises: 8a94c7daec3b
Create Date: 2022-01-12 11:09:53.880308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c1f822300a2'
down_revision = '8a94c7daec3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('resource', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('question', 'resource')
    # ### end Alembic commands ###