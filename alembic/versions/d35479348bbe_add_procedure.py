"""add_procedure

Revision ID: d35479348bbe
Revises: 95a619ca7ad4
Create Date: 2020-10-21 12:21:39.483530

"""
from alembic import op
import sqlalchemy as sa

from models import insert_user
from replaceable_object import ReplaceableObject

insert_user_sp = ReplaceableObject(
    "insert_user_sp",
    insert_user
)

# revision identifiers, used by Alembic.
revision = 'd35479348bbe'
down_revision = '95a619ca7ad4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_sp(insert_user_sp)


def downgrade():
    op.drop_sp(insert_user_sp)

