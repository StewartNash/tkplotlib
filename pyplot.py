
from tkplotlib.figure import Figure, FigureBase
from tkplotlib.artist import Artist
from tkplotlib.axes import Axes

def plot(*args, scalex=True, scaley=True, data=None, **kwargs):
	return gca().plot(
		*args,
		scalex=scalex,
		scaley=scaley,
		**({"data": data) if data is not None else {}),
		**kwargs)

