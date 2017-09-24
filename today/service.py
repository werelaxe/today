from random import choice

import requests

from html.parser import HTMLParser
from today.cache_wrapper import remember


URL = "http://kakoysegodnyaprazdnik.ru/"


@remember
def get_today():
    return choice(get_celebrates()).lower()


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


def get_celebrates():
    content = requests.get(URL).content.decode()
    parser = TodayParser()
    parser.feed(content)
    return parser.today_celebrates
