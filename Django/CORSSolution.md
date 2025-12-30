Perfect — this is a great thing to keep boilerplate for.
Below is a **clean, copy-pasteable Markdown note** you can drop straight into your notes repo.

---

````md
# Django REST Framework – CORS Setup (Boilerplate)

## Problem
When a frontend (e.g. Vite on `http://localhost:5173`) calls a Django REST API
(e.g. `http://127.0.0.1:8000`), the browser may block the request with a CORS error:

> No 'Access-Control-Allow-Origin' header is present on the requested resource

CORS **must be configured on the backend**, not the frontend.

---

## Solution: django-cors-headers

### 1. Install dependency
```bash
pip install django-cors-headers
````

---

### 2. Add to `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    ...
    "corsheaders",
    "rest_framework",
]
```

---

### 3. Add middleware (ORDER MATTERS)

`CorsMiddleware` should be as high as possible, especially before
`CommonMiddleware`.

```python
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    ...
]
```

---

### 4. Allow frontend origins

Explicit is better than wildcard.

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
```

---

### 5. If using authentication (cookies / Authorization headers)

```python
CORS_ALLOW_CREDENTIALS = True
```

---

### 6. Allow common headers (usually not required, but safe)

```python
from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = list(default_headers) + [
    "authorization",
]
```

---

### 7. Development-only shortcut (⚠️ NOT for production)

```python
CORS_ALLOW_ALL_ORIGINS = True
```

Use this **only** during early development.

---

## Common Gotchas

### `localhost` ≠ `127.0.0.1`

These are treated as **different origins** by the browser.

✔ Allowed:

* `http://localhost:5173`
* `http://127.0.0.1:5173`

❌ Not interchangeable

---

### Preflight (OPTIONS) requests

Requests with:

* `POST`, `PUT`, `DELETE`
* `Authorization` header
* `Content-Type: application/json`

trigger a **preflight OPTIONS request**.

If CORS isn’t configured correctly, Django will reject the request **before**
your view is hit.

---

## Minimal Working Example

```python
# settings.py

INSTALLED_APPS = [
    "corsheaders",
    "rest_framework",
    ...
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]

CORS_ALLOW_CREDENTIALS = True
```

---

## Debug Tips

* Restart the Django server after changes
* Check the Network tab → OPTIONS request
* Look for `Access-Control-Allow-Origin` in response headers
* If missing → CORS config is wrong or middleware order is incorrect

---

## References

* [https://github.com/adamchainz/django-cors-headers](https://github.com/adamchainz/django-cors-headers)

```
