import os
import json

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
import pytest

from .db import Base
from .loader import load_models
from .models import (
    Simple,
    Person,
    Author,
    Post
)


def removeTestDb():
    os.remove('test.db')

@pytest.fixture(scope='session', autouse=True)
def load_test_models(request):
    engine = sa.create_engine('sqlite:///test.db')
    DBSession = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = DBSession()
    load_models(session)
    # Run callback 'removeTestDb' when all tests are finished
    request.addfinalizer(removeTestDb)


class TestBasicRequest(object):
    def setup_class(self):
        self._engine = sa.create_engine('sqlite:///test.db')
        self._DBSession = sessionmaker(bind=self._engine)
        self._session = self._DBSession()

    def teardown_class(self):
        self._session.close()

    def test_1_count(self):
        count = self._session \
            .query(Simple) \
            .count()
        assert count == 4

    def test_2_simple_request(self):
        entity = self._session \
            .query(Simple) \
            .filter_by(name='Toto') \
            .first()
        assert entity.name == 'Toto'
        assert entity.age == 20
