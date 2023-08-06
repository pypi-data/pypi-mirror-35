from django.contrib.flatpages.models import FlatPage
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

TextField = models.TextField


try:
    from ckeditor.fields import RichTextField

    TextField = RichTextField
except ImportError:
    pass


class FlatPageExtended(FlatPage):
    meta_title = models.CharField(_("Title"), max_length=500, blank=True, null=True)
    meta_keywords = models.CharField(
        _("Keywords"), max_length=500, blank=True, null=True
    )
    meta_description = models.TextField(_("Description"), blank=True, null=True)

    def save(self, *args, **kwargs):
        self.url = "/{}/".format(slugify(self.title, allow_unicode=True))
        return super().save(*args, **kwargs)
