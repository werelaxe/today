from marshmallow import Schema, fields
from marshmallow import post_load

from today.utils import get_current_time


class TodayQuerySchema(Schema):
    date = fields.Date()

    @post_load
    def make_query(self, data):
        return TodayQuery(**data)


class TodayQuery:
    def __init__(self, date=None):
        if date is None:
            date = get_current_time().date()
        self.date = date

    @property
    def params(self):
        return self.__dict__
