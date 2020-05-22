"""empty message

Revision ID: 7e0ae727f97d
Revises: be692153eac1
Create Date: 2020-05-21 07:33:05.594863

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e0ae727f97d'
down_revision = 'be692153eac1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('subscribers_user_id_fkey', 'subscribers', type_='foreignkey')
    op.drop_column('subscribers', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscribers', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('subscribers_user_id_fkey', 'subscribers', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###
