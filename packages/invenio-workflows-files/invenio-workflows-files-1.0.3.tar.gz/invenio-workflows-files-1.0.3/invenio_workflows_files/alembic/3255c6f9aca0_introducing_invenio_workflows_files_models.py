# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Alembic migration 3255c6f9aca0."""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.

revision = '3255c6f9aca0'
down_revision = None
branch_labels = (u'invenio_workflows_files', )
depends_on = None


def upgrade():
    """Upgrades alembic."""
    op.create_table('workflows_buckets',
                    sa.Column('workflow_object_id', sa.Integer(),
                              nullable=False),
                    sa.Column('bucket_id',
                              sqlalchemy_utils.types.uuid.UUIDType(),
                              nullable=False),
                    sa.ForeignKeyConstraint(['bucket_id'],
                                            [u'files_bucket.id'],
                                            name=op.f(
                                                'fk_workflows_buckets_bucket'
                                                '_id_files_bucket'),
                                            onupdate='CASCADE',
                                            ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['workflow_object_id'],
                                            [u'workflows_object.id'],
                                            name=op.f(
                                                'fk_workflows_buckets_workflow'
                                                '_object_id_workflows_object'),
                                            onupdate='CASCADE',
                                            ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('workflow_object_id', 'bucket_id',
                                            name=op.f('pk_workflows_buckets'))
                    )


def downgrade():
    """Downgrades alembic."""
    op.drop_table('workflows_buckets')
