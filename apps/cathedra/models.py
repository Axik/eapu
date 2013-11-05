from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from skd_tools.utils import image_path
from django.db import models
from ckeditor.fields import RichTextField


class Position(models.Model):
    title = models.CharField(max_length=64)
    key = models.AutoField(primary_key=True)
    description = models.CharField(max_length=256)


class Science(models.Model):
    title = models.CharField(max_length=64)
    key = models.AutoField(primary_key=True)
    description = models.CharField(max_length=256)


class Lector(models.Model):
    first_name = models.CharField(_('first name'), max_length=30)
    middle_name = models.CharField(_('middle name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    position_title = models.ForeignKey(Position, verbose_name=_('position'), related_name='position')
    science_title = models.ForeignKey(Science, verbose_name=_('science'), related_name='science')
    contact = models.CharField(max_length=64)
    photo = models.ImageField(upload_to=image_path)
    bio = RichTextField()


class Room(models.Model):
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=64)
    description = RichTextField()
