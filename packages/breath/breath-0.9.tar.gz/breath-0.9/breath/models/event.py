import datetime
from typing import List, Tuple
from statistics import mean, stdev
import logging
from breath.models.session import Session
from autologging import traced
from peewee import *

from breath.models.base import Base

log = logging.getLogger(__name__)


@traced
class Event(Base):

	@staticmethod
	def trainStatistics():
		timeDiff = []
		for session in Session.select().where(Session.training == True):
			events: List[Event] = Event.select().where(Event.session == session)
			if len(events) > 1:
				for i in range(1, len(events)):
					timeDiff.append((events[i].createdAt - events[i - 1].createdAt).total_seconds())

		return mean(timeDiff), stdev(timeDiff)

	session: Session = ForeignKeyField(Session, backref='session')

	window: str = TextField()
	windowName: str = TextField()
	processName: str = TextField()
	key: str = TextField()
	ascii: str = IntegerField()
	message: str = TextField()

	# DEFAULT
	createdAt: datetime.datetime = DateTimeField(default=datetime.datetime.now)

	def save(self, *args, **kwargs):
		return super().save(*args, **kwargs)

	def __str__(self):
		return self.toString('id', 'session', 'windowName', 'processName', 'key', 'ascii', 'message')
