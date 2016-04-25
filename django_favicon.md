Как вставить favicon.ico в django-проект?

**urls.py**

```python
urlpatterns = [
    ...
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
    ...
]
```
