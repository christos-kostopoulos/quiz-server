"""create choice and question  migr ation.

Revision ID: 8a94c7daec3b
Revises: af7bb67dc3a6
Create Date: 2022-01-01 18:24:43.468449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a94c7daec3b'
down_revision = 'af7bb67dc3a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('questionTitle', sa.Text(), nullable=True),
    sa.Column('quiz_id', sa.Integer(), nullable=False),
    sa.Column('explanation', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['quiz_id'], ['quiz.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('choice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('choice', sa.Text(), nullable=True),
    sa.Column('is_right_choice', sa.Boolean(), nullable=True),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('choice')
    op.drop_table('question')
    # ### end Alembic commands ###