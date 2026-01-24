## Django restframework permission configurations

- Install dependencies

```bash
pip install djangorestframework djangorestframework-simplejwt
```

- `settings.py`

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]

```

- REST Framework config (JWT + permissions)

```python
REST_FRAMEWORK = {
    # Authentication = WHO the user is
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),

    # Permissions = WHAT the user can do
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
}
```

- Simple JWT config (token lifespan)

```python
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}
```

- URLs in `urls.py`

```python
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

```