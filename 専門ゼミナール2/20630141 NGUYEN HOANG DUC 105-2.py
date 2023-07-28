#20630141 NGUYEN HOANG DUC
#105-1
#迷路のデータを作る

import random

#迷路の作成
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

map_data = create_maze(15,17)
print(*map_data,sep='\n')
