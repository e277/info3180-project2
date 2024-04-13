"""empty message

Revision ID: dda762336fe6
Revises: 0b99b03a2b29
Create Date: 2024-04-13 14:37:11.162645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dda762336fe6'
down_revision = '0b99b03a2b29'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.alter_column('biography',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=1000),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.alter_column('biography',
               existing_type=sa.String(length=1000),
               type_=sa.VARCHAR(length=80),
               existing_nullable=True)

    # ### end Alembic commands ###
