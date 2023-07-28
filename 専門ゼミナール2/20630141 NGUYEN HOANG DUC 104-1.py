#20630141 NGUYEN HOANG DUC
#104-1

from tkinter import *
from PIL import ImageTk, Image

# ウィンドウとキャンバスを作成
win = Tk()
cv = Canvas(win, width=710, height=396)
cv.pack()

# 画像ファイルを読む
filename = "meditation.jpg"
img = Image.open(filename)
print("size={0}x{1}".format(img.width, img.height))

# Tkinterで使えるように変換
img_tk = ImageTk.PhotoImage(img)

# 画像を表示
cv.create_image(0, 0, image=img_tk, anchor=NW)

# メインループを実行
win.mainloop()


