import datetime
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

    @classmethod
    def get_rev_list(cls, page_id):
        query = current_app.datastore.query(
            namespace="Archive",
            kind="WorkResult",
            filters=[('key', '=', page_id)],
            order=['-created_at'],
            projection=['created_at']
        )
        result = list(query.fetch())
        if result:
            result.pop(0)  # remove first one if exists
        for row in result:
            row['created_at'] = datetime.datetime.fromtimestamp(row['created_at']/1000000)
        return result


