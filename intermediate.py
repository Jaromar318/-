Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def moon_weight():
	print('Введите Ваш лунный вес')
	my_weight = float(sys.stdin.readline())
	weight = 1
	for year in range (1, 16):
		my_weight = my_weight + weight
		print('Год %s, вес: %ы' % (year, my_weight))
import sys
SyntaxError: invalid syntax
>>> import sys
>>> moon_weight()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    moon_weight()
NameError: name 'moon_weight' is not defined
>>> def moon_weight():
	print('Введите Ваш лунный вес')
	my_weight = float(sys.stdin.readline())
	weight = 1
	for year in range (1, 16):
		my_weight = my_weight + weight
		print('Год %s, вес: %ы' % (year, my_weight))

		
>>> moon_weight()
Введите Ваш лунный вес
18
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    moon_weight()
  File "<pyshell#11>", line 7, in moon_weight
    print('Год %s, вес: %ы' % (year, my_weight))
ValueError: unsupported format character '?' (0x44b) at index 14
>>> def moon_weight():
	print('Введите Ваш лунный вес')
	my_weight = float(sys.stdin.readline())
	weight = 1
	for week in range (1, 16):
		my_weight = my_weight + weight
		print('Год %s, вес: %ы' % (weak, my_weight))

		
>>> moon_weight()
Введите Ваш лунный вес
18
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    moon_weight()
  File "<pyshell#14>", line 7, in moon_weight
    print('Год %s, вес: %ы' % (weak, my_weight))
NameError: name 'weak' is not defined
>>> def moon_weight():
	print('Введите Ваш лунный вес')
	my_weight = float(sys.stdin.readline())
	weight = 1
	for week in range (1, 16):
		my_weight = my_weight + weight
		print('Год %s, вес: %ы' % (week, my_weight))

		
>>> moon_weight()
Введите Ваш лунный вес
18
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    moon_weight()
  File "<pyshell#17>", line 7, in moon_weight
    print('Год %s, вес: %ы' % (week, my_weight))
ValueError: unsupported format character '?' (0x44b) at index 14
>>> def moon_weight():
	print('Введите Ваш лунный вес')
	my_weight = float(sys.stdin.readline())
	weight = 1
	for year in range (1, 16):
		my_weight = my_weight + weight
		print('Год %s, вес: %s' % (year, my_weight))

		
>>> moon_weight()
Введите Ваш лунный вес
18
Год 1, вес: 19.0
Год 2, вес: 20.0
Год 3, вес: 21.0
Год 4, вес: 22.0
Год 5, вес: 23.0
Год 6, вес: 24.0
Год 7, вес: 25.0
Год 8, вес: 26.0
Год 9, вес: 27.0
Год 10, вес: 28.0
Год 11, вес: 29.0
Год 12, вес: 30.0
Год 13, вес: 31.0
Год 14, вес: 32.0
Год 15, вес: 33.0
>>> class Things
SyntaxError: invalid syntax
>>> class Things:
	pass

>>> class Inanimate(Things):
	pass

>>> class Animate(Things):
	pass

>>> class Sidwalks(Inanimate):
	pass

>>> class Animals(Animate):
	pass

>>> class Mammals(Animals):
	pass

>>> class Girafes(Mammals):
	pass

>>> class Animals(Animate):
	def breathe(self):
		pass
	def move(self):
		pass
	def eat_food(self):
		pass

	
>>> class Mammals(Animals):
	def feed_young_with_milk(self):
		pass

	
>>> class Giraffes(Mammals):
	def eat_leaves_from_trees(self):
		pass

	
>>> reginald = Giraffes()
>>> reginald.move()
>>> reginald.eat_leaves_from_treas()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    reginald.eat_leaves_from_treas()
AttributeError: 'Giraffes' object has no attribute 'eat_leaves_from_treas'
>>> reginald.eat_leaves_from_trees()
>>> harold = Giraffes()
>>> harold.move()
>>> class Animals(Animate):
	def breathe(self):
		print('дышит')
	def move(self):
		print('двигается')
	def eat_food(self):
		print('ест')

		
>>> class Mammals(Animals):
	def feed_young_with_milk(self):
		print('кормит детенышей молоком')

		
>>> class Giraffes(Mammals):
	def eat_leaves_from_trees(self):
		print('ест листья')

		
>>> reginald.move()
>>> reginald = Giraffes()
>>> harold = Giraffes()
>>> reginald.move()
двигается
>>> harold.eat_leaves_from_trees()
ест листья
>>> import turtle
>>> avery = turtle.Pen()
>>> kate = turtle.Pen()
>>> avery.forward(50)
>>> avery.right(90)
>>> avery.forward(20)
>>> kate.left(90)
>>> kate.forward(100)
>>> jacob = turtle.Pen()
>>> jacob.left(180)
>>> jacob.forward(80)
>>> jar = turtle.Pen()
>>> jar.right(90)
>>> jar.forward(150)
>>> jar.right(50)
>>> jar.forward(500)
>>> kate.forward(200)
>>> class Giraffes(Mammals):
	def find_food(self):
		self.move()
		print('Я нашел еду')
		self.eat_food()
	def eat_leaves_from_trees(self):
		self.eat_food()
	def dance_a_jig(self):
		self.move()
		self.move()
		self.move()
		self.move()

		
>>> reginald = Giraffes()
>>> reginald.dance_a_jig()
двигается
двигается
двигается
двигается
>>> class Giraffes:
	def _init_(self, spots):
		self.giraffe_spots = spots

		
>>> orwald = Giraffes(100)
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    orwald = Giraffes(100)
TypeError: Giraffes() takes no arguments
>>> class Giraffes:
	def __init__(self, spots):
		self.giraffes_spots = spots

		
>>> ozwald = Giraffes(100)
>>> gertrude = Giraffes(150)
>>> print(ozwald.giraffe_spots)
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    print(ozwald.giraffe_spots)
AttributeError: 'Giraffes' object has no attribute 'giraffe_spots'
>>> print(ozwald.giraffes_spots)
100
>>> 