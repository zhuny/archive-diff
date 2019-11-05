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

    @classmethod
    def get_by_id(cls, key_id):
        return current_app.datastore.get(
            key=current_app.datastore.key(
                "Work", key_id,
                namespace="Archive"
            )
        )

    @classmethod
    def get_last_rev(cls, page_id):
        query = current_app.datastore.query(
            namespace="Archive",
            kind="WorkResult",
            filters=[('key', '=', page_id)],
            order=['-created_at']
        ).fetch(1)
        for row in query:
            return row


