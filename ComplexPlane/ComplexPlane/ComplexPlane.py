import math
import tkinter as tk
import time
from enum import Enum

def mag(x, y):
	return math.sqrt(x * x + y * y)

def sf(x, digits):
	if x == 0:
		return 0
	return round(x, digits - int(math.floor(math.log10(abs(x)))) - 1)

class Angle(Enum):
	DEGREES = 1
	RADIANS = 2
	PI_RADIANS = 3
	TAU_RADIANS = 4

def formatAngle(degrees, angleFormat=Angle.TAU_RADIANS, sigfigs=3):
	"""
	Converts an angle in degrees to a formatted string, rounded to n significant figures.
	"""
	if angleFormat == Angle.DEGREES:
		angle = sf(degrees, 3)
		return f'{angle}°'
	
	if angleFormat == Angle.RADIANS:
		angle = sf(math.radians(degrees), sigfigs)
		return f'{angle} rad'

	if angleFormat == Angle.PI_RADIANS:
		angle = sf(math.radians(degrees) / math.pi, sigfigs)
		return f'{angle}π'

	if angleFormat == Angle.TAU_RADIANS:
		angle = sf(math.radians(degrees) / math.tau, sigfigs)
		return f'{angle}τ'

	return ""


#Width and height of the canvas
width = 1200
height = 800

#Scale of the graph in pixels
scale = 300

#Create tkinter window and canvas
window = tk.Tk()
canvas = tk.Canvas(window, width=width, height=height)
canvas.pack()
canvas.configure(scrollregion=(-width / 2, -height / 2, width / 2, height / 2))

def draw_axes():
	"""
	Draw the graph axes, unit circle and grid lines
	"""

	for x in range((int) (scale), (int) (width / 2), (int) (scale)):
		canvas.create_line(x, -height / 2, x, height / 2, fill="light gray")
		canvas.create_line(-x, -height / 2, -x, height / 2, fill="light gray")

	for y in range((int) (scale), (int) (height / 2), (int) (scale)):
		canvas.create_line(-width / 2, y, width / 2, y, fill="light gray")
		canvas.create_line(-width / 2, -y, width / 2, -y, fill="light gray")

	canvas.create_oval(-scale, -scale, scale, scale, outline="light gray")

	canvas.create_line(-width / 2, 0, width / 2, 0, arrow=tk.BOTH)
	canvas.create_line(0, -height / 2, 0, height / 2, arrow=tk.BOTH)


def draw_vector_arc(x, y, color, tags="draw"):

	xS = x * scale
	yS = -y * scale

	radians = math.atan2(y, x)
	degrees = math.degrees(radians)
	magnitude = mag(xS, yS)

	canvas.create_arc(-magnitude, -magnitude, magnitude, magnitude, extent=degrees, style=tk.ARC, outline=color, tags=tags)
	canvas.create_line(0, 0, xS, yS, fill=color, arrow=tk.LAST, tags=tags)
	canvas.create_text(x * scale, -y * scale, fill=color, text=f'{sf(x, 3)}+{sf(y, 3)}i ({formatAngle(degrees)})', anchor=tk.S, tags=tags)
	
def draw_vector_arc2(degrees, magnitude, color, start=0, tags="draw"):
	radians = math.radians(degrees)
	startRadians = math.radians(start)
	x = math.cos(radians) * magnitude
	y = math.sin(radians) * magnitude
	xS = math.cos(radians + startRadians) * magnitude * scale
	yS = -math.sin(radians + startRadians) * magnitude * scale
	magS = mag(xS, yS)

	canvas.create_arc(-magS, -magS, magS, magS, start=start, extent=degrees, style=tk.ARC, outline=color, tags=tags)
	canvas.create_line(0, 0, xS, yS, fill=color, arrow=tk.LAST, tags=tags)
	#canvas.create_text(x * scale, -y * scale, fill=color, text=f'{sf(x, 3)}+{sf(y, 3)}i ({formatAngle(degrees)} x {sf(magnitude, 3)})', anchor=tk.S, tags=tags)
		

def exp(x, r=100):
	return sum([
		x**n / math.factorial(n)	
		for n in range(0, r)
	])

def draw_exp_spiral(theta, magnitude=1, start=0, end=100):

	v0 = (0, 0)
	d0 = v0
	gr = 1 / 1.61803398875

	for n in range(start, end):
		r = ((n + 1) % 2) * (2 - ((n + 1) % 4))
		i = (n % 2) * (2 - (n % 4))
		
		f = 1 / math.factorial(n)
		p = theta ** n

		r *= f * p * magnitude * scale
		i *= f * p * magnitude * scale

		v1 = (r + v0[0], -i + v0[1])

		d1 = (r * gr + v0[0], -i * gr + v0[1])

		canvas.create_line(v0, v1, tags="draw")
		#canvas.create_arc(min(vm1[0], v1[0]), min(vm1[1], v1[1]), max(vm1[0], v1[0]), max(vm1[1], v1[1]), tags="draw")
		canvas.create_line(d0, v0, d1, smooth="true", tags="draw")
		v0 = v1
		d0 = d1


class Complex:

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def mag_angle(magnitude, degrees):
		radians = math.radians(degrees)
		a = math.cos(radians) * magnitude
		b = math.sin(radians) * magnitude
		return Complex(a, b)

	def magnitude(self):
		return mag(self.a, self.b)

	def radians(self):
		return (math.atan2(self.b, self.a) % math.tau + math.tau) % math.tau

	def degrees(self):
		return (math.degrees(math.atan2(self.b, self.a)) % 360 + 360) % 360

	def __add__(self, other):
		a = self.a + other.a
		b = self.b + other.b
		return Complex(a, b)

	def __mul__(self, other):

		#Bracket expansion method
		a = self.a * other.a - self.b * other.b
		b = self.a * other.b + other.a * self.b
		return Complex(a, b)

		#Polar coordinates method
		radians = self.radians() + other.radians()
		magnitude = self.magnitude() * other.magnitude()
		a = math.cos(radians) * magnitude
		b = math.sin(radians) * magnitude
		return Complex(a, b)

	def print(self):
		print(f'{sf(self.a, 3)}+{sf(self.b, 3)}i ({formatAngle(self.degrees())} x {sf(self.magnitude(), 3)})')

	def draw(self, color, start=0):
		draw_vector_arc2(self.degrees(), self.magnitude(), color, start)





#c1 = Complex(4, 1)
#c2 = Complex(3, 2)
#c3 = c1 * c2
#
#c1.draw("red")
#c2.draw("green", start=c1.degrees())
#c3.draw("blue")

draw_axes()

a = 0
while True:
	canvas.delete('draw')
	draw_vector_arc2(math.degrees(a), 1, "green")
	draw_exp_spiral(a, 1, 0, 100)
	a += math.pi * .01
	time.sleep(0.01)
	canvas.update()