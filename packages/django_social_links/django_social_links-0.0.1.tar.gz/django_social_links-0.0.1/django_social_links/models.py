from django.db import models
from django.utils.translation import ugettext_lazy as _
__author__ = "spi4ka"


class SocialNetwork(models.Model):

    name = models.CharField(_("Name"), max_length=100)
    link = models.CharField(_("Link"), max_length=300)

    da = models.DateTimeField(_("Date of create"), auto_now_add=True)
    de = models.DateTimeField(_("Date of last edit"), auto_now=True)

    class Meta:
        verbose_name = _("Social Network")
        verbose_name_plural = _("Social Networks")
        ordering = ['-da']

    def __unicode__(self):
        return u"{}".format(self.__str__(),)

    def __str__(self):
        return self.name
