import sqlalchemy as sa
from pypi.data.modelbase import SqlAlchemyBase

# noinspection PyUnresolvedReferences
import pypi.data.__all_models


class Package(SqlAlchemyBase):

    __tablename__ = 'packages'

    id = sa.Column(sa.String, primary_key=True)
    created_date = sa.Column(sa.DateTime)
    summary = sa.Column(sa.String)
    description = sa.Column(sa.String)

    home_page = sa.Column(sa.String)
    docs_url = sa.Column(sa.String)
    package_url = sa.Column(sa.String)

    author_name = sa.Column(sa.String)
    author_email = sa.Column(sa.String)

    license = sa.Column(sa.String)
