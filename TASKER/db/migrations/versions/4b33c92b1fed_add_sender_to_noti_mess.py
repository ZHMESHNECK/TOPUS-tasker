"""add sender to noti_mess

Revision ID: 4b33c92b1fed
Revises: 52fb14ffde71
Create Date: 2024-04-06 17:04:18.953013

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4b33c92b1fed'
down_revision: Union[str, None] = '52fb14ffde71'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notificationMessage', sa.Column('sender_id', sa.BigInteger(), nullable=False))
    op.create_foreign_key(None, 'notificationMessage', 'user', ['sender_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'notificationMessage', type_='foreignkey')
    op.drop_column('notificationMessage', 'sender_id')
    # ### end Alembic commands ###