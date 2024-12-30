from tkplotlib.artist import Artist


class FigureBase(Artist):
	def __init__(self):
		super().__init__()

		del self._axes


class Figure(FigureBase):
	def __init__(self):
		super().__init__()
		self._root_figure = self
