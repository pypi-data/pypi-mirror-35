from sqlalchemy import and_, or_
from sqlalchemy.orm.query import Query

from .base import BaseLogicalNode


class AndNode(BaseLogicalNode):
    """"""

    def __init__(self) -> None:
        super(AndNode, self).__init__()
        self._method = and_

    def __str__(self) -> str:
        return '<AND node : {}>'.format(id(self))


class OrNode(BaseLogicalNode):
    """"""

    def __init__(self) -> None:
        super(OrNode, self).__init__()

    def __str__(self) -> str:
        return '<OR node : {}>'.format(id(self))
