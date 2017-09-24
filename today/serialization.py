from marshmallow import Schema, fields
from marshmallow import post_load


class TodayQuerySchema(Schema):
    usual = fields.Boolean()
    raw = fields.Boolean()
    congrat = fields.Boolean()

    @post_load
    def make_query(self, data):
        return TodayQuery(**data)


class TodayQuery:
    def __init__(self, usual=True, raw=False, congrat=False):
        self.usual = usual
        self.raw = raw
        self.congrat = congrat

    @property
    def params(self):
        return self.__dict__
