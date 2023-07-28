# 迷路の作成
from tkinter import *
import random

tile_size = 20 # 描画タイルのサイズ

# 迷路の作成
# ここに作った関数をコピーして
def create_maze(rows,cols):
    data = [[0 for i in range(cols)] for j in range(rows)]

    #外周を壁にする
    for j in range(0,rows):
        data[j][cols-1]=1
        data[j][0]=1
    for i in range(0,cols):
        data[0][i]=1
        data[rows-1][i]=1
    
    #柱を作って倒す(インデックスが偶数の時)

    for i in range(2,rows-1,2):
       for j in range(2,cols-1,2):
             data[i][j]=1              
             t=True
             while t==True:
               a=random.randint(0,3)
               if a==0:
                   if data[i+1][j]!=1:
                       data[i+1][j]=1
                       t=False
               elif a==1:
                   if data[i-1][j]!=1:
                       data[i-1][j]=1
                       t=False
               elif a==2:
                   if data[i][j-1]!=1:
                       data[i][j-1]=1
                       t=False
               else:
                   if data[i][j+1]!=1:
                       data[i][j+1]=1
                       t=False              
                
    return data





# 迷路を表示する関数
def draw_map(cv, data):
    # 左上から右下へと描画
    rows = len(map_data)    # 迷路の行数
    cols = len(map_data[0]) # 迷路の列数

    for y in range(rows):
        y1 = y * tile_size
        y2 = (y + 1) * tile_size
        for x in range(cols):
            x1 = x * tile_size
            x2 = (x + 1) * tile_size

            # 該当場所の値を得る
            p = data[y][x]
            # 値に応じた色を決定する
            if p == 0: color = "white"
            if p == 1: color = "#404040"
            if p == 2: color = "red"
            if p == 3: color = "blue"
            if p == 4: color = "green"
            if p == 5: color = "cyan"
            # 正方形を描画 --- (*5)
            cv.create_rectangle(
                    x1, y1, x2, y2, # 座標
                    fill = color, # 塗色
                    outline = "black", width = 2) # 枠線

# ウィンドウとキャンバスを作成
def create_window(data, events = []):
    rows = len(map_data)    # 迷路の行数
    cols = len(map_data[0]) # 迷路の列数
    
    win = Tk()
    win.title("迷路")
    cv = Canvas(win,
            width=(cols * tile_size), 
            height=(rows * tile_size))
    cv.pack()
    draw_map(cv, data)

    # 追加処理があればここで処理する
    for func in events: func(cv, data)
    win.mainloop()

if __name__ == "__main__":
    map_data = create_maze(11, 19)
    create_window(map_data)

