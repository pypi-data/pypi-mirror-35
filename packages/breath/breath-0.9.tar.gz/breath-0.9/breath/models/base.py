import sys

from autologging import traced
from peewee import *
from breath import utils

this = sys.modules[__name__]
this.proxy = Proxy()

@traced
class Base(Model):
	class Meta:
		database = this.proxy

	def toString(self, *args):
		return utils.objToString(self, *args)

