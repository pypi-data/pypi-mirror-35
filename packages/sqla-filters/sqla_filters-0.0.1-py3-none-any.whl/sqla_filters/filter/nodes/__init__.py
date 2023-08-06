"""Node package.

In this papckage are defined all the node that can be fin in a filter tree.
Here a list of available nodes:
- Logical
    - BaseLogicalNode
    - AndNode
    - OrNode

- Operator
    - BaseOperatorNode
    - LikeNode
    - EqNode
    - NotEqNode
    - NullNode
    - NotNullNode
    - GtNode
    - GteNode
    - LtNode
    - LteNode
    - InNode
    - NotInNode
    - ContainsNode
"""
from .base import (
    TreeNode,
    BaseLogicalNode,
    BaseOperatorNode,
)
from .logical import (
    OrNode,
    AndNode,
)
from .operator import (
    LikeNode,
    EqNode,
    NotEqNode,
    NullNode,
    NotNullNode,
    GtNode,
    GteNode,
    LtNode,
    LteNode,
    InNode,
    NotInNode,
    ContainsNode
)

OPERATOR_NODES = {
    'like': LikeNode,
    'eq': EqNode,
    'not_eq': NotEqNode,
    'null': NullNode,
    'not_null': NotNullNode,
    'gt': GtNode,
    'gte': GteNode,
    'lt': LtNode,
    'lte': LteNode,
    'in': InNode,
    'not_in': NotInNode,
    'contains': ContainsNode
}

LOGICAL_NODES = {
    'and': AndNode,
    'or': OrNode
}

__all__ = (
    'TreeNode',

    'BaseLogicalNode',
    'AndNode',
    'OrNode',

    'BaseOperatorNode',
    'LikeNode',
    'EqNode',
    'NotEqNode',
    'NullNode',
    'NotNullNode',
    'GtNode',
    'GteNode',
    'LtNode',
    'LteNode',
    'InNode',
    'NotInNode',
    'ContainsNode',

    'OPERATOR_NODES',
    'LOGICAL_NODES',
)

