"""Carga alturas

Revision ID: b2d60c7e75eb
Revises: bdf65a23680c
Create Date: 2017-07-09 00:35:04.382106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2d60c7e75eb'
down_revision = 'bdf65a23680c'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    res = conn.execute("""COPY alturas (codcalle, desde, hasta, codpostal) FROM"""
        """'/tmp/cpa_argentina/alturas.CSV' DELIMITER ';' HEADER CSV;""")

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###