from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from skd_tools.utils import image_path
from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField


class Position(models.Model):
    title = models.CharField(max_length=64, verbose_name=_('position title'))
    key = models.SlugField(max_length=10, verbose_name=_('short title'))
    description = models.CharField(max_length=256, blank=True, verbose_name=_('description'))

    def __unicode__(self):
        return self.title


class Science(models.Model):
    title = models.CharField(max_length=64, verbose_name=_(' science title'))
    key = models.SlugField(max_length=10, verbose_name=_('short title'))
    description = models.CharField(max_length=256, blank=True, verbose_name=_('description'))

    def __unicode__(self):
        return self.title


class Lector(models.Model):
    last_name = models.CharField(_('last name'), max_length=30)
    first_name = models.CharField(_('first name'), max_length=30)
    middle_name = models.CharField(_('middle name'), max_length=30)
    position_title = models.ForeignKey(Position, verbose_name=_('position'), related_name='l_position')
    science_title = models.ForeignKey(Science, verbose_name=_('science'), related_name='l_science')
    contact = models.CharField(max_length=64, verbose_name=_('contacts'))
    photo = ImageField(upload_to=image_path, verbose_name=_('photo'))
    bio = RichTextField(verbose_name=_('biography'))

    def __unicode__(self):
        return '{} {} {}'.format(self.last_name, self.first_name, self.middle_name)

    def get_absolute_url(self):
        return "/lectors/%i/" % self.id


class Aspirant(models.Model):
    last_name = models.CharField(_('last name'), max_length=30)
    first_name = models.CharField(_('first name'), max_length=30)
    middle_name = models.CharField(_('middle name'), max_length=30)
    position_title = models.ForeignKey(Position, verbose_name=_('position'), related_name='a_position', blank=True, null=True)
    science_title = models.ForeignKey(Science, verbose_name=_('science'), related_name='a_science')
    contact = models.CharField(max_length=64, verbose_name=_('contacts'))
    photo = ImageField(upload_to=image_path, verbose_name=_('photo'))
    bio = RichTextField(verbose_name=_('biography'))

    def __unicode__(self):
        return '{} {} {}'.format(self.last_name, self.first_name, self.middle_name)

    def get_absolute_url(self):
        return "/aspirants/%i/" % self.id


class Technician(models.Model):
    last_name = models.CharField(_('last name'), max_length=30)
    first_name = models.CharField(_('first name'), max_length=30)
    middle_name = models.CharField(_('middle name'), max_length=30)
    position_title = models.ForeignKey(Position, verbose_name=_('position'), related_name='t_position', blank=True, null=True)
    science_title = models.ForeignKey(Science, verbose_name=_('science'), related_name='t_science', blank=True, null=True)
    contact = models.CharField(max_length=64, verbose_name=_('contacts'))
    photo = ImageField(upload_to=image_path, verbose_name=_('photo'))
    bio = RichTextField(verbose_name=_('biography'))

    def __unicode__(self):
        return '{} {} {}'.format(self.last_name, self.first_name, self.middle_name)

    def get_absolute_url(self):
        return "/technicians/%i/" % self.id


class Room(models.Model):
    number = models.PositiveIntegerField(verbose_name=_('number'))
    title = models.CharField(max_length=64, verbose_name=_('title'))
    description = RichTextField(blank=True, verbose_name=_('description'))

    def __unicode__(self):
        return str(self.number)
