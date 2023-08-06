import os

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from sqla_filters.parser import JSONFiltersParser

from ..db import Base
from ..loader import load_models

from ..models import (
    Simple,
    Person,
    Author,
    Post
)


class TestEquality(object):
    def setup_class(self):
        self._engine = sa.create_engine('sqlite:///test.db')
        self._DBSession = sessionmaker(bind=self._engine)
        self._session = self._DBSession()

    def teardown_class(self):
        self._session.close()

    def test_1_eq(self):
        data = '{ \
            "type": "and", \
            "data": [\
                { \
                    "type": "operator", \
                    "data": { \
                        "attribute": "name", \
                        "operator": "eq", \
                        "value": "Toto" \
                    }\
                } \
            ] \
        }'
        parser = JSONFiltersParser(data)
        query = self._session \
            .query(Simple)
        result = parser.tree.filter(query).first()
        assert result.name == 'Toto'
        assert result.age == 20
        assert result.average == 10

    def test_2_not_eq(self):
        data = '{ \
            "type": "and", \
            "data": [\
                { \
                    "type": "operator", \
                    "data": { \
                        "attribute": "name", \
                        "operator": "not_eq", \
                        "value": "Toto" \
                    }\
                } \
            ] \
        }'
        parser = JSONFiltersParser(data)
        query = self._session \
            .query(Simple)
        results = parser.tree.filter(query).all()
        assert len(results) == 3

    def test_3_eq_relation(self):
        data = '{ \
            "type": "and", \
            "data": [\
                { \
                    "type": "operator", \
                    "data": { \
                        "attribute": "author.person.name", \
                        "operator": "eq", \
                        "value": "Person_1" \
                    }\
                } \
            ] \
        }'
        parser = JSONFiltersParser(data)
        query = self._session \
            .query(Post)
        results = parser.tree.filter(query).first()
        assert results.title == 'post_1'
        assert results.content == 'content_1'

    def test_4_not_eq_relation(self):
        data = '{ \
            "type": "and", \
            "data": [\
                { \
                    "type": "operator", \
                    "data": { \
                        "attribute": "author.person.name", \
                        "operator": "not_eq", \
                        "value": "Person_1" \
                    }\
                } \
            ] \
        }'
        parser = JSONFiltersParser(data)
        query = self._session \
            .query(Post)
        results = parser.tree.filter(query).all()
        assert len(results) == 4
        assert results[0].title == 'post_2'
        assert results[0].content == 'content_2'
        assert results[1].title == 'post_3'
        assert results[1].content == 'content_3'
        assert results[2].title == 'post_5'
        assert results[2].content == 'content_5'
        assert results[3].title == 'post_6'
        assert results[3].content == 'content_6'


class TestNull(object):
    def setup_class(self):
        self._engine = sa.create_engine('sqlite:///test.db')
        self._DBSession = sessionmaker(bind=self._engine)
        self._session = self._DBSession()

    def teardown_class(self):
        self._session.close()

    def test_1_null(self):
        data = '{ \
            "type": "and", \
            "data": [ \
                { \
                    "type": "operator", \
                    "data": { \
                        "attribute": "average", \
                        "operator": "null", \
                        "value": null \
                    } \
                } \
            ] \
        }'
        parser = JSONFiltersParser(data)
        query = self._session \
            .query(Simple)
        result = parser.tree.filter(query).first()
        assert result.name == 'Tata'
        assert result.age == 23
        assert result.average == None

    def test_2_not_null(self):
        data = '{ \
            "type": "and", \
            "data": [\
                { \
                    "type": "operator", \
                    "data": { \
                        "attribute": "average", \
                        "operator": "not_null", \
                        "value": "" \
                    } \
                } \
            ] \
        }'
        parser = JSONFiltersParser(data)
        query = self._session \
            .query(Simple)
        results = parser.tree.filter(query).all()
        assert len(results) == 3


class TestGreater(object):
    def setup_class(self):
        self._engine = sa.create_engine('sqlite:///test.db')
        self._DBSession = sessionmaker(bind=self._engine)
        self._session = self._DBSession()

    def teardown_class(self):
        self._session.close()

    def test_1_gt(self):
        data = '{ \
            "type": "and", \
            "data": [ \
                { \
                    "type": "operator", \
                    "data": { \
                        "attribute": "age", \
                        "operator": "gt", \
                        "value": 21 \
                    } \
                }\
            ] \
        }'
        parser = JSONFiltersParser(data)
        query = self._session \
            .query(Simple)
        results = parser.tree.filter(query).all()
        assert len(results) == 2

    def test_2_gte(self):
        data = '{ \
            "type": "and", \
            "data": [ \
                { \
                    "type": "operator", \
                    "data": { \
                        "attribute": "age", \
                        "operator": "gte", \
                        "value": 21 \
                    } \
                }\
            ] \
        }'
        parser = JSONFiltersParser(data)
        query = self._session \
            .query(Simple)
        results = parser.tree.filter(query).all()
        assert len(results) == 3

    def test_3_gt_relation(self):
        data = '{ \
            "type": "and", \
            "data": [ \
                { \
                    "type": "operator", \
                    "data": { \
                        "attribute": "author.posts.pages", \
                        "operator": "gt", \
                        "value": 7 \
                    } \
                }\
            ] \
        }'
        parser = JSONFiltersParser(data)
        query = self._session \
            .query(Person)
        results = parser.tree.filter(query).all()
        assert len(results) == 1
        assert results[0].name == 'Person_3'

    def test_4_gte_relation(self):
        data = '{ \
            "type": "and", \
            "data": [ \
                { \
                    "type": "operator", \
                    "data": { \
                        "attribute": "author.posts.pages", \
                        "operator": "gte", \
                        "value": 7 \
                    } \
                }\
            ] \
        }'
        parser = JSONFiltersParser(data)
        query = self._session \
            .query(Person)
        results = parser.tree.filter(query).all()
        assert len(results) == 2
        assert results[0].name == 'Person_1'
        assert results[1].name == 'Person_3'


