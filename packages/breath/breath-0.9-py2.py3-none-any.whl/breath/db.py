import logging
import sys
import urllib.parse
from typing import Union

from autologging import traced
from playhouse.sqlite_ext import SqliteExtDatabase

import breath
from breath import models
from breath.settings import logger
from breath.models.base import proxy
from breath.utils import path

log = logging.getLogger(__name__)

this = sys.modules[__name__]
this.instance: SqliteExtDatabase = None


@traced
def init(memory=False):
	log.info('Database initing')
	this.instance = SqliteExtDatabase(str(path.app('data', f'{breath.__name__}.sqlite')))

	proxy.initialize(this.instance)
	connect()
	seedTables()


def seedTables():
	log.warning('Database creating arhitecture...')
	this.instance.create_tables([
		models.Event, models.Session
	])


@traced
def connect():
	log.info('Database connecting...')
	this.instance.connect(reuse_if_open=True)

@traced
def clean():
	this.instance.drop_tables([
		models.Event, models.Session
	])

@traced
def close():
	log.info('Database closing...')
	this.instance.close()


if __name__ == '__main__':
	init()

	for event in models.Event.select():
		print(event)
