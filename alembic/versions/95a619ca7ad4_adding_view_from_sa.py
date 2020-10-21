"""adding view from sa

Revision ID: 95a619ca7ad4
Revises: c3d696e072c7
Create Date: 2020-10-21 11:32:54.305308

"""
from alembic import op
import sqlalchemy as sa
from replaceable_object import ReplaceableObject
from models import premium_members

# revision identifiers, used by Alembic.
revision = '95a619ca7ad4'
down_revision = 'c3d696e072c7'
branch_labels = None
depends_on = None

premium_users_view = ReplaceableObject(
    "premium_users_view",
    str(premium_members)
)


def upgrade():
    op.create_view(premium_users_view)


def downgrade():
    op.drop_view(premium_users_view)

