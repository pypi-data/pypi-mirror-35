import sys
import time
from autologging import traced
import logging
import pyxhook
from breath import models

log = logging.getLogger(__name__)

this = sys.modules[__name__]
this.api: pyxhook.HookManager = None
this.session: models.Session = None
this.callback = lambda: None
this.callbackKey: models.Event = None

@traced
def init():
	this.api = pyxhook.HookManager()
	this.api.KeyDown = onKeyDownEvent
	this.api.HookKeyboard()
	log.debug(' - pyxhookAPI inited')

def listen(training: bool, callback=None, callbackKey=None):
	log.info('pyxhookAPI is listening for event...')

	this.callback = callback
	this.callbackKey = callbackKey

	this.api.start()

	this.session = models.Session(training=training)
	this.session.save()

	try:
		while this.session.running:
			time.sleep(0.1)
	except KeyboardInterrupt:
		stop()

def stop():
	log.info('pyxhookAPI stoped listening for event...')
	this.session.stop()
	this.api.cancel()

@traced
def onKeyDownEvent(event):
	eventModel = models.Event(
		session=this.session,

		window=event.Window,
		windowName=event.WindowName,
		processName=event.WindowProcName,
		key=event.Key,
		ascii=event.Ascii,
		message=event.MessageName
	)
	eventModel.save()

	log.info(' > %s', eventModel.key)

	if this.callbackKey is None:
		log.warning('Setting callback key: %s', eventModel)
		this.callbackKey = eventModel

	if eventModel.ascii == this.callbackKey.ascii:
		this.callback(eventModel)

	if eventModel.ascii == 87 or eventModel.key == 'End':
		this.stop()
		exit(0)
