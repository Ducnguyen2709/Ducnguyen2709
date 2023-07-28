# -*- coding: utf-8 -*-
# 20630000　氏名
# 107-2 ゲームのメインプログラム　P203

from tkinter import *
from PIL import Image, ImageTk
from drivegame_info import ginfo
from drivegame_map import *

# ウィンドウとキャンバスを作成
def create_window(ginfo):
    
    # ウィンドウサイズを計算
    w = ginfo["cols"] * ginfo["tile_size"]
    h = ginfo["rows"] * ginfo["tile_size"]
    
    # ウィンドウとキャンバスを作成
    win = Tk()
    ginfo["cv"] = Canvas(win, width = w, height = h)
    ginfo["cv"].pack()
    
    # 画像を読み込み
    img = Image.open("car32.png")
    ginfo["car_img"] = ImageTk.PhotoImage(img)
    
    # 走行コースデータを作成
    ginfo["map_data"] = create_map(ginfo)
    
    return win    

# 道路と車の描画
def draw_map(ginfo):
    cv = ginfo["cv"] 
    cv.delete("all") # 既存のキャンバスをクリア
    
    # 道路を描画
    tile_size = ginfo["tile_size"]
    colors = ["white", "#442233"] # 道路と障壁の色
    
    for y in range(ginfo["rows"]):
        y1 = y * tile_size
        y2 = (y + 1) * tile_size
        for x in range(ginfo["cols"]):
            x1 = x * tile_size
            x2 = (x + 1) * tile_size
            
            # タイルを描画
            v = ginfo["map_data"][y][x]
            color = colors[v] #塗色の指定
            cv.create_rectangle(
                    x1, y1, x2, y2, # 座標
                    fill = color, # 塗色
                    width = 0) # 枠線なし
    
    # 車を描画（ｙ座標を下から2行目に固定）
    x = ginfo["car"] * ginfo["tile_size"]
    y = (ginfo["rows"] - 2) * ginfo["tile_size"]
    cv.create_image(x, y, image=ginfo["car_img"], anchor=NW)

if __name__ == "__main__":
    win = create_window(ginfo)
    draw_map(ginfo)
    win.mainloop()
            
            
