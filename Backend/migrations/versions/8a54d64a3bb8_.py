"""empty message

Revision ID: 8a54d64a3bb8
Revises: 7e54da17f6f6
Create Date: 2023-06-07 07:18:19.837160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a54d64a3bb8'
down_revision = '7e54da17f6f6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('startDay', sa.Date(), nullable=False),
    sa.Column('endDay', sa.Date(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('creatorId', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['creatorId'], ['user.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('schedule',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Day', sa.Date(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('creatorId', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['creatorId'], ['user.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('schedule')
    op.drop_table('goal')
    # ### end Alembic commands ###