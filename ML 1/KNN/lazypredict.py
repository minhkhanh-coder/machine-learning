from lazypredict.Supervised import LazyClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
# Load dữ liệu
data = load_breast_cancer()
X, y = data.data, data.target
# Chia thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Sử dụng LazyPredict để tạo mô hình
clf = LazyClassifier()
models, predictions = clf.fit(X_train, X_test, y_train, y_test)
# In ra các mô hình và điểm số đánh giá
print(models)
print(predictions)