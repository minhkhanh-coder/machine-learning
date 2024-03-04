import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs
# Tạo dữ liệu giả định với 2 cụm và một số điểm nhiễu (noise)
data,_= make_blobs(n_samples=16, centers=2, cluster_std=0.60, random_state=0)
data = np.concatenate([data, np.array([[3, 0], [4, 0], [5, 0], [6, 0]])])
# Sử dụng DBSCAN để phân cụm dữ liệu
dbscan = DBSCAN(eps=1.0, min_samples=3)
labels = dbscan.fit_predict(data)
#Tim core points và noise
core_samples_mask = np.zeros_like(labels, dtype=bool)
core_samples_mask[dbscan.core_sample_indices_] = True
noise_samples_mask = (labels == -1) & ~core_samples_mask
# Hiển thị dữ liệu với màu sắc cho core points, border points và noise
plt.scatter(data[core_samples_mask, 0], data[core_samples_mask, 1], c='blue', edgecolors='k',s=100, label='Core points')
plt.scatter(data[noise_samples_mask, 0], data[noise_samples_mask, 1], c='gray', marker='x', s=100, label='Noise')
# Về vòng tròn với bán kính là eps tại mỗi điểm dữ liệu
for i, (x, y) in enumerate(data):
    circle = plt.Circle((x, y), dbscan.eps, color='gray', fill=False, linestyle='dotted', alpha = 0.5)
    plt.gca().add_patch(circle)
    plt.text(x, y,f'{i+1}', color='red',ha='center',va='center')
plt.title("DBSCAN Clustering with eps={dbscan.eps}")
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()