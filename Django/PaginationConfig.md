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



