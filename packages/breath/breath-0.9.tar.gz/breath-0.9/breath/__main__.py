'''
Usage:
  breath start
  breath train
  breath clean

'''

import logging
from docopt import docopt
from breath import main

log = logging.getLogger(__name__)


def cli():
	arguments = docopt(__doc__)
	main.init()

	if arguments.get('start'):
		main.start()
	elif arguments.get('train'):
		main.train()
	elif arguments.get('clean'):
		main.clean()


if __name__ == '__main__':
	cli()
