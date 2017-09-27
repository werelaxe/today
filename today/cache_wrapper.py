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
