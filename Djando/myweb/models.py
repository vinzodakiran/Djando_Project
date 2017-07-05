# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class myweb_tabl(models.Model):
	name = models.CharField(max_length = 210)
	address = models.CharField(max_length = 210)

	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		
		