class TestLower(object):
    def setup_class(self):
        self._engine = sa.create_engine('sqlite:///test.db')
        self._DBSession = sessionmaker(bind=self._engine)
        self._session = self._DBSession()

    def teardown_class(self):
        self._session.close()

    def test_1_lt(self):
        data = '{ \
            "type": "and", \
            "data": [ \
                { \
                    "type": "operator", \
                    "data": { \
                        "attribute": "age", \
                        "operator": "lt", \
                        "value": 23 \
                    } \
                }\
            ] \
        }'
        parser = JSONFiltersParser(data)
        query = self._session \
            .query(Simple)
        results = parser.tree.filter(query).all()
        assert len(results) == 3

    def test_2_lte(self):
        data = '{ \
            "type": "and", \
            "data": [ \
                { \
                    "type": "operator", \
                    "data": { \
                        "attribute": "age", \
                        "operator": "lte", \
                        "value": 23 \
                    } \
                }\
            ] \
        }'
        parser = JSONFiltersParser(data)
        query = self._session \
            .query(Simple)
        results = parser.tree.filter(query).all()
        assert len(results) == 4

    def test_3_lt_relation(self):
        data = '{ \
            "type": "and", \
            "data": [ \
                { \
                    "type": "operator", \
                    "data": { \
                        "attribute": "author.posts.pages", \
                        "operator": "lt", \
                        "value": 4 \
                    } \
                }\
            ] \
        }'
        parser = JSONFiltersParser(data)
        query = self._session \
            .query(Person)
        results = parser.tree.filter(query).all()
        assert len(results) == 2
        assert results[0].name == 'Person_1'
        assert results[1].name == 'Person_3'

    def test_4_lte_relation(self):
        data = '{ \
            "type": "and", \
            "data": [ \
                { \
                    "type": "operator", \
                    "data": { \
                        "attribute": "author.posts.pages", \
                        "operator": "lte", \
                        "value": 4 \
                    } \
                }\
            ] \
        }'
        parser = JSONFiltersParser(data)
        query = self._session \
            .query(Person)
        results = parser.tree.filter(query).all()
        assert len(results) == 3
        assert results[0].name == 'Person_1'
        assert results[1].name == 'Person_3'
        assert results[2].name == 'Person_2'


class TestIn(object):
    def setup_class(self):
        self._engine = sa.create_engine('sqlite:///test.db')
        self._DBSession = sessionmaker(bind=self._engine)
        self._session = self._DBSession()

    def teardown_class(self):
        self._session.close()

    def test_1_in(self):
        data = '{ \
            "type": "and", \
            "data": [ \
                { \
                    "type": "operator", \
                    "data": { \
                        "attribute": "name", \
                        "operator": "in", \
                        "value": ["Toto", "Titi"] \
                    } \
                } \
            ] \
        }'
        parser = JSONFiltersParser(data)
        query = self._session \
            .query(Simple)
        results = parser.tree.filter(query).all()
        assert len(results) == 2
        assert results[0].name == 'Toto'
        assert results[0].age == 20
        assert results[0].average == 10
        assert results[1].name == 'Titi'
        assert results[1].age == 21
        assert results[1].average == 12.3

    def test_2_not_in(self):
        data = '{ \
            "type": "and", \
            "data": [ \
                { \
                    "type": "operator", \
                    "data": { \
                        "attribute": "name", \
                        "operator": "not_in", \
                        "value": ["Toto", "Titi"] \
                    } \
                } \
            ] \
        }'
        parser = JSONFiltersParser(data)
        query = self._session \
            .query(Simple)
        results = parser.tree.filter(query).all()
        assert len(results) == 2
        assert results[0].name == 'Tutu'
        assert results[0].age == 22
        assert results[0].average == 9.6
        assert results[1].name == 'Tata'
        assert results[1].age == 23
        assert results[1].average == None

    def test_3_in_relation(self):
        data = '{ \
            "type": "and", \
            "data": [ \
                { \
                    "type": "operator", \
                    "data": { \
                        "attribute": "author.person.name", \
                        "operator": "in", \
                        "value": ["Person_1", "Person_3"] \
                    } \
                } \
            ] \
        }'
        parser = JSONFiltersParser(data)
        query = self._session \
            .query(Post)
        results = parser.tree.filter(query).all()
        assert len(results) == 4
        assert results[0].title == 'post_1'
        assert results[0].content == 'content_1'
        assert results[1].title == 'post_3'
        assert results[1].content == 'content_3'
        assert results[2].title == 'post_4'
        assert results[2].content == 'content_4'
        assert results[3].title == 'post_6'
        assert results[3].content == 'content_6'

    def test_4_not_in_relation(self):
        data = '{ \
            "type": "and", \
            "data": [ \
                { \
                    "type": "operator", \
                    "data": { \
                        "attribute": "author.person.name", \
                        "operator": "not_in", \
                        "value": ["Person_1", "Person_3"] \
                    } \
                } \
            ] \
        }'
        parser = JSONFiltersParser(data)
        query = self._session \
            .query(Post)
        results = parser.tree.filter(query).all()
        assert len(results) == 2
        assert results[0].title == 'post_2'
        assert results[0].content == 'content_2'
        assert results[1].title == 'post_5'
        assert results[1].content == 'content_5'
