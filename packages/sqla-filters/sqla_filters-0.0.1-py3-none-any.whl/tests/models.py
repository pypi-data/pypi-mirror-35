import sqlalchemy as sa
from sqlalchemy.orm import relationship

from .db import Base


class Simple(Base):
    __tablename__ = 'simple'

    s_id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(50))
    age = sa.Column(sa.Integer)
    average = sa.Column(sa.Float)


class Post(Base):
    __tablename__ = 'post'

    p_id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(100))
    content = sa.Column(sa.String)
    pages = sa.Column(sa.Integer)
    author_id = sa.Column(sa.Integer, sa.ForeignKey('author.a_id'))
    author = relationship('Author', back_populates='posts')

    def __str__(self):
        return '{} | {}'.format(self.title, self.content)


class Author(Base):
    __tablename__ = 'author'

    a_id = sa.Column(sa.Integer, primary_key=True)
    author_name = sa.Column(sa.String(50))
    posts = relationship('Post', back_populates='author')
    person_id = sa.Column(sa.Integer, sa.ForeignKey('person.p_id'))
    person = relationship('Person', back_populates="author")

    def __str__(self):
        return '{}'.format(self.author_name)

class Person(Base):
    __tablename__ = 'person'

    p_id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(50))
    author = relationship('Author', uselist=False, back_populates="person")

    def __str__(self):
        return '{}'.format(self.name)
