import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Top-Football-Leagues-Scorers2016-2019.csv")

# Điều kiện vòng tròn trong
filter_11 = df[(df["Year"] == 2016)]
filter_12 = df[(df["Year"] == 2017)]
filter_13 = df[(df["Year"] == 2018)]

# Vòng tròn trong (tổng số bàn thắng của tất cả các giải mỗi năm (2016 - 2018))
inpie_1 = filter_11["Goals"].sum()
inpie_2 = filter_12["Goals"].sum()
inpie_3 = filter_13["Goals"].sum()

inring = [inpie_1, inpie_2, inpie_3]

# Điều kiện vòng tròn ngoài - 5 giải
filter_21 = filter_11.groupby("League")["Goals"].sum().reset_index()
filter_22 = filter_12.groupby("League")["Goals"].sum().reset_index()
filter_23 = filter_13.groupby("League")["Goals"].sum().reset_index()

# Vòng tròn ngoài
# 1/3 -1
outpie_11 = filter_11["Goals"].iloc[0]
outpie_12 = filter_11["Goals"].iloc[1]
outpie_13 = filter_11["Goals"].iloc[2]
outpie_14 = filter_11["Goals"].iloc[3]
outpie_15 = filter_11["Goals"].iloc[4]

# 1/3 -2
outpie_21 = filter_12["Goals"].iloc[0]
outpie_22 = filter_12["Goals"].iloc[1]
outpie_23 = filter_12["Goals"].iloc[2]
outpie_24 = filter_12["Goals"].iloc[3]
outpie_25 = filter_12["Goals"].iloc[4]

# 1/3 - 3

outpie_31 = filter_13["Goals"].iloc[0]
outpie_32 = filter_13["Goals"].iloc[1]
outpie_33 = filter_13["Goals"].iloc[2]
outpie_34 = filter_13["Goals"].iloc[3]
outpie_35 = filter_13["Goals"].iloc[4]

outring = [outpie_11, outpie_12, outpie_13, outpie_14, outpie_15, outpie_21, outpie_22, outpie_23, outpie_24, outpie_25, outpie_31, outpie_32, outpie_33, outpie_34, outpie_35]

# Vẽ biểu đồ doughnut
fig, ax = plt.subplots()

# Vòng tròn trong
ax.pie(inring, labels=['2016', '2017', '2018'], autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.3, edgecolor='w'))

# Vòng tròn ngoài
ax.pie(outring, radius=0.7, colors=['red', 'green', 'blue', 'purple', 'orange', 'pink', 'lightblue', 'lightgreen', 'lightcoral', 'lightyellow', 'yellow', 'lightgray', 'lightpink', 'lightcyan', 'lightgreen'], 
       autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.3, edgecolor='w'))

# Hiển thị biểu đồ
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()