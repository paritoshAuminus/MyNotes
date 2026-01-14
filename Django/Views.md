# Django Views – Complete Industry Cheatsheet

This document covers **ALL view types used in real Django projects**, including **Django core** and **Django REST Framework (DRF)**.

---

## What Is a View?

A **view** is the layer that:

* Receives an HTTP request
* Executes business logic
* Returns an HTTP response

**Flow**
Request → URLconf → View → Response

A response can be:

* HTML
* JSON
* Redirect
* Error (404, 403, etc.)

---

# DJANGO CORE VIEWS

---

## 1. Function-Based Views (FBVs)

### What they are

Plain Python functions that take `request` and return a response.

### Example: Basic FBV

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Django")
```

### Example: Handling methods manually

```python
def my_view(request):
    if request.method == "GET":
        return HttpResponse("GET")
    elif request.method == "POST":
        return HttpResponse("POST")
```

### Example: Render template

```python
from django.shortcuts import render

def page(request):
    return render(request, "page.html", {"name": "Django"})
```

### Example: Redirect

```python
from django.shortcuts import redirect

def go_home(request):
    return redirect("home")
```

### Used when

* Simple logic
* Full control needed
* Small apps or utilities

---

## 2. Class-Based Views (CBVs)

### What they are

Views written as classes using OOP.
Each HTTP method maps to a method (`get`, `post`, etc.).

### Example: Basic CBV

```python
from django.views import View
from django.http import HttpResponse

class HomeView(View):
    def get(self, request):
        return HttpResponse("Hello Django")
```

### Example: GET + POST

```python
class FormView(View):
    def get(self, request):
        return HttpResponse("Form")

    def post(self, request):
        return HttpResponse("Submitted")
```

### Why CBVs

* Cleaner structure
* Reusable via inheritance
* Scales better than FBVs

---

## 3. Generic Class-Based Views (CRUD Backbone)

Used in **almost every production Django app**.

---

### ListView – list objects

```python
from django.views.generic import ListView
from .models import Article

class ArticleListView(ListView):
    model = Article
```

---

### DetailView – single object

```python
from django.views.generic import DetailView

class ArticleDetailView(DetailView):
    model = Article
```

---

### CreateView – create object

```python
from django.views.generic import CreateView

class ArticleCreateView(CreateView):
    model = Article
    fields = ["title", "content"]
```

---

### UpdateView – update object

```python
from django.views.generic import UpdateView

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ["title", "content"]
```

---

### DeleteView – delete object

```python
from django.views.generic import DeleteView
from django.urls import reverse_lazy

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("article_list")
```

---

## 4. TemplateView (Static Pages)

### Used for static or near-static pages

```python
from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "about.html"
```

---

## 5. RedirectView

### Used for URL redirects

```python
from django.views.generic import RedirectView

class OldPageRedirect(RedirectView):
    url = "/new-page/"
```

---

# DJANGO REST FRAMEWORK (INDUSTRY STANDARD FOR APIs)

---

## What DRF Views Do

They return:

* JSON
* HTTP status codes
* Serialized data

Used for:

* Mobile apps
* Frontend frameworks (React, Vue)
* Public APIs

---

## 6. APIView (Low-level DRF view)

### Most basic DRF view

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    def get(self, request):
        return Response({"message": "Hello API"})
```

### Used when

* Full control needed
* Custom API logic

---

## 7. GenericAPIView

### Adds queryset + serializer support

```python
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer

class ArticleAPIView(GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)
```

---

## 8. Concrete Generic API Views (MOST USED)

These map directly to CRUD.

---

### ListAPIView

```python
from rest_framework.generics import ListAPIView

class ArticleListAPI(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

---

### RetrieveAPIView

```python
from rest_framework.generics import RetrieveAPIView

class ArticleDetailAPI(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

---

### CreateAPIView

```python
from rest_framework.generics import CreateAPIView

class ArticleCreateAPI(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

---

### UpdateAPIView

```python
from rest_framework.generics import UpdateAPIView

class ArticleUpdateAPI(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

---

### DestroyAPIView

```python
from rest_framework.generics import DestroyAPIView

class ArticleDeleteAPI(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

---

## 9. ViewSets (MOST COMMON IN INDUSTRY)

### Combines all CRUD into ONE class

```python
from rest_framework.viewsets import ModelViewSet

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

Used with routers → clean URLs, less code.

---

## 10. Function-Based API Views (DRF)

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def hello_api(request):
    return Response({"message": "Hello"})
```

---

# URL MAPPING (DON’T SCREW THIS UP)

---

### FBV

```python
path("", home)
```

### CBV

```python
path("", HomeView.as_view())
```

### DRF ViewSet

```python
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("articles", ArticleViewSet)
```

---

# FINAL MENTAL MODEL (INDUSTRY REALITY)

FBV

* Simple
* Explicit
* Rare in large systems

CBV

* Structured
* Reusable
* Default for Django apps

Generic CBV

* CRUD backbone
* Used everywhere

APIView

* Custom APIs

GenericAPIView

* Mid-level control

ViewSet

* **Most common in production APIs**

---

# RULES YOU SHOULD REMEMBER

* Web pages → Django CBVs
* CRUD → Generic CBVs
* APIs → DRF ViewSets
* Custom API logic → APIView
* Large projects → avoid FBVs

---