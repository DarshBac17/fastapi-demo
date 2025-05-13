"""merging

Revision ID: 598b38471b53
Revises: fd39cdcb2d98, 6ce24ee64e05
Create Date: 2025-05-13 11:04:53.962206

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '598b38471b53'
down_revision: Union[str, None] = ('fd39cdcb2d98', '6ce24ee64e05')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
