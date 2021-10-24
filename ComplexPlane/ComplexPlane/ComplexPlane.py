import math
import tkinter as tk
from enum import Enum



def mag(x, y):
	return math.sqrt(x * x + y * y)

def sf(x, digits):
	return round(x, digits - int(math.floor(math.log10(abs(x)))) - 1)

class Angle(Enum):
	DEGREES = 1
	RADIANS = 2
	PI_RADIANS = 3

def formatAngle(degrees, angleFormat=Angle.DEGREES, sigfigs=3):
	if angleFormat == Angle.DEGREES:
		angle = sf(degrees, 3)
		return f'{angle}°'
	
	if angleFormat == Angle.RADIANS:
		angle = sf(math.radians(degrees), sigfigs)
		return f'{angle} rad'

	if angleFormat == Angle.PI_RADIANS:
		angle = sf(math.radians(degrees) / math.pi, sigfigs)
		return f'{angle}π'

	return ""


width = 1000
height = 600
origin = width / 2, height / 2
scale = 20, 20

window = tk.Tk()
canvas = tk.Canvas(window, width=width, height=height)
canvas.pack()

canvas.configure(scrollregion=(-width / 2, -height / 2, width / 2, height / 2))

def draw_axes():

	for x in range((int) (-width / 2), (int) (width / 2), scale[0]):
		canvas.create_line(x, -height / 2, x, height / 2, fill="light gray")

	for y in range((int) (-height / 2), (int) (height / 2), scale[1]):
		canvas.create_line(-width / 2, y, width / 2, y, fill="light gray")

	canvas.create_line(-width / 2, 0, width / 2, 0, arrow=tk.BOTH)

	canvas.create_line(0, -height / 2, 0, height / 2, arrow=tk.BOTH)

def draw_arc(degrees, color):
	canvas.create_arc(-100, -100, 100, 100, extent=degrees, style=tk.ARC)

def draw_vector_arc(x, y, color):

	xS = x * scale[0]
	yS = -y * scale[1]

	radians = math.atan2(y, x)
	degrees = math.degrees(radians)
	magnitude = mag(xS, yS)

	canvas.create_arc(-magnitude, -magnitude, magnitude, magnitude, extent=degrees, style=tk.ARC, outline=color)
	canvas.create_line(0, 0, xS, yS, fill=color, arrow=tk.LAST)
	canvas.create_text(x * scale[0], -y * scale[1], fill=color, text=f'{sf(x, 3)}+{sf(y, 3)}i ({formatAngle(degrees)})', anchor=tk.S)
	
def draw_vector_arc2(degrees, magnitude, color, start=0):
	radians = math.radians(degrees)
	startRadians = math.radians(start)
	x = math.cos(radians) * magnitude
	y = math.sin(radians) * magnitude
	xS = math.cos(radians + startRadians) * magnitude * scale[0]
	yS = -math.sin(radians + startRadians) * magnitude * scale[1]
	magS = mag(xS, yS)

	canvas.create_arc(-magS, -magS, magS, magS, start=start, extent=degrees, style=tk.ARC, outline=color)
	canvas.create_line(0, 0, xS, yS, fill=color, arrow=tk.LAST)
	canvas.create_text(x * scale[0], -y * scale[1], fill=color, text=f'{sf(x, 3)}+{sf(y, 3)}i ({formatAngle(degrees)} x {sf(magnitude, 3)})', anchor=tk.S)
		
class Complex:

	def __init__(self, a, b):
		self.a = a
		self.b = b
		self.magnitude = mag(a, b)
		self.angle = math.atan2(b, a)

	def degrees(self):
		return math.degrees(self.angle)

	def mag_angle(magnitude, radians):
		return Complex(math.cos(radians) * magnitude, math.sin(radians) * magnitude)

	def __add__(self, other):
		return Complex(self.a + other.a, self.b + other.b)

	def __mul__(self, other):
		radians = self.angle + other.angle
		magnitude = self.magnitude * other.magnitude
		return Complex(math.cos(radians) * magnitude, math.sin(radians) * magnitude)

	def print(self):
		print(f'{sf(self.a, 3)}+{sf(self.b, 3)}i ({formatAngle(math.degrees(self.angle))} x {sf(self.magnitude, 3)})')

	def draw(self, color, start=0):
		draw_vector_arc2(math.degrees(self.angle), self.magnitude, color, start)

draw_axes()

c1 = Complex(4, -1)
c2 = Complex(-3, 2)
c3 = c1 * c2

c1.print()
print("x")
c2.print()
print("=")
c3.print()

c1.draw("red")
c2.draw("green", start=c1.degrees())
c3.draw("blue")

window.mainloop()
