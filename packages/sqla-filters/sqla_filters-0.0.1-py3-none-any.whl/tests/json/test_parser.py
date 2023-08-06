from sqla_filters.parser import JSONFiltersParser
from sqla_filters.filter import (
    AndNode,
    EqNode
)

class TestJsonFilterParser(object):
    def setup_class(self):
        self._data = '{ \
            "type": "and", \
            "data": [ \
                { \
                    "type": "operator", \
                    "data": { \
                        "attribute": "name", \
                        "operator": "eq", \
                        "value": "toto" \
                    } \
                }, \
                { \
                    "type": "operator", \
                    "data": { \
                        "attribute": "age", \
                        "operator": "eq", \
                        "value": 20 \
                    } \
                } \
            ] \
        }'
        self._jparser = JSONFiltersParser(self._data)

    def test_1_raw_data(self):
        assert self._jparser.raw_data == self._data

    def test_2_parse_data(self):
        tree = self._jparser.tree
        assert isinstance(tree.root, AndNode)
        assert len(tree.root.childs) == 2

        child1 = tree.root.childs[0]
        assert isinstance(child1, EqNode)
        assert child1.attribute == 'name'
        assert child1.value == 'toto'

        child2 = tree.root.childs[1]
        assert isinstance(child2, EqNode)
        assert child2.attribute == 'age'
        assert child2.value == 20
