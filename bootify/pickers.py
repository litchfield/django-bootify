from django import forms
from django.utils.safestring import mark_safe

DATE_HTML = """<div class="bootify-datepicker">%s</div>"""

TIME_HTML = """
<div class="bootify-timepicker">
    <div class="input-group bootstrap-timepicker">
        %s
        <span class="input-group-addon"><i class="icon-time"></i></span>
    </div>
</div>
"""

class BootstrapDateInput(forms.DateInput):
    def render(self, name, value, attrs=None):
        a = {
            'class': '%s form-control datepicker-default' % attrs.get('class', ''),
            'placeholder': 'dd/mm/yyyy',
        }
        a.update(attrs)
        input_html = super(BootstrapDateInput, self).render(name, value, a)
        return mark_safe(DATE_HTML % input_html)

class BootstrapTimeInput(forms.TimeInput):
    def render(self, name, value, attrs=None):
        a = {'class': '%s form-control timepicker-default' % attrs.get('class', '')}
        a.update(attrs)
        input_html = super(BootstrapTimeInput, self).render(name, value, a)
        return mark_safe(TIME_HTML % input_html)

class BootstrapSplitDateTimeWidget(forms.SplitDateTimeWidget):
    def __init__(self, date_format=None, time_format=None, attrs=None):
        widgets = [
            BootstrapDateInput(format=date_format),
            BootstrapTimeInput(format=time_format),
        ]
        forms.MultiWidget.__init__(self, widgets, attrs)

class BootstrapSplitDateTimeField(forms.SplitDateTimeField):
    widget = BootstrapSplitDateTimeWidget


