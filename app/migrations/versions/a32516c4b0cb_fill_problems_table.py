"""fill problems table

Revision ID: a32516c4b0cb
Revises: 4dd0b08f77e4
Create Date: 2025-02-22 20:36:13.711006

"""
import json
import os
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a32516c4b0cb'
down_revision: Union[str, None] = '4dd0b08f77e4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


DATA_DIR = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'problems_json_storage')
def upgrade():

    data_to_insert = []
    for filename in os.listdir(DATA_DIR):
        file_path = os.path.join(DATA_DIR, filename)
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)

                row_data = {
                    'name': data['name'],
                    'category': data['category'],
                    'difficulty': data['difficulty'],
                    'description': data['description'],
                    'recommended_time_complexity': data['recommended_time_complexity'],
                    'recommended_space_complexity': data['recommended_space_complexity'],
                    'testcases': data['testcases']
                }
                data_to_insert.append(row_data)
            except Exception as e:
                print(f"Error processing file {filename}: {e}")

    if data_to_insert:
        op.bulk_insert(
            sa.table('problems',
                sa.Column('id', sa.Integer),
                sa.Column('name', sa.String),
                sa.Column('category', sa.String),
                sa.Column('difficulty', sa.String),
                sa.Column('description', sa.String),
                sa.Column('recommended_time_complexity', sa.String),
                sa.Column('recommended_space_complexity', sa.String),
                sa.Column('testcases', sa.JSON)
            ),
            data_to_insert
        )


def downgrade():
    op.execute(sa.text("DELETE FROM problems"))
