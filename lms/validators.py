import re

from rest_framework.exceptions import ValidationError


class LinkVideoValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile('youtube\.com')
        tmp_val = dict(value).get(self.field)
        if not bool(reg.match(tmp_val)):
            raise ValidationError('Ссылки допустимы только с youtube.com')

