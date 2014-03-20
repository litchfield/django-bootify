from django.forms.widgets import *
from django.forms.widgets import ChoiceInput, RadioChoiceInput, CheckboxChoiceInput, ChoiceFieldRenderer
from django.utils.encoding import force_text
from django.utils.html import format_html, format_html_join
from django.utils.safestring import mark_safe

CSS = set(['radio', 'checkbox'])
CSS_INLINE = set(['radio-inline', 'checkbox-inline'])

class _ChoiceInputMixin(object):
    def render(self, name=None, value=None, attrs=None, choices=()):
        from utils import get_css
        if 'id' in self.attrs:
            label_extra = format_html(' for="{0}_{1}"', self.attrs['id'], self.index)
        else:
            label_extra = ''
        css = get_css(self.attrs)
        if css & CSS_INLINE:
            label_extra += format_html(' class="{0}"', ' '.join(css))
            self.attrs['class'] = ' '.join(css - CSS_INLINE)
        if css & CSS:
            self.attrs['class'] = ' '.join(css - CSS)
        if self.attrs['class'] == '':
            del self.attrs['class']
        html = format_html('<label{0}>{1} {2}</label>', label_extra, self.tag(), self.choice_label)
        if css & CSS:
            html = format_html('<div class="{0}">{1}</div>', ' '.join(css), html)
        return html

class _RadioChoiceInput(_ChoiceInputMixin, RadioChoiceInput):
    pass

class _CheckboxChoiceInput(_ChoiceInputMixin, CheckboxChoiceInput):
    pass

class _ChoiceFieldRenderer(ChoiceFieldRenderer):
    def render(self):
        return mark_safe('\n'.join([ force_text(widget) for widget in self ]))

class BootRadioFieldRenderer(_ChoiceFieldRenderer):
    choice_input_class = _RadioChoiceInput

class BootCheckboxFieldRenderer(_ChoiceFieldRenderer):
    choice_input_class = _CheckboxChoiceInput

class BootRadioSelect(RadioSelect):
    renderer = BootRadioFieldRenderer
    base_css = 'radio'

    def __init__(self, attrs=None, choices=(), inline=False):
        from utils import set_css
        css = self.base_css
        if inline:
            css += '-inline'
        #print css, inline
        attrs = attrs or {}
        set_css(attrs, css)
        super(BootRadioSelect, self).__init__(attrs, choices)

class BootCheckboxSelectMultiple(CheckboxSelectMultiple):
    renderer = BootCheckboxFieldRenderer
    base_css = 'checkbox'

    def __init__(self, attrs=None, choices=(), inline=False):
        from utils import set_css
        css = self.base_css
        if inline:
            css += '-inline'
        set_css(attrs, css)
        super(BootCheckboxSelectMultiple, self).__init__(attrs, choices)
