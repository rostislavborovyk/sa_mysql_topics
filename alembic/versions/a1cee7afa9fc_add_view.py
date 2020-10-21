"""add view

Revision ID: a1cee7afa9fc
Revises: c3d696e072c7
Create Date: 2020-10-21 11:11:05.541269

"""
from alembic import op
import sqlalchemy as sa

import os
# from os.path import abspath, dirname
# sys.path.insert(0, dirname(abspath(__file__)))
print(os.path)

from replaceable_object import ReplaceableObject

# revision identifiers, used by Alembic.
revision = 'a1cee7afa9fc'
down_revision = 'c3d696e072c7'
branch_labels = None
depends_on = None

premium_users_view = ReplaceableObject(
    "premium_users_view",
    "SELECT name FROM users WHERE premium_user = 1"
)


def upgrade():
    op.create_view(premium_users_view)


def downgrade():
    op.drop_view(premium_users_view)
