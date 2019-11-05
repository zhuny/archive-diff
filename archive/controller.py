from operator import attrgetter

from flask import current_app


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


