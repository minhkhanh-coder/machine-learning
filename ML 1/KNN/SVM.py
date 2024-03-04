import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

# Load bộ dữ liệu Iris chỉ với 2 đặc trưng
iris = datasets.load_iris()
X = iris.data[:,:2] # Chỉ lấy 2 đặc trưng đầu tiên
y = iris.target

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Tạo mô hình SVM với kernel tuyến tính
clf = svm.SVC(kernel="linear")
clf.fit(X_train, y_train)

# Dự đoán nhanc trên tahao huấn luyện và tập kiểm thử
y_train_pred = clf.predict(X_train)
y_test_pred = clf.predict(X_test)

# Tính độ chính xác 
accuracy_train = accuracy_score(y_train, y_train_pred)
accuracy_test = accuracy_score(y_test, y_test_pred)

# In độ chính xác
print(f"đọo chính xác trên tập huấn luyện: {accuracy_train}")
print(f"đọ chính xác trên tập kiểm tra: {accuracy_test}")


# Trực quan hoá ranh giới quyết định
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)


# Vẽ đồ thị
plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm)
plt.xlabel('Đặc trưng 1')
plt.ylabel('Đặc trưng 2')
plt.title('Ranh giới quyết định của SVM')
plt.show()