import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#đọc dữ liệu 
df=pd.read_csv("Top-Football-Leagues-Scorers2016-2019.csv")
# print(df)


def bieudo_matdo(df):
    # Tính tổng số cầu thủ cho mỗi năm
    players_sum = df.groupby('Year')['Goals'].sum()
    # Thiết lập kiểu của seaborn
    sns.set(style="whitegrid")

    # Tạo subplot
    plt.figure(figsize=(12, 7))

    # Tạo đồ thị mật độ 
    plt.fill_between(players_sum.index, players_sum.values, color='skyblue', alpha=1)

    # Đặt kích thước cho tên trục và tiêu đề
    plt.xlabel("Năm", fontsize=16,fontweight="bold")
    plt.ylabel("Số bàn thắng ghi được(bàn thắng)", fontsize=16,fontweight="bold")
    plt.title("Số bàn thắng ghi được qua các năm", fontsize=16,fontweight="bold")

    # Chỉnh kích thước của các chỉ số trên trục x
    plt.tick_params(axis='x', labelsize=16)
    plt.xticks(players_sum.index, map(int, players_sum.index), fontsize=16)
    plt.yticks(fontsize=16)
    # Thêm đường kẻ ngang
    plt.grid(axis='y', linestyle='-', alpha=0.7)
    # Hiển thị biểu đồ
    plt.show()

bieudo_matdo(df)