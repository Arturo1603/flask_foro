"""change

Revision ID: 71fba1c73ee5
Revises: b7997480de8c
Create Date: 2022-10-26 13:15:17.615122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71fba1c73ee5'
down_revision = 'b7997480de8c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('publication', sa.Column('title', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('publication', 'title')
    # ### end Alembic commands ###
