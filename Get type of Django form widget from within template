# Получение типа поля из формы в Django
Удобно когда у нас есть форма из коробки, а нам нужно поправить шаблон.

Для примера - шаблон формы входа.

#### Файл шаблона:
```html
{% extends "base.html" %}
{% load fields_tags %}

                <form method="post" action="">
                    {% csrf_token %}
                    {% for field in form %}
                    <div class="form-group">
                        <input class="form-control" 
                           placeholder="{{ field.label }}" 
                           name="{{ field.name }}" 
                           type="{% if field.field.widget|fieldtype == 'TextInput' %}text{% endif %}
                           {% if field.field.widget|fieldtype == 'PasswordInput' %}password{% endif %}">
                    </div>
                    {% endfor %}
                    <button class="btn btn-success pull-right" type="submit">Войти</button>
                    <input type="hidden" name="text" value="{{ next }}">
                </form>
```

#### Файл шаблонного тегов templatetags/fields_tags.py
```python
from django import template
register = template.Library()

@register.filter('fieldtype')
def fieldtype(field):
    return field.__class__.__name__
```

* Таким образом, мы создали модификатор, который получает имя класс виджета
