"""chat

Revision ID: eaf337668371
Revises: 100b56aa05ba
Create Date: 2024-03-23 21:49:51.266191

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eaf337668371'
down_revision: Union[str, None] = '100b56aa05ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chat_users',
    sa.Column('chat_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['chat_id'], ['chat.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('chat_id', 'user_id')
    )
    op.create_table('message',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('chat_id', sa.BigInteger(), nullable=False),
    sa.Column('sender_id', sa.BigInteger(), nullable=False),
    sa.Column('message', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['chat_id'], ['chat.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_message_chat_id'), 'message', ['chat_id'], unique=False)
    op.add_column('chat', sa.Column('chat', sa.VARCHAR(), nullable=False))
    op.drop_index('ix_chat_chat_id', table_name='chat')
    op.create_index(op.f('ix_chat_chat'), 'chat', ['chat'], unique=False)
    op.drop_column('chat', 'chat_id')
    op.drop_column('chat', 'message')
    op.drop_column('chat', 'sender')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chat', sa.Column('sender', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('chat', sa.Column('message', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('chat', sa.Column('chat_id', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_chat_chat'), table_name='chat')
    op.create_index('ix_chat_chat_id', 'chat', ['chat_id'], unique=False)
    op.drop_column('chat', 'chat')
    op.drop_index(op.f('ix_message_chat_id'), table_name='message')
    op.drop_table('message')
    op.drop_table('chat_users')
    # ### end Alembic commands ###
