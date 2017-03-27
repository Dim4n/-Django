## Как получить имя поля формы в Django ?

forms.py

```python
class LoginForm(forms.Form):
    u"""Форма авторизации"""
    username = forms.CharField(
        label=u'Ваш логин/email',
        widget=forms.TextInput(attrs={
            'placeholder': u'Ведите логин/email',
            'id': 'your-fname',
            'class': 'form-control',
        }),
        required=True,
    )
    password = forms.CharField(
        label=u'Ваш пароль',
        widget=forms.PasswordInput(attrs={
            'placeholder': u'Введите пароль',
            'id': 'your-pwd',
            'class': 'form-control',
        }),
        required=True,
    )
```

```html
<form action="/" method="post">
		{% csrf_token %}
		{% for field in form %}
		<div class="form-group">
		    <label for="{{ field.id_for_label }}" class="control-label">{{ field.label }}<sup>*</sup></label><br>
		    {{ field }}
    </div>
    {% endfor %}
    ...
</form>
```
