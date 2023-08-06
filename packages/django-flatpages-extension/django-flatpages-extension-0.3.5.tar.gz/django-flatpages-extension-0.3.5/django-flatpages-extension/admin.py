from django.contrib import admin
from .forms import FlatpageExtendedForm
from .models import FlatPageExtended
from django.contrib.flatpages.admin import FlatPageAdmin


FlatPageAdmin.fieldsets[0][1]['fields'] = (
    'url', 'meta_title', 'meta_keywords', 'meta_description',
    'title', 'content', 'sites'
)


@admin.register(FlatPageExtended)
class FlatPageAdminExtended(FlatPageAdmin):
    form = FlatpageExtendedForm