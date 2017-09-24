from datetime import datetime


def remember(func):
    time_cache = {}

    def cached_func():
        current_date = datetime.now().date()
        cache_value = time_cache.get(current_date, None)
        if cache_value is not None:
            return cache_value
        value = func()
        time_cache[current_date] = value
        return value
    return cached_func
