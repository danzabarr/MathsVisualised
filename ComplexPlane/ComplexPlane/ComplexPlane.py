import tkinter as tk

width = 1000
height = 600
origin = width / 2, height / 2
scale = 10, 10

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

def draw_vector(x1, y1, x2, y2, color):
	canvas.create_line(x1 * scale[0], -y1 * scale[1], x2 * scale[0], -y2 * scale[1], fill=color, arrow=tk.LAST)


def draw_vector(x, y, color):
	canvas.create_line(0, 0, x * scale[0], -y * scale[1], fill=color, arrow=tk.LAST)
	canvas.create_text(x * scale[0], -y * scale[1], fill=color, text=f'({x},{y})', anchor=tk.S)

draw_axes()

draw_vector(5, 3, "red")

window.mainloop()
