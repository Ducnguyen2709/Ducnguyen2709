# 02:繰り返し小さな円を表示

from tkinter import *

# ランダムな色を返す関数
w=int(input("幅の長さは?"))
h=int(input("縦の長さは?"))

def random_color():
    # ランダムに色の配色を決定
    from random import randint 
    rnd = lambda : randint(0, 255)
    r = rnd()
    g = rnd()
    b = rnd()
    # HTMLの色形式に変換
    f = "#{0:02x}{1:02x}{2:02x}"
    color = f.format(r, g, b)
    return color

# たくさんの円を描画する
def draw_circles():
    # 画面を初期化
    cv.delete("all")
    # 繰り返し円を描画
    for y in range(int(h/20)):
        y1 = y * 20
        y2 = y1 + 20
        for x in range(int(w/20)):
            x1 = x * 20
            x2 = x1 + 20
            # 円を描画
            color = random_color()
            cv.create_oval(x1, y1, x2, y2, 
                    fill = color, width = 0)
    # 0.1秒後に再描画
    win.after(100, draw_circles)

# ウィンドウとキャンバスを作成
win = Tk()
cv = Canvas(win, width=w,height=h)
cv.pack()

win.after(1, draw_circles) # 円を描画
win.mainloop()

