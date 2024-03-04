import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Top-Football-Leagues-Scorers2016-2019.csv")

# Biểu đồ cột (Bar Chart)
def bar_chart():
    plt.figure(figsize=(12, 6))
    
    selected_columns = ["Player Names", "Goals"]

    df_top_scorers = df[selected_columns]
    total_goals_by_player = df_top_scorers.groupby("Player Names")["Goals"].sum()
    top_10_scorers = total_goals_by_player.nlargest(10)


    bars = plt.bar(top_10_scorers.index, top_10_scorers, color="#1f78b4")

    plt.xlabel("Cầu Thủ", fontsize=14)
    plt.ylabel("Số bàn thắng (bàn)", fontsize=14)
    plt.title("Top 10 cầu thủ ghi bàn nhiều nhất (2016-2019)", fontsize=16, fontweight="bold")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha="center", va="bottom")

    plt.grid(axis="y", linestyle="--", alpha=0.7)

    legend = plt.legend(["Số lần ghi bàn"], title="Chú thích", title_fontsize="12", fontsize="12")

    
    plt.show()

# Biểu đồ đường (Line Chart)
def line_chart():
    print("Chua lam")

# Biểu đồ tròn (Pie Chart)
def pie_chart():
    goals_column = "Goals"
    year_column = "Year"
    league_column = "League"

    df_2016 = df[df[year_column] == 2016]

    total_goals_2016 = df_2016[goals_column].sum()

    goals_by_league = df_2016.groupby(league_column)[goals_column].sum() / total_goals_2016 * 100

    plt.figure(figsize=(12, 7))
    plt.pie(goals_by_league, labels=goals_by_league.index, autopct="%1.1f%%", startangle=90, counterclock=False)

    plt.legend(title="Giải Đấu", bbox_to_anchor=(1, 0.5), title_fontsize=12, fontsize=12, loc="lower left")
    plt.title("Tỉ lệ Số bàn thắng theo các giải đấu (2016)", fontsize=16, fontweight="bold")

    plt.show()


# Biểu đồ điểm (Scatter Plot)
def scatter_plot():
    plt.figure(figsize=(11, 6))

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

    plt.title("Mối tương quan giữa Số trận đấu và Số bàn thắng của Laliga - TBN (2016-2018)", fontsize=16, fontweight='bold')
    plt.xlabel("Số trận đá (trận)", fontsize=14)
    plt.ylabel("Số bàn thắng (bàn)", fontsize=14)
    plt.legend(title = "Chú thích", labels = ["Năm 2016","Năm 2017", "Năm 2018"], title_fontsize=12, fontsize=12)
    plt.show()

# Biểu đồ bong bóng (Bubble Chart)
def bubble_chart():
    plt.figure(figsize=(15, 9.5))

    #La Liga - 2016
    filter_df = df[(df["Country"] == "Spain") & (df["League"] == "La Liga") & (df["Year"] == 2016)]
    top_goals = filter_df.nlargest(5, "Goals")

    x1 = top_goals["Goals"].iloc[0]
    y1 = top_goals["OnTarget"].iloc[0]
    z1 = top_goals["Shots"].iloc[0]
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

# Biểu đồ phân phối tần suất (Histogram)
def histogram():
    print("chua lam")


# Biểu đồ doughnut (Doughnut Chart)
def doughnut_chart():
    print("Chua lam")

# Biểu đồ vùng (Area Chart)
def area_chart():
    selected_leagues = ["La Liga", "Serie A", "Bundesliga", "Premier League"]
    filtered_df = df[df["League"].isin(selected_leagues)]

    grouped_df = filtered_df.groupby(["Year", "League"])["Goals"].sum().reset_index()
    pivot_df = grouped_df.pivot(index="Year", columns="League", values="Goals")
    pivot_df.plot(kind="area", stacked=True, figsize=(10, 6))

    plt.title("Tổng số bàn thắng ở các giải đấu khác nhau qua các năm (2016-2019)", fontsize=16, fontweight="bold")
    plt.xlabel("Năm", fontsize=14)
    plt.ylabel("Tổng số bàn thắng (bàn)", fontsize=14)

    legend = plt.legend(title="Giải đấu", loc="upper left", title_fontsize=12, fontsize=12)

    plt.xticks(pivot_df.index, map(int, pivot_df.index), fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(axis="y", linestyle="-", alpha=0.7)

    plt.show()

# Biểu đồ mật độ (Density Plot)
def density_plot():
    players_sum = df.groupby("Year")["Goals"].sum()
    sns.set(style="whitegrid")
    plt.figure(figsize=(12, 7))

    plt.fill_between(players_sum.index, players_sum.values, color="skyblue", alpha=1)

    plt.xlabel("Năm", fontsize=14)
    plt.ylabel("Số bàn thắng ghi được (bàn)", fontsize=14)
    plt.title("Tổng Số bàn thắng ghi được qua các năm (2016-2019)", fontsize=16,fontweight="bold")

    plt.tick_params(axis="x", labelsize=16)
    plt.xticks(players_sum.index, map(int, players_sum.index), fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(axis="y", linestyle="-", alpha=0.7)
    plt.legend(title = "Chú thích", labels=["Tổng Số bàn thắng"], title_fontsize=12, fontsize=12, loc="upper left")
    plt.show()

area_chart()