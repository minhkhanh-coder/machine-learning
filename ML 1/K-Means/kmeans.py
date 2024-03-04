import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


# Tạo dữ liệu giả định với 3 cụm
data,_= make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)

# Sử dụng KMeans để phân cụm dữ liệu
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(data)
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# Về dữ liệu và các trung tâm cụm
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', edgecolors='k')
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200)
plt.title('K-Means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()