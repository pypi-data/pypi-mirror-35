import re
import requests
import redis

from cachecontrol import CacheControlAdapter
from cachecontrol.heuristics import ExpiresAfter
from cachecontrol.caches.redis_cache import RedisCache

from django.conf import settings


def get_cache_requests(url):
    # Check settings
    if not hasattr(settings, 'EXTERNAL_CACHE'):
        return None
    external_cache = settings.EXTERNAL_CACHE
    redis_url = external_cache.get('redis')
    pattern = external_cache.get('pattern')
    minutes = external_cache.get('minutes')
    if (redis_url or pattern or minutes) is None:
        return None
    # Check if redis is connected
    r = redis.from_url(redis_url)
    try:
        r.info()
    except redis.ConnectionError:
        return None  # No cache connection, cannot use cache
    session = requests.session()
    # Check if url path matches (RegEx: https://regexr.com/)
    match = re.search(r'%s' % pattern, url)
    if match is None:
        return None
    # Everything is connected and matches, can use cached request
    adapter = CacheControlAdapter(heuristic=ExpiresAfter(minutes=int(minutes)), cache=RedisCache(r))
    session.mount('https://', adapter)
    session.mount('http://', adapter)
    return session


# HTTP Get Request
def get(url, **kwargs):
    req = get_cache_requests(url)  # Use cache if available
    if req is not None:
        return req.get(url, **kwargs)
    return requests.get(url, **kwargs)


# HTTP Post Request
def post(url, **kwargs):
    return requests.post(url, **kwargs)


# HTTP Put Request
def put(url, **kwargs):
    return requests.put(url, **kwargs)


# HTTP Delete Request
def delete(url, **kwargs):
    return requests.delete(url, **kwargs)
