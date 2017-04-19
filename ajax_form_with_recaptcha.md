Ajax форма с рекапчей

```
pip install django-recaptcha2
```

Добавим в INSTALL APPS

```python
INSTALLED_APPS = (
    ...
    'snowpenguin.django.recaptcha2',
    ...
)
```

Зарегаем ключи на гугле

```python
RECAPTCHA_PRIVATE_KEY = 'your private key'
RECAPTCHA_PUBLIC_KEY = 'your public key'
```

Форма (на примере заказа звонка):

forms.py

```python
from django import forms

# from captcha.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

from apps.generic.models import PhoneCallItem, QuestionItem


class PhoneCallForm(forms.ModelForm):
    fio = forms.CharField(
        label=u'ФИО',
        widget=forms.TextInput(attrs={
            'placeholder': u'ФИО',
        }),
        required=True,
    )
    phone = forms.CharField(
        label=u'Телефон',
        widget=forms.TextInput(attrs={
            'placeholder': u'Телефон',
        }),
        required=True,
    )
    captcha = ReCaptchaField(
        label=u'Я не робот',
        widget=ReCaptchaWidget()
    )

    class Meta:
        model = PhoneCallItem
        fields = [
            'fio', 'phone',
        ]
```



index.html

```html
{% load recaptcha2 %}

<head>
{% recaptcha_explicit_support %}
</head>


<!-- Modal sale-->
<div class="modal fade" id="phoneModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header text-center">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title" id="myModalLabel">Задать вопрос:</h4>
      </div>
      <form action="/query_question/">{% csrf_token %}
        <div class="modal-body text-center">
          {% for field in form_phoneform %}
            {{ field }}
          {% endfor %}
          <div class="recap">
            <div id='recaptcha1'></div>
            <script>
                django_recaptcha_callbacks.push(function() {
                    grecaptcha.render('recaptcha1', { // id меняем если форм много
                        'sitekey': '{{ public_key }}'
                    })
                });
            </script>
          </div>
        </div>
        <div class="modal-footer">
          <p class="warn" id="warn1" style="display:none;"></p>
          <button type="button" id="button1" class="btn send center-block">Задать вопрос</button>
        </div>
      </form>
    </div>
  </div>
</div>

{% recaptcha_explicit_init %}

<script>
(function($){
    $(document).ready(function(){
        $('#button1').click(function(){
            var url = $(this).closest('form').attr('action');
            $.post( url, {
                    'csrfmiddlewaretoken': $(this).closest('form').find('input[name=csrfmiddlewaretoken]').val(),
                    'fio': $(this).closest('form').find('input[name=fio]').val(),
                    'phone': $(this).closest('form').find('input[name=phone]').val(),
                    'g-recaptcha-response': $(this).closest('form').find('textarea[name=g-recaptcha-response]').val(),
                }
            ).done(function( data ) {
                $('#warn1').html('');
                $('#warn1').css('display', 'none');
                if( data['status'] == true ) {
                    $('#warn1').css('display', 'block');
                    $('#warn1').html('Ваше сообщение отправлено!');
                    setInterval( function(){
                       $('#phoneModal').modal('hide');
                    }, 1000);
                }
                else {
                    var html = '';
                    for (x in data['errors']) {
                        html += data['errors'][x] + '<br>';
                    }
                    $('#warn1').html(html);
                    $('#warn1').css('display', 'block');
                }
            });
        });
    });
})(jQuery);
</script>
```

urls:

```python
urlpatterns = [
...
url(r'^query_phonecall/', QueryPhoneCall.as_view(), name='query-phonecall'),
...
]
```

views.py

```python
def get_field_name(f, form):
    field = form.fields[f]
    return field.label


class QueryPhoneCall(CreateView):
    template_name = ''
    form_class = PhoneCallForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(QueryPhoneCall, self).dispatch(request, *args, **kwargs)

    def form_invalid(self, form):
        if self.request.is_ajax():
            #print self.request
            #print form
            to_json_response = dict()
            to_json_response['status'] = False
            to_json_response['errors'] = [u'Поле "%s" необходимо заполнить!' % get_field_name(field_name, form) for
                                          field_name in form.errors]


            return HttpResponse(json.dumps(to_json_response), content_type='application/json')
        else:
            print(1)

    def form_valid(self, form):
        if self.request.is_ajax():

            # type_action = self.request.POST.get('type_action', '') or '0';

            # template = 'feedback/callback_query_template.html' \
            #     if type_action == '1' else 'feedback/send_query_template.html';

            # now = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")
            # message = EmailMessage(
            #     'feedback/mail_template.html',
            #     {
            #         'mail': {
            #             'now': now,
            #             'type': type_action,
            #             'name': self.request.POST.get('name', ''),
            #             'phone': self.request.POST.get('phone', ''),
            #             'email': self.request.POST.get('email', ''),
            #             'message': self.request.POST.get('message', ''),
            #         }
            #     },
            #     local.DEFAULT_FROM_EMAIL,
            #     to=[local.EMAIL_TO, local.EMAIL_TO_CC]
            # )

            to_json_response = dict()
            # to_json_response['new_cptch_key'] = CaptchaStore.generate_key()
            # to_json_response['new_cptch_image'] = captcha_image_url(to_json_response['new_cptch_key'])

            # if message.send():
            to_json_response['status'] = True
            to_json_response['result'] = u'Сообщение отправлено'

            # else:
            #     to_json_response['status'] = False
            #     to_json_response['result'] = u'К сожалению, заказ не отправлен из-за технических проблем на сервере.'

            return HttpResponse(json.dumps(to_json_response), content_type='application/json')
        else:
            print(2)
```
