#103-2
#lamda関数
#20630141 NGUYEN HOANG DUC

#普通の関数
def tasu(a,b):
    return a+b

hiku = lamda a,b:a-b

#変数に関数を代入--(*3)
add= tasu
sub= hiku

#変数に代入した関数を実行ーーー
print(add(100,10))
print(sub(50,5))
