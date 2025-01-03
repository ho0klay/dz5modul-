
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def distance(self):
		return(x ** 2 + y ** 2) ** (1 / 2)

	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)
