import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Top-Football-Leagues-Scorers2016-2019.csv")
plt.figure(figsize=(10, 6))


filter_1 = df[(df["Country"] == "Spain") & (df["League"] == "La Liga") & (df["Year"] == 2016)]
filter_2 = df[(df["Country"] == "Spain") & (df["League"] == "La Liga") & (df["Year"] == 2017)]
filter_3 = df[(df["Country"] == "Spain") & (df["League"] == "La Liga") & (df["Year"] == 2018)]


x1 = filter_1["Matches_Played"]
y1 = filter_1["Goals"]

x2 = filter_2["Matches_Played"]
y2 = filter_2["Goals"]

x3 = filter_3["Matches_Played"]
y3 = filter_3["Goals"]


plt.scatter(x1, y1, c="blue", marker="o", alpha=0.75)
plt.scatter(x2, y2, c="red", marker="^", alpha=0.75)
plt.scatter(x3, y3, c="green", marker="s", alpha=0.75)

plt.title("Mối tương quan giữa số trận đấu và số bàn thắng của TBN (Laliga) (2016-2018)", fontsize=14, fontweight='bold')

plt.xlabel("Số trận đá (trận)", fontsize=14)
plt.ylabel("Số bàn thắng (bàn)", fontsize=14)
plt.legend(title = "Chú thích", labels = ["Năm 2016","Năm 2017", "Năm 2018"])
plt.show()