from random import choice

import requests

from html.parser import HTMLParser
from today.cache_wrapper import remember

BASE_URL = "http://kakoysegodnyaprazdnik.ru/baza"

MONTH_LABELS = {
    1: 'yanvar',
    2: 'fevral',
    3: 'mart',
    4: 'aprel',
    5: 'may',
    6: 'iyun',
    7: 'iyul',
    8: 'avgust',
    9: 'sentyabr',
    10: 'oktyabr',
    11: 'noyabr',
    12: 'dekabr',
}


@remember
def get_today(date):
    return choice(get_celebrates(date)).lower()


class TodayParser(HTMLParser):
    def error(self, message):
        pass

    def __init__(self):
        super().__init__()
        self.collect = False
        self.collected_data = []

    def handle_starttag(self, tag, attrs):
        if tag == 'span':
            if attrs == [('itemprop', 'text')]:
                self.collect = True

    def handle_endtag(self, tag):
        if tag == 'span':
            self.collect = False

    def handle_data(self, data):
        if self.collect:
            self.collected_data.append(data)

    @property
    def today_celebrates(self):
        for index in range(len(self.collected_data)):
            if self.collected_data[index].startswith("Именины"):
                return self.collected_data[:index]
        return self.collected_data


def make_url(base_url, date):
    month = MONTH_LABELS[date.month]
    return "{base_url}/{month}/{day}".format(
        base_url=base_url,
        month=month,
        day=date.day,
    )


def get_celebrates(date):
    content = requests.get(make_url(BASE_URL, date)).content.decode()
    parser = TodayParser()
    parser.feed(content)
    return parser.today_celebrates
