
class StringVar:

	def __init__(self, ):
		self.s = ''

	def set(self, val):
		self.s = val

	def get(self):
		return self.s	

s = StringVar()
print(s.set('Hello!'))
print(s.get())