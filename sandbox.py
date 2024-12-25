import tkinter

root = tkinter.Tk()
root.title("tkplotlib")

canvas = tkinter.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

x_data = [10, 20, 30, 40, 50]
y_data = [20, 40, 10, 50, 30]

canvas.create_line(50, 250, 350, 250, width=2) # x-axis
canvas.create_line(50, 250, 50, 50, width=2) # y-axis

for i in range(len(x_data) - 1):
	x1 = x_data[i] * 5 + 50
	y1 = 250 - y_data[i] * 4
	x2 = x_data[i + 1] * 5 + 50
	y2 = 250 - y_data[i + 1] * 4
	canvas.create_line(x1, y1, x2, y2, width=2)

root.mainloop()
