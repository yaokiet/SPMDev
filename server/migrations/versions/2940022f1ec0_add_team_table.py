"""Add Team table

Revision ID: 2940022f1ec0
Revises: f0dd244d7999
Create Date: 2024-09-23 14:12:39.533001

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2940022f1ec0'
down_revision = 'f0dd244d7999'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teams',
    sa.Column('Team_ID', sa.Integer(), nullable=False),
    sa.Column('Team_Name', sa.String(length=20), nullable=False),
    sa.Column('Team_Lead_ID', sa.Integer(), nullable=True),
    sa.Column('Dept', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['Team_Lead_ID'], ['employees.Staff_ID'], ),
    sa.PrimaryKeyConstraint('Team_ID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teams')
    # ### end Alembic commands ###
