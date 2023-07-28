#20630141 NGUYEN HOANG DUC
#111-2
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as split
from sklearn import svm
from PIL import Image
import numpy as np


digits= load_digits()
print(digits.DESCR)

index = 19
print(digits.data[index])
print(digits.target[index])

plt.matshow(digits.images[index],cmap="gray")
plt.show()

for i in [3,10,12]:
    n = 16 - digits.data[i]
    nr = n.reshape(8,8)
    plt.matshow(nr,cmap= "gray")   
plt.show()

x_train, x_test, y_train, y_test = split(digits.data,digits.target,train_size=0.8)


clf = svm.LinearSVC()


clf.fit(x_train, y_train)

pred = clf.predict(x_test)

result = list(pred == y_test).count(True)/ len(y_test)
print("正確率" + str(result))

png_file = "tegaki10.png"

img = Image.open(png_file)
plt.imshow(img)

img.thumbnail((8,8),Image.LANCZOS)
img = img.convert("L")
plt.matshow(img, cmap="gray")

img_a= np.array(img,"f")
img_a= 255 - img_a
img_a= img_a//16
img_a= img_a.reshape(-1,)

"""print("---学習に利用したデータ---")
print(digits.data[0])

print("----今回変換したデータ---")
print(img_a)"""

#学習モデルを読み込んで判定
pred = clf.predict([img_a])
print("---判定結果--")
print(result)

