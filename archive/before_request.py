import datetime

from flask import Flask


def init(app: Flask):

    @app.template_filter("dtform")
    def dtform(s):
        if isinstance(s, datetime.datetime):
            return f"{s.year}년 {s.month}월 {s.day}일 {s.hour}시 {s.month}분"
        return s


