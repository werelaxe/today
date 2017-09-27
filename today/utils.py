import datetime
import pytz


TIMEZONE_DIFF = datetime.datetime.now(pytz.timezone('Asia/Yekaterinburg')).utcoffset().total_seconds() // 60 // 60
TIME_DIFF = datetime.timedelta(0, 3600 * TIMEZONE_DIFF)


def get_current_time():
    return datetime.datetime.now() + TIME_DIFF


def remember(func):
    cache = {}

    def cached_func(*args):
        cache_value = cache.get(args, None)
        if cache_value is not None:
            return cache_value
        value = func(*args)
        cache[args] = value
        return value
    return cached_func
