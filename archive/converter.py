import string

from flask import Flask
from werkzeug.routing import BaseConverter


class ShortIntConverter(BaseConverter):
    regex = r"\d+|-[0-9a-zA-Z]+"

    _num2alpha = []
    _alpha2num = {}

    @classmethod
    def init(cls):
        for i in range(10):
            cls._add_chr(str(i))
        for char in string.ascii_letters:
            cls._add_chr(char)

    @classmethod
    def _add_chr(cls, char):
        index = len(cls._num2alpha)
        cls._num2alpha.append(char)
        cls._alpha2num[char] = index

    @classmethod
    def num2alpha(cls, number):
        base = len(cls._num2alpha)
        alpha = []
        while number > 0:
            number, r = divmod(number, base)
            alpha.append(cls._num2alpha[r])
        alpha.reverse()
        return "".join(alpha)

    @classmethod
    def alpha2num(cls, alpha):
        num = 0
        base = len(cls._num2alpha)
        for char in alpha:
            num = num*base+cls._alpha2num[char]
        return num

    def to_url(self, value):
        if isinstance(value, int):
            value = '-'+self.num2alpha(value)
        return value

    def to_python(self, value):
        if value.startswith('-'):
            value = self.alpha2num(value[1:])
        else:
            value = int(value)
        return value


def init(app: Flask):
    ShortIntConverter.init()
    app.url_map.converters['short'] = ShortIntConverter


