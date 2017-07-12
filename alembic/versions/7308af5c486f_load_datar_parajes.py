"""Load datar parajes

Revision ID: 7308af5c486f
Revises: d856dd59fc5a
Create Date: 2017-07-11 12:58:22.624108

"""
import os
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7308af5c486f'
down_revision = 'd856dd59fc5a'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    cwd = os.getcwd()
    path = os.path.join(cwd, 'cpa_csv', 'parajes.csv')
    res = conn.execute(
        sa.text("COPY datar_parajes (id, id_provincia, nombre) FROM :path DELIMITER ',' HEADER CSV;"),
        path=path
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
