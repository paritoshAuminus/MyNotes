## Configuring media files

- `sttings.py`

```python
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

- Install `pillow`

```bash
pip install pillow
```

- serve media in development (critical, or images won't load)

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # your routes
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

```

> **Note:** `media` and `static` are totally different, so is there configuration, media files are **images, videos** while static files are **html, CSS, javascript**