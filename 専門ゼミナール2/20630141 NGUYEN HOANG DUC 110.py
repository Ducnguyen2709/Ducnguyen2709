# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""
#20630141 NGUYEN HOANG DUC
#110-1(p222)

from sklearn import datasets
import random
import numpy as np
iris = datasets.load_iris()
"""
print(iris.DESCR)
print(iris.data)
print(iris.target)

#二つのリストを合成
d=list(zip(iris.data.tolist(),iris.target))
#シャップル
random.shuffle(d)
#8:2の割合で分ける
train_data = d[0:120]
test_data = d[120:150]

#合成したリストを分離する
x_train, y_train = zip(*train_data)
x_test, y_test = zip(*test_data)
 
print(list(zip(x_train, y_train)))
print(x_train,y_train)
"""
from sklearn.model_selection import train_test_split as split

x_train, x_test, y_train, y_test = split(iris.data,iris.target,train_size = 0.8)

from sklearn import svm

clf = svm.SVC()

clf.fit(x_train, y_train)

pred = clf.predict(x_test)

result = list(pred == y_test).count(True)/ len(y_test)
print("正確率" + str(result))

cnt = 0
for pre,y in zip(pred, y_test):
    result = (pre == y)
    print(pre,y,result)
    if result: cnt +=1
print("{0}/{1}={2}".format(cnt,len(y_test),cnt/len(y_test)))
    
    