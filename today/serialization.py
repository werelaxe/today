from datetime import datetime

from marshmallow import Schema, fields
from marshmallow import post_load


class TodayQuerySchema(Schema):
    date = fields.Date()

    @post_load
    def make_query(self, data):
        return TodayQuery(**data)


class TodayQuery:
    def __init__(self, date=datetime.now().date()):
        self.date = date

    @property
    def params(self):
        return self.__dict__
