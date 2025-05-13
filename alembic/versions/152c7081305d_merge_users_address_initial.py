"""merge users, address, initial

Revision ID: 152c7081305d
Revises: 33d37504b0b1, b0f604fc2d7e
Create Date: 2025-05-09 17:33:52.588203

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '152c7081305d'
down_revision: Union[str, None] = ('33d37504b0b1', 'b0f604fc2d7e')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
