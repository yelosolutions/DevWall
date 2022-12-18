"""User name and password nullable=True

Revision ID: 178e1ce07f84
Revises: 86ca1d56bec2
Create Date: 2022-12-10 17:20:11.016817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '178e1ce07f84'
down_revision = '86ca1d56bec2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('user', 'name',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'name',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###