from tkinter import *

win = Tk()

cv = Canvas(win,width = 400, height = 300)
cv.pack()

#円の描画
cv.create_oval(
    120,120,240,240,
    fill="red",
    outline="green",width=2)

cv.create_polygon(
    210,290,390,290,390,140,
    fill="blue",
    outline="red",width=2)

cv.create_rectangle(
    10,10,130,110,
    fill="green",
    outline="red",width=2)

win.mainloop()

