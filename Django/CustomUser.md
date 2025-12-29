## Creating Custom user by extending Django's internal user

- Custom user model

```python
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return self.username
```

- `settings.py`

```python
...
AUTH_USER_MODEL = 'accounts.User'
```

> **Note:** Make sure **not** to name the app or model as **`auth`** which is the actual name of django's internal user.

### A helpful diagram

```
REQUEST
  |
  |  Authorization: Bearer token
  v
JWTAuthentication
  |
  |  token valid?
  v
request.user  ✅
request.auth  ✅
  |
  v
YOUR VIEW RUNS
```