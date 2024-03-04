import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("Top-Football-Leagues-Scorers2016-2019.csv")

plt.figure(figsize=(15, 9.5))

#La Liga - 2016
filter_df = df[(df["Country"] == "Spain") & (df["League"] == "La Liga") & (df["Year"] == 2016)]
top_goals = filter_df.nlargest(5, "Goals")


# So lan sut (gia tri x)
x1 = top_goals["Goals"].iloc[0]
# So lan sut trung muc tieu (gia tri y)
y1 = top_goals["OnTarget"].iloc[0]
# So ban thang (kich thuoc cua bong bong)
z1 = top_goals["Shots"].iloc[0]
# Ten cau thu 
name_1 = top_goals["Player Names"].iloc[0]

x2 = top_goals["Goals"].iloc[1]
y2 = top_goals["OnTarget"].iloc[1]
z2 = top_goals["Shots"].iloc[1]
name_2 = top_goals["Player Names"].iloc[1]

x3 = top_goals["Goals"].iloc[2]
y3 = top_goals["OnTarget"].iloc[2]
z3 = top_goals["Shots"].iloc[2]
name_3 = top_goals["Player Names"].iloc[2]

x4 = top_goals["Goals"].iloc[3]
y4 = top_goals["OnTarget"].iloc[3]
z4 = top_goals["Shots"].iloc[3]
name_4 = top_goals["Player Names"].iloc[3]

x5 = top_goals["Goals"].iloc[4]
y5 = top_goals["OnTarget"].iloc[4]
z5 = top_goals["Shots"].iloc[4]
name_5 = top_goals["Player Names"].iloc[4]

# Tạo điểm chú thích KHÔNG QUAN TRỌNG
plt.scatter(x1, y1, s=20, c="pink", marker="o", alpha=0.5)
plt.scatter(x2, y2, s=20, c="red", marker="o", alpha=0.5)
plt.scatter(x3, y3, s=20, c="cyan", marker="o", alpha=0.5)
plt.scatter(x4, y4, s=20, c="greenyellow", marker="o", alpha=0.5)
plt.scatter(x5, y5, s=20, c="orange", marker="o", alpha=0.5)


plt.scatter(x1, y1, s=z1*150, c="pink", marker="o", alpha=0.75)
plt.scatter(x2, y2, s=z2*150, c="red", marker="o", alpha=0.75)
plt.scatter(x3, y3, s=z3*150, c="cyan", marker="o", alpha=0.75)
plt.scatter(x4, y4, s=z4*150, c="greenyellow", marker="o", alpha=0.75)
plt.scatter(x5, y5, s=z5*150, c="orange", marker="o", alpha=0.75)



plt.text(x1, y1, f"{name_1} \n{z1} shots", fontsize=10, ha="center", va="center", fontweight="bold")
plt.text(x2, y2, f"{name_2} \n{z2} shots", fontsize=10, ha="center", va="center", fontweight="bold")
plt.text(x3, y3, f"{name_3} \n{z3} shots", fontsize=10, ha="center", va="center", fontweight="bold")
plt.text(x4, y4, f"{name_4} \n{z4} shots", fontsize=10, ha="center", va="center", fontweight="bold")
plt.text(x5, y5, f"{name_5} \n{z5} shots", fontsize=10, ha="center", va="center", fontweight="bold")


plt.title("Số bàn thắng và Số lần sút trúng mục tiêu của các cầu thủ hàng đầu giải đấu La Liga - 2016", fontsize=16, fontweight="bold")
plt.xlabel("Số bàn thắng (bàn thắng)", fontsize=14)
plt.ylabel("Số lần sút bóng trúng mục tiêu (lần)", fontsize=14)

plt.xticks(np.arange(10, 46, 5))
plt.yticks(np.arange(25, 91, 5)) 


plt.legend(title = "Tên cầu thủ:", labels=[name_1, name_2, name_3, name_4, name_5], title_fontsize=12, fontsize=12, loc="upper left")
plt.show()