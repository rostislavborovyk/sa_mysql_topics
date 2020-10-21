"""generated column employeesCount

Revision ID: 94d62878e1ad
Revises: 0fadb549841a
Create Date: 2020-10-21 20:17:08.369480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94d62878e1ad'
down_revision = '0fadb549841a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departments', sa.Column('employeesCount', sa.Integer(), sa.Computed("`attributes` ->> '$.employeesCount'", ), nullable=True))
    op.create_index(op.f('ix_departments_employeesCount'), 'departments', ['employeesCount'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_departments_employeesCount'), table_name='departments')
    op.drop_column('departments', 'employeesCount')
    # ### end Alembic commands ###