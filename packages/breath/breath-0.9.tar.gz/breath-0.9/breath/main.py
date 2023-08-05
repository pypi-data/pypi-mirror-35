import logging
from breath import utils
import sys
from autologging import traced
from multiprocessing import Process
from breath import db, models
from breath.settings import logger
from breath.utils import path
from breath.services import pyxhookAPI, audio

this = sys.modules[__name__]

log = logging.getLogger(__name__)


@traced
def init(ENV='dev'):
	logger.init(path.app(f'data/settings/logger.{ENV}.json'))
	db.init(memory=False)

	pyxhookAPI.init()


@traced
def train():
	log.info('Start recording events:')

	def callback(event: models.Event):
		pass

	pyxhookAPI.listen(training=True, callback=callback)

@traced
def clean():
	log.info('Cleaning database')
	db.clean()

@traced
def start():
	log.info('Start traning breath:')

	mean, stderr = models.Event.trainStatistics()

	def play(file):

		with utils.capture() as out:
			audioFile = audio.File(file=str(path.app(f'data/sounds/{file}.wav')))
			audioFile.play()
			audioFile.close()

	def callback(event: models.Event):

		query = models.Event.select()
		query = query.where(models.Event.session == event.session)
		query = query.order_by(models.Event.createdAt.desc())
		query = query.paginate(1, 2)

		if len(query) == 2:
			timeDiff = (query[0].createdAt - query[1].createdAt).total_seconds()

			if mean - stderr < timeDiff < mean + stderr:
				# This is breath
				return None

			elif timeDiff < mean - stderr:
				missedTime = round(timeDiff - (mean - stderr), 2)
				thread = Process(target=play, args=('lower', ))
			else:
				missedTime = round(timeDiff - (mean + stderr), 2)
				thread = Process(target=play, args=('higher', ))

			log.warning('Timediff: %s sec',missedTime)

			thread.daemon = True
			thread.start()

	log.warning('Enter callback key: ')
	pyxhookAPI.listen(training=False, callback=callback)
