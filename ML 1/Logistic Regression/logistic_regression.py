import warnings
import numpy as np
import pandas as pd
from scipy import stats
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Tắt tất cả các cảnh báo
warnings.filterwarnings("ignore")

# Đọc tập dữ liệu từ file csv
df = pd.read_csv("./weatherAus.csv")
print("Kích thước dataframe dữ liệu thời tiết:", df.shape)

# Hiển thị tập dữ liệu
print(df.head())

# Tên các cột
col_names = df.columns
print(col_names)

# Thống kê cơ bản của mỗi cột
print(df.describe())

# Kiểm tra giá trị Null
print(df.count().sort_values())

# Loại bỏ các cột không cần thiết
df = df.drop(columns=['Sunshine','Evaporation','Cloud3pm','Cloud9am','Date'],axis=1)
print(df.shape)

# Loại bỏ các hàng chứa giá trị Null
df = df.dropna()
print(df.shape)

# Loại bỏ các giá trị ngoại lệ
z = np.abs(stats.zscore(df._get_numeric_data()))
print(z)
df = df[(z < 3).all(axis=1)]
print(df.shape)



# Chuẩn hóa dữ liệu
numerical = [var for var in df.columns if df[var].dtype=="float64"]
for col in numerical:
    df[col] = preprocessing.scale(df[col])
    
print(df.head())

# Chuyển Yes/No -> 1/0
df["RainToday"] = LabelEncoder().fit_transform(df["RainToday"])
df["RainTomorrow"] = LabelEncoder().fit_transform(df["RainTomorrow"])

# Xử lý dữ liệu phân loại
categorical = [var for var in df.columns if df[var].dtype=='object']
print("Number of categorical variables: ", len(categorical))
print(categorical)


categorical_columns = ['Location','WindGustDir', 'WindDir3pm', 'WindDir9am']

# Hiển thị các giá trị duy nhất trong từng cột phân loại
for col in categorical_columns:
    print(np.unique(df[col]))

# Tạo các biến giả tưởng (dummy variables)
df = pd.get_dummies(df, columns=categorical_columns)

# Đặt X là tất cả các đặc trưng
X = df.loc[:, df.columns != 'RainTomorrow']

# Đặt y là biến mục tiêu RainTomorrow
y = df.RainTomorrow

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Tách dữ liệu thành 5 phần và trộn để tránh thiên lệch
logReg = LogisticRegression()
logReg.fit(X_train, y_train)







# Dự đoán trên tập kiểm thử với mô hình đã được huấn luyện
y_pred = logReg.predict(X_test)

# Đánh giá mô hình
accuracy_score = accuracy_score(y_test, y_pred)
print("Độ chính xác của tập dữ liệu: {:.2f}".format(accuracy_score))

# Chọn ngẫu nhiên 100 điểm từ tập kiểm thử
random_indices = np.random.choice(len(X_test), size=100, replace=False)

# Biểu đồ điểm so sánh kết quả thực tế và dự đoán
plt.figure(figsize=(16, 5))
plt.scatter(range(100), y_test.iloc[random_indices], color="black", label="Thực tế")
plt.scatter(range(100), y_pred[random_indices], color="red", marker="x", label="Dự đoán")

plt.title("Biểu đồ so sánh Kết quả Thực tế và Dự đoán 'Ngày mai trời có mưa hay không?'", fontsize=15, fontweight="bold")
plt.xlabel("Số mẫu (mẫu)", fontsize=12)
plt.ylabel("Có mưa (1) / Không có mưa (0)", fontsize=12)
plt.legend(title="Kết quả", title_fontsize=12, fontsize=12)
plt.yticks([0, 1])
plt.show()
