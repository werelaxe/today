def remember(func):
    time_cache = {}

    def cached_func(*args):
        cache_value = time_cache.get(args, None)
        if cache_value is not None:
            return cache_value
        value = func(*args)
        time_cache[args] = value
        return value
    return cached_func
