from tkinter import *

win = Tk()

cv = Canvas(win,width = 400, height = 300)
cv.pack()

cv.create_polygon(
    30,200,50,280,350,280,370,200,
    fill="brown",
    outline="black",width=2)

cv.create_rectangle(
    100,120,300,200,
    fill="brown",
    outline="black",width=2)
cv.create_rectangle(
    240,70,260,120,
    fill="brown",
    outline="black",width=2)

cv.create_oval(
    250,45,270,65,
    fill="gray",
    outline="gray",width=2)

cv.create_oval(
    300,35,310,45,
    fill="gray",
    outline="gray",width=2)

cv.create_oval(
    280,40,290,50,
    fill="gray",
    outline="gray",width=2)


win.mainloop()

