#20630141 NGUYEN HOANG DUC
#107-1 グエン　ホアン　ドゥック P201

def key_event(e):
    print("キーを押しました")
    print(e)

win= Tk()
win.bind("<Key>",key_event)
win.mainloop()
