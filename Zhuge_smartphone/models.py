# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class UserAvatar(models.Model):
	avatar_index = models.IntegerField(default = 0)
	d_name = models.CharField(max_length = 100)
	reg_name = models.CharField(max_length = 100)
	isOccupied = models.BooleanField(default = False)
	user_name = models.CharField(max_length = 100)
	lastused = models.DateTimeField(default = datetime.now, blank=True)
	def __str__(self):
		return 'smartphone {}'.format(self.avatar_index)

