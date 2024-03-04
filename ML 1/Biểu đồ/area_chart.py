import pandas as pd
import matplotlib.pyplot as plt

#đọc dữ liệu 
df=pd.read_csv("Top-Football-Leagues-Scorers2016-2019.csv")
# print(df)

def bieudo_area():
    # Chọn các giải đấu cần vẽ biểu đồ
    selected_leagues = ['La Liga', 'Serie A', 'Bundesliga', 'Premier League']

    # Lọc DataFrame theo giải đấu đã chọn
    filtered_df = df[df['League'].isin(selected_leagues)]

    # Nhóm theo 'Năm' và 'Giải đấu' và tính tổng số bàn thắng
    grouped_df = filtered_df.groupby(['Year', 'League'])['Goals'].sum().reset_index()

    # Pivot DataFrame để có 'Giải đấu' làm cột
    pivot_df = grouped_df.pivot(index='Year', columns='League', values='Goals')

    # Vẽ biểu đồ diện tích chồng lên nhau
    pivot_df.plot(kind='area', stacked=True, figsize=(10, 6))

    # Đặt tiêu đề và nhãn trục
    plt.title('Tổng số bàn thắng ở các giải đấu khác nhau qua các năm (2016-2019)', fontsize=16, fontweight="bold")
    plt.xlabel('Năm', fontsize=16, fontweight="bold")
    plt.ylabel('Tổng số bàn thắng (bàn thắng)', fontsize=16, fontweight="bold")

    # Bảng chú thích với kích thước nhỏ hơn
    legend = plt.legend(title='Giải đấu', loc='upper left', fontsize=12)
    legend.get_title().set_fontsize('8')  # Kích thước của tiêu đề bảng chú thích

    # Chỉnh kích thước của các chỉ số trên trục x và y
    plt.xticks(pivot_df.index, map(int, pivot_df.index), fontsize=16)
    plt.yticks(fontsize=16)

    # Hiển thị đường kẻ ngang
    plt.grid(axis='y', linestyle='-', alpha=0.7)

    # Hiển thị biểu đồ
    plt.show()

bieudo_area()