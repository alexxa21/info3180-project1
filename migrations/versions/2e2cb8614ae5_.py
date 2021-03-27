"""empty message

Revision ID: 2e2cb8614ae5
Revises: 
Create Date: 2021-03-27 15:30:23.402368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e2cb8614ae5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property',
    sa.Column('propertyID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.Column('rooms', sa.String(length=10), nullable=True),
    sa.Column('bathrooms', sa.String(length=10), nullable=True),
    sa.Column('price', sa.String(length=20), nullable=True),
    sa.Column('property_type', sa.String(length=20), nullable=True),
    sa.Column('location', sa.String(length=150), nullable=True),
    sa.Column('photo', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('propertyID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('property')
    # ### end Alembic commands ###