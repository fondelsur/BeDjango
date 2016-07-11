from __future__ import unicode_literals

from django.db import models


class Notes(models.Model):
	body = models.TextField(verbose_name='Body')
	publish_date = models.DateTimeField(verbose_name='Created at',
										auto_now_add=True)
	addresee = models.CharField(verbose_name='Addresee', blank=True, null=True,
								max_length=255)

	class Meta(object):
		verbose_name = 'Note'
		verbose_name_plural = 'Notes'
