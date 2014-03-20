from django import template
from bootify.utils import bootify_widget
register = template.Library()

@register.filter
def boot(field):
    field.field.widget = bootify_widget(field.field.widget)
    return field

@register.filter
def boot_inline(field):
    field.field.widget = bootify_widget(field.field.widget, inline=True)
    return field

@register.filter
def boot_disabled(self):
    field.field.widget = bootify_widget(field.field.widget, disabled=True)
    return field

@register.filter
def placeholder(field, label):
    try:
        field.field.widget.attrs['placeholder'] = label
    except:
        pass
    return field

@register.filter
def required(field):
    try:
        field.field.widget.attrs['required'] = 'required'
    except:
        pass
    return field    