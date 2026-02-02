```python
# Caching configuration
CACHES = {
    'default': {
        # local memory cache (fastest, can't persist) - stored in RAM
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-blog-cache',
    }
}
```

- In the views use, `@method_decorator()` with `cache_page(60 * 60)`