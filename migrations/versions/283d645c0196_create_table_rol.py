"""create table rol

Revision ID: 283d645c0196
Revises: 5fb9e5ab8bc4
Create Date: 2022-10-13 16:15:16.599900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '283d645c0196'
down_revision = '5fb9e5ab8bc4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles')
    # ### end Alembic commands ###
