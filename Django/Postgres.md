# Django + Postgres Deployment (Boilerplate)

## Problem
You want to deploy a Django backend with Postgres on Render, Railway, or Supabase.
The backend must read database credentials from environment variables to remain secure and production-ready.

---

## Solution: Environment Variables + dj-database-url

### 1. Environment Variables

Set these in your Render / Railway / Supabase service:

| Variable | Example / Notes |
|----------|----------------|
| `SECRET_KEY` | `your-random-secret-key` |
| `DEBUG` | `False` |
| `DATABASE_URL` | `postgres://username:password@host:port/dbname` (from your Postgres provider) |
| `ALLOWED_HOSTS` | `your-app-url.vercel.com` or `*` for testing |
| `DJANGO_SETTINGS_MODULE` | `backend.settings` (if needed) |

> ⚠️ Never commit `SECRET_KEY` or `DATABASE_URL` to GitHub.

---

### 2. Install dependencies

```bash
pip install dj-database-url psycopg2-binary
```

---

### 3. Update `settings.py`

```python
import os
import dj_database_url

# SECURITY
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

# DATABASE
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

---

### 4. Root Directory (for monorepo)

If using a monorepo:

```
Blogify/
├── frontend/
└── backend/
```

- Set **Root Directory** = `backend`  
- Ensures build commands run from backend and auto-deploy triggers only on backend changes.

---

### 5. Deployment Commands

#### Build / Install

```bash
pip install -r requirements.txt
```

#### Run migrations

```bash
python manage.py migrate
```

#### Collect static files (optional)

```bash
python manage.py collectstatic --noinput
```

#### Start server

```bash
gunicorn backend_name.wsgi --bind 0.0.0.0:$PORT
```

> Replace `backend_name` with your Django project folder name. `$PORT` is auto-provided by Render/Railway.

---

### 6. Local testing with Postgres

```env
DATABASE_URL=postgres://postgres:password@localhost:5432/blogify_db
```

- Install Postgres locally if needed: `brew install postgresql` (Mac) / `sudo apt install postgresql` (Linux).  

---

### 7. Free Postgres Options

- **Railway:** Persistent free tier, 256–500 MB, auto-generated `DATABASE_URL`.  
- **Supabase:** 500 MB free, persistent forever.  
- Avoid Render Free Postgres — it expires in 30 days.

---

### 8. Optional: Serve frontend via backend

- Build React app: `npm run build`  
- Copy `build/` to `backend/static`  
- Django serves it via `STATIC_URL`  

---

### 9. Notes / Tips

- Run `python manage.py migrate` whenever you add new models.  
- Backup database regularly if using free tiers.  
- Restart server after changing environment variables.  

---

## References

* [https://docs.djangoproject.com/en/4.2/ref/settings/#databases](https://docs.djangoproject.com/en/4.2/ref/settings/#databases)  
* [https://github.com/jacobian/dj-database-url](https://github.com/jacobian/dj-database-url)
