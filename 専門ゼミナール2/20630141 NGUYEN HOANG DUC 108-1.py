# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 10:57:29 2021

@author: 20937734
"""
import sys
from drivegame_info import ginfo
from drivegame_map import *
from drivegame_draw import *
import tkinter.messagebox as msgbox

def init_game():
    global win
    
    #ウインドウとキャンバスと走行コース生成
    win = create_window(ginfo)
    
    #キーボードのイベントを設定
    win.bind("<Left>", key_event_left)
    win.bind("<Right>", key_event_right)
    #ゲーム開始
    game_loop() 
    win.mainloop()
    
#キーイベントの定義
def key_event_left(e):
    if ginfo["car"] > 0 :
        ginfo["car"]-=1

def key_event_right(e):
    if ginfo["car"] <= ginfo["cols"] :
        ginfo["car"]+=1
        
def game_loop():
    draw_map(ginfo)
    win.title("ドライブゲーム　スコア=" + str(ginfo["score"]))
    map_data = ginfo["map_data"]
    v= map_data[ginfo["rows"]-2][ginfo["car"]]
    if v!=0:
        msgbox.showinfo(
                title="ゲームオーバー",
                message="コースアウトしました\n" +
                        "スコア="+ str(ginfo["score"]))
        ret = msgbox.askyesno("確認", "ゲームを終了しますか？")
        if ret == True:
            
            destroy()
    #スコアを加算
    ginfo["score"]+=10
    
    del(map_data[ginfo["rows"]-1])
    line = create_map_line(ginfo)
    map_data.insert(0,line)
    win.after(100,game_loop)
    
if __name__=="__main__": init_game()
