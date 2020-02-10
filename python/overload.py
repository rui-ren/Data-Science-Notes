class Human():
	def __init__(self, n):
		self.name = n
		print("__init__", self.name)
	def __def__(self):
		print("__del__")

h = Human('Time')

print('....')

h = 'a'
