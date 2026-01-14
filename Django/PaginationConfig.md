# Django Pagination Config

## Using paginator in standard django views

### Step 1 - Import and initialize `Paginator`

```python
from django.core.paginator import Paginator
from django.shortcuts import render
from myapp.models import Contact
def contact_list(request):
   contacts = Contact.objects.all()
   paginator = Paginator(contacts, 10) # 10 items per page
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)
   return render(request, 'contacts.html', {'page_obj': page_obj})
```

## Using pagination with DRF

### Step 1 - Add global configuration to the settings.py

```python
REST_FRAMEWORK = {
'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
'PAGE_SIZE': 10
}
```

### Step 2 - Apply Pagination to a view

```python
from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer
class ContactListView(generics.ListAPIView):
   queryset = Contact.objects.all()
   serializer_class = ContactSerializer
```

- This automatically paginates results with count, next, previous, and results keys in the API response.

Perfect — then let’s make this a **proper blueprint-level DRF pagination cheat sheet** that you can **copy-paste directly into real projects**.
This will be **complete, structured, and configuration-ready**, not just conceptual.

---

# 📌 Django & DRF Pagination — **Blueprint Cheat Sheet**

---

## 0️⃣ Core Rule (VERY IMPORTANT)

> **Pagination ALWAYS works on a QuerySet, never on a Model class**

```python
queryset = Blog.objects.all()   # ✅
queryset = Blog                # ❌
```

---

## 1️⃣ Django Core Pagination (NOT DRF)

### Django `Paginator`

```python
from django.core.paginator import Paginator
```

**Purpose**

* Core Django utility
* Used for templates or manual APIs

**Usage**

```python
paginator = Paginator(queryset, per_page)
page_obj = paginator.get_page(page_number)
```

**Limitations**

* No API-friendly response
* No settings integration
* Manual JSON required

---

## 2️⃣ DRF Pagination (HIGH LEVEL)

**What DRF does**

* Wraps Django Paginator
* Adds standardized API responses
* Integrates with serializers & viewsets

**Global Configuration**

```python
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "...",
    "PAGE_SIZE": 10,
}
```

---

## 3️⃣ DRF Pagination Classes (DETAILED)

---

## 🔹 1. PageNumberPagination

### Description

* Uses **page numbers**
* Most common & beginner-friendly

### Request

```
GET /api/blogs/?page=2
```

### Default Response

```json
{
  "count": 100,
  "next": "http://api/blogs/?page=3",
  "previous": "http://api/blogs/?page=1",
  "results": [...]
}
```

---

### Global Configuration (COPY-PASTE)

```python
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS":
        "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}
```

---

### Custom PageNumber Pagination

```python
from rest_framework.pagination import PageNumberPagination

class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100
```

```python
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS":
        "myapp.pagination.StandardPagination"
}
```

---

### Best Use Cases

* Admin panels
* CRUD APIs
* Small–medium datasets

---

## 🔹 2. LimitOffsetPagination

### Description

* Uses **limit** + **offset**
* Offset = number of records to skip

### Request

```
GET /api/blogs/?limit=10&offset=20
```

### Default Response

```json
{
  "count": 100,
  "next": "...?limit=10&offset=30",
  "previous": "...?limit=10&offset=10",
  "results": [...]
}
```

---

### Global Configuration (COPY-PASTE)

```python
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS":
        "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
}
```

---

### Custom LimitOffset Pagination

```python
from rest_framework.pagination import LimitOffsetPagination

class LimitPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100
```

---

### Best Use Cases

* Infinite scrolling
* Mobile apps
* Feeds

### Drawbacks

* Slow on very large offsets
* Inconsistent if data changes

---

## 🔹 3. CursorPagination (ADVANCED)

### Description

* Uses an **encoded cursor**
* No page numbers or offsets
* Requires deterministic ordering

---

### Request

```
GET /api/blogs/?cursor=cD0yMDIzLTEy...
```

---

### Response

```json
{
  "next": "...?cursor=abc123",
  "previous": null,
  "results": [...]
}
```

---

### Custom Cursor Pagination (REQUIRED)

```python
from rest_framework.pagination import CursorPagination

class CursorBasedPagination(CursorPagination):
    page_size = 10
    ordering = "-created_at"
```

---

### Apply to View

```python
class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = CursorBasedPagination
```

---

### Best Use Cases

* Large datasets
* High-traffic APIs
* Real-time feeds

### Limitations

* Cannot jump to page numbers
* Requires stable ordering field

---

## 🔹 4. Disable Pagination (Per View)

```python
class BlogViewSet(ModelViewSet):
    pagination_class = None
```

---

## 4️⃣ Pagination Scope

### Global (settings.py)

```python
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "...",
    "PAGE_SIZE": 10,
}
```

### Per View / ViewSet

```python
pagination_class = CustomPagination
```

---

## 5️⃣ Performance & Best Practices

* Use `.count()` instead of `len()`
* Always order querysets explicitly
* Cursor pagination scales best
* Avoid offset pagination for huge tables

---

## 6️⃣ Common Errors ❌

| Error                    | Cause                           |
| ------------------------ | ------------------------------- |
| `ModelBase has no len()` | Using model instead of queryset |
| No pagination applied    | Missing pagination class        |
| Cursor error             | No ordering field               |

---

## 7️⃣ Recommendation Matrix

| Use Case        | Pagination Type  |
| --------------- | ---------------- |
| CRUD APIs       | PageNumber       |
| Infinite scroll | LimitOffset      |
| Large datasets  | Cursor           |
| HTML pages      | Django Paginator |

---

## 8️⃣ One-Line Rule to Remember 🧠

> **HTML → Django Paginator**
> **APIs → DRF Pagination**
> **Big Data → CursorPagination**

---


