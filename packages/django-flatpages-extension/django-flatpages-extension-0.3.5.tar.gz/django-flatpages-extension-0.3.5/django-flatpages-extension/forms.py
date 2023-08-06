from django import forms
from django.contrib.flatpages.forms import FlatpageForm
from .models import FlatPageExtended


TextField = forms.fields.TextInput


try:
    from ckeditor.fields import RichTextFormField
    TextField = RichTextFormField
except ImportError:
    pass


class FlatpageExtendedForm(FlatpageForm, forms.ModelForm):
    content = TextField()

    class Meta:
        model = FlatPageExtended
        fields = '__all__'
