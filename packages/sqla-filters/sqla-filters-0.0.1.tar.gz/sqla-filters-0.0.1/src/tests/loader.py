import os
import json

from .models import (
    Simple,
    Person,
    Author,
    Post
)


def _load_simple(session, data):
    simple_list = data['simple']
    for entity in simple_list:
        session.add(
            Simple(
                name=entity['name'], 
                age=entity['age'],
                average=entity['average']
            )
        )

def _load_person(session, data):
    person_list = data['person']
    for entity in person_list:
        session.add(
            Person(
                name=entity['name']
            )
        )
    session.commit()

def _load_author(session, data):
    author_list = data['author']
    person_list = session.query(Person).all()
    for author, person in zip(author_list, person_list):
        author_instance = Author(author_name=author['author_name'])
        session.add(author_instance)
        person.author = author_instance
    session.commit()


def _load_post(session, data):
    post_list = data['post']
    author_list = session.query(Author).all()
    for index, post in enumerate(post_list):
        post_instance = Post(
            title=post['title'],
            content=post['content'],
            pages=int(post['pages'])
        )
        session.add(post_instance)
        author_list[index%3].posts.append(post_instance)
    session.commit()


def load_models(session):
        path = os.path.join(
            os.path.dirname(__file__),
            'resources/entities.json'
        )
        with open(path) as f:
            data = json.load(f)
            _load_simple(session, data)
            _load_person(session, data)
            _load_author(session, data)
            _load_post(session, data)
