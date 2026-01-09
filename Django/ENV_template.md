# Django Blog Backend – Render Deployment (.env Template)

Use this environment file to configure your Django backend with Render Postgres.

---

### **1. Secret Key**
```env
# Django secret key (keep this private!)
SECRET_KEY=django-insecure-3yf4=kj&ln3v0$_(&y-$8pv6k8*%g^i^_8x@t&_s1$=%7iu=ss
```

---

### **2. Debug Mode**
```env
# Set to False in production
DEBUG=False
```

---

### **3. Allowed Hosts**
```env
# Either '*' for testing or your Render service URL
ALLOWED_HOSTS=*
```

---

### **4. Postgres Database**
```env
# Full External Database URL from Render
DATABASE_URL=postgres://blogify_db_5837_user:YOUR_PASSWORD_HERE@dpg-d5eaqs95pdvs73f8qc6g-a:5432/blogify_db_5837
```

> ⚠️ Replace `YOUR_PASSWORD_HERE` with the password shown in Render.  
> ✅ No separate PASSWORD variable is needed — it’s included in the URL.

---

### **Notes / Tips**
- Do **not** commit this file to GitHub — add `.env` to `.gitignore`.  
- Make sure `settings.py` reads these variables using `os.environ` and `dj_database_url`:

``
