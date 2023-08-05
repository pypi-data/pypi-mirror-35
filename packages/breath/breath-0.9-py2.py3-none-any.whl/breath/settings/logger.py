import json
import logging
import logging.config
import sys
from pathlib import Path

import coloredlogs
from autologging import traced

from breath.utils import path

log = logging.getLogger(__name__)

this = sys.modules[__name__]
this.level = None

@traced
def init(file: Path = path.app('data/settings/logger.dev.json')):
	with file.open() as f:
		setup = json.load(f)

	# Create logging directory
	path.logBase.mkdir(exist_ok=True)

	# Setup for file loggers
	for name, logger in setup['handlers'].items():
		if '_file_handler' in name:
			if logger['filename'] is None:
				logger['filename'] = path.log(f'{str(logger["level"]).lower()}.log')
			else:
				logger['filename'] = path.log(logger['filename'])

	# Setup our own flask and app logger
	logging.config.dictConfig(setup)
	coloredlogs.DEFAULT_LOG_FORMAT = setup['formatters']['console']['format']
	coloredlogs.DEFAULT_DATE_FORMAT = None
	coloredlogs.install(level=setup['handlers']['console_handler']['level'])

	log.info('Logger inited from: %s', file.absolute())
	for name, logger in setup['loggers'].items():
		log.debug(' - %s:\t%s', name, logger['level'])

	log.info('Logger streams: %s', path.logBase.absolute())
	for name, logger in setup['handlers'].items():
		if '_file_handler' in name:
			log.debug(' - %s: \t%s', name.replace('_file_handler', ''), logger['filename'])
