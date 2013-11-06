from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from skd_tools.utils import image_path
from ckeditor.fields import RichTextField


class Position(models.Model):
    title = models.CharField(max_length=64, verbose_name=_('position title'))
    key = models.SlugField(max_length=10, verbose_name=_('short position title'))
    description = models.CharField(max_length=256, verbose_name=_('description position'))


class Science(models.Model):
    title = models.CharField(max_length=64, verbose_name=_('position title'))
    key = models.SlugField(max_length=10, verbose_name=_('short position title'))
    description = models.CharField(max_length=256, verbose_name=_('description position'))


class Lector(models.Model):
    first_name = models.CharField(_('first name'), max_length=30)
    middle_name = models.CharField(_('middle name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    position_title = models.ForeignKey(Position, verbose_name=_('position'), related_name='position')
    science_title = models.ForeignKey(Science, verbose_name=_('science'), related_name='science')
    contact = models.CharField(max_length=64, verbose_name=_('contacts'))
    photo = models.ImageField(upload_to=image_path, verbose_name=_("lector's photo"))
    bio = RichTextField(verbose_name=_("lelctor's biography"))


class Room(models.Model):
    number = models.PositiveIntegerField(verbose_name=_('number room'))
    title = models.CharField(max_length=64, verbose_name=_('title room'))
    description = RichTextField(verbose_name=_('description room'))
