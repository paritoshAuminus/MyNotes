# Django Blog Backend – Quick Deploy Cheat Sheet

## Environment Variables (.env)
```env
SECRET_KEY=django-insecure-<your-random-key>
DEBUG=False
ALLOWED_HOSTS=*
DATABASE_URL=postgres://blogify_db_5837_user:<your-password>@dpg-d5eaqs95pdvs73f8qc6g-a:5432/blogify_db_5837
```

## Commands (Run in backend root directory)
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn backend.wsgi --bind 0.0.0.0:$PORT
```

## Notes
- Set **Root Directory = backend** if monorepo  
- `.env` should never be committed to GitHub  
- For local testing, replace DATABASE_URL with local Postgres
