#20630141 NGUYEN HOANG DUC
#113
#P248

from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as split
from sklearn import svm
from PIL import Image
import numpy as np
import glob

data = []
target = []

def glob_images(dir, label, size):
    files = glob.glob(dir + "/*.jpg")
    for f in files:
        img = Image.open(f)
        img= img.convert("RGB")
        img.thumbnail((size,size),Image.LANCZOS)
        ary = np.array(img).reshape(-1,)
        data.append(ary)
        target.append(label)
        
#画像ディレクトリとラベル、画像サイズ指定してデータを追加
glob_images("./lemon",label=0,size=128)
glob_images("./strawberry",label=1,size=128)


for i in [100,200,300,400,500]:
    n = data[i]
    nr = n.reshape(128,128,3)
    plt.matshow(nr,)   
plt.show()

x_train, x_test, y_train, y_test = split(data,target,train_size=0.8)


clf = svm.LinearSVC()


clf.fit(x_train, y_train)

pred = clf.predict(x_test)


result = list(pred == y_test).count(True)/ len(y_test)
print("正確率" + str(result))

