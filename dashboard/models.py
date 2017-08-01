from __future__ import unicode_literals

from django.db import models


from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def p4_validator(value):
    if not value.startswith('//System/'):
        raise ValidationError(
            _('%(value)s is not an perforce link'),
            params={'value': value},
        )


# Create your models here.
class KP250Version(models.Model):

    version = models.CharField(max_length=30, blank=False)
    p4_link = models.CharField(max_length=255, blank=False, validators=[p4_validator])
    comment = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.version


class PlinkVersion(models.Model):

    version = models.CharField(max_length=30, blank=False)
    p4_link = models.CharField(max_length=255, blank=False, validators=[p4_validator])
    comment = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.version


class PanelVersion(models.Model):

    version = models.CharField(max_length=30, blank=False)
    comment = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.version


class PowerMaxVersion(models.Model):

    panel_version = models.ForeignKey(PanelVersion, blank=False)
    panel_type = models.CharField(max_length=30, blank=False)
    release = models.CharField(max_length=30, blank=False)
    default = models.CharField(max_length=30, blank=False)
    vlm = models.CharField(max_length=10, blank=False)
    eeprom_ver = models.CharField(max_length=30, default='Unknown')
    plink = models.ForeignKey(PlinkVersion, on_delete=models.SET_NULL, null=True, blank=True)
    kp_250 = models.ForeignKey(KP250Version, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.TextField(max_length=1000, blank=True)

    p4_release = models.CharField(max_length=255, blank=False, validators=[p4_validator])
    p4_default = models.CharField(max_length=255, blank=False, validators=[p4_validator])

    def __str__(self):
        return 'Panel: {0} Release: {1} Default: {2}'.format(self.panel_type, self.release, self.default)


