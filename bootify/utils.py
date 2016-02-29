from django.forms.widgets import *
from .widgets import *


CSS = set(['radio', 'checkbox'])
CSS_INLINE = set(['radio-inline', 'checkbox-inline'])

FORM_CONTROLS_WIDGETS = [
    TextInput,
    PasswordInput,
    #HiddenInput,
    #DateInput,
    #DateTimeInput,
    #TimeInput,
    Textarea,
    #CheckboxInput,
    Select,
    NullBooleanSelect,
    SelectMultiple,
    #RadioSelect,
    #CheckboxSelectMultiple,
    FileInput,
    ClearableFileInput,
    MultipleHiddenInput,
    #SplitDateTimeWidget,
    #SplitHiddenDateTimeWidget,
    #SelectDateWidget,
]

try:
    FORM_CONTROLS_WIDGETS += [
        NumberInput,
        EmailInput,
        URLInput,
    ]
except NameError:
    # Requires Django 1.6+
    pass

FORM_CONTROLS_WIDGETS = tuple(FORM_CONTROLS_WIDGETS)

try:
    from django.forms.widgets import ChoiceInput
    CLASS_MAP = {
        RadioSelect: BootRadioSelect,
        CheckboxSelectMultiple: BootCheckboxSelectMultiple,
        #BootRadioSelect: BootRadioSelect,
        #BootCheckboxSelectMultiple: BootCheckboxSelectMultiple,
    }
except ImportError:
    # Requires Django 1.6+
    CLASS_MAP = {}

def bootify_widget(widget, inline=False, disabled=False):
    if type(widget) in (BootCheckboxSelectMultiple, BootRadioSelect):
        # already bootified
        return widget
    if type(widget) in CLASS_MAP:
        widget = CLASS_MAP[type(widget)](attrs=widget.attrs, choices=widget.choices, inline=inline)
    elif isinstance(widget, FORM_CONTROLS_WIDGETS):
        set_css(widget.attrs, 'form-control')
    return widget

def get_css(attrs):
    return set(attrs.get('class', '').split(' '))

def set_css(attrs, extra_css=None):
    css = get_css(attrs) - CSS - CSS_INLINE
    if extra_css:
        css.add(extra_css)
    attrs['class'] = ' '.join(css)
    return attrs
