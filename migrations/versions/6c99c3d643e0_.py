"""empty message

Revision ID: 6c99c3d643e0
Revises: 30090e584ec5
Create Date: 2019-04-10 10:12:41.882550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c99c3d643e0'
down_revision = '30090e584ec5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'test')
    op.drop_column('users', 'admin')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('admin', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('test', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
