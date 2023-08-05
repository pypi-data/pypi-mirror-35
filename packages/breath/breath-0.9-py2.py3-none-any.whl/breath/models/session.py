import datetime
import logging
from autologging import traced
from peewee import *
from breath.models.base import Base

log = logging.getLogger(__name__)

@traced
class Session(Base):

	training: bool = BooleanField()
	running: bool = BooleanField(default=True)
	createdAt: datetime.datetime = DateTimeField(default=datetime.datetime.now)

	def stop(self):
		self.running = False
		self.save()

	def __str__(self):
		return self.toString('id')




