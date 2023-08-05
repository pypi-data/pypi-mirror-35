import contextlib


@contextlib.contextmanager
def capture():
	import sys
	from io import StringIO
	oldout, olderr = sys.stdout, sys.stderr
	try:
		out = [StringIO(), StringIO()]
		sys.stdout, sys.stderr = out
		yield out
	finally:
		sys.stdout, sys.stderr = oldout, olderr
		out[0] = out[0].getvalue()
		out[1] = out[1].getvalue()


def objToString(obj, *args):
	infos = []
	for arg in args:
		cal = (obj, arg)
		if hasattr(*cal):
			atr = getattr(*cal)
		else:
			atr = None

		infos.append(f'{arg}={atr}')

	info = ','.join(infos)
	return f'{obj.__class__.__name__}({info})'
