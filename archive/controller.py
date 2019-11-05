from operator import attrgetter

from flask import current_app
from google.cloud.datastore import Key


class PageController:
    # define classmethod to use controller

    @classmethod
    def get_list(cls):
        query = current_app.datastore.query(
            namespace="Archive",
            kind="Work"
        )
        result = list(query.fetch())
        result.sort(key=attrgetter("id"))
        return result

    @classmethod
    def get_by_id(cls, key_id):
        return current_app.datastore.get(
            key=current_app.datastore.key(
                "Work", key_id,
                namespace="Archive"
            )
        )


