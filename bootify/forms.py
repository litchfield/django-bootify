from django.forms import *
from django.forms.forms import Form as BaseForm
from django.forms.models import ModelForm as BaseModelForm
from utils import bootify_widget

class BootMixin(object):
    def __init__(self, *args, **kwargs):
        super(BootMixin, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            before = field.widget
            field.widget = bootify_widget(field.widget)
            #print(name, ':', before, '->', field.widget)

class BootForm(BootMixin, BaseForm):
    pass

class BootModelForm(BootMixin, BaseModelForm):
    pass
