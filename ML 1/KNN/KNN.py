import numpy as np
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Dữ liệu
area = [100, 120, 130, 155, 180, 200, 220, 240, 250, 260]
rooms = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6]
price = [250, 300, 320, 370, 400, 450, 500, 550, 600, 620]

# Chuyển đổi dữ liệu thành mảng 2D
X = np.column_stack((area, rooms))
y = np.array(price)

# Sử dụng k-NN để dự đoán giá trị
knn = KNeighborsRegressor(n_neighbors=3)
knn.fit(X, y)

# Dự đoán giá trị cho các căn nhà mới
new_data = np.array([[210, 4], [300, 2], [150, 3]])
predicted_prices = knn.predict(new_data)

# Hiển thị kết quả dự đoán
for i in range(len(new_data)):
    print(f"Dự đoán gía trị căn nhà {i+1}: ${predicted_prices[i]:,.2f}")

# Vẽ biểu đồ 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(area, rooms, price, c='blue', marker='o', label='Điểm dữ liệu')
ax.scatter(new_data[:, 0], new_data[:, 1], predicted_prices, c='red', marker='x', s=100, label='Dự đoán')
ax.set_xlabel('Diện tích (m2)')
ax.set_ylabel('Số phòng')
ax.set_zlabel('Giá trị (ngàn $)')
ax.legend()
plt.title('KNN Hồi quy: Dự đoán giá trị')
plt.show()
