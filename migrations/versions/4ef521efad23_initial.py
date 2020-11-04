"""initial

Revision ID: 4ef521efad23
Revises: 58e359cf2d19
Create Date: 2020-11-04 15:57:13.710010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ef521efad23'
down_revision = '58e359cf2d19'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('voters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('national_id', sa.String(), nullable=True),
    sa.Column('passport', sa.String(), nullable=True),
    sa.Column('first_name', sa.String(length=255), nullable=True),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('voted', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('voters')
    # ### end Alembic commands ###