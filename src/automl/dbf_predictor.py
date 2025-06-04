import sys
from pathlib import Path
import streamlit.web.cli as stcli
import os


def main():
    # 模擬命令列輸入 streamlit run <本檔案絕對路徑>
    sys.argv = ["streamlit", "run", str(Path(__file__).resolve())]
    stcli.main()

# Streamlit
if __name__ == "__main__":
    import streamlit as st
    import pandas as pd
    from matplotlib import pyplot as plt
    from matplotlib.font_manager import FontProperties

    # 微軟正黑體（Windows）
    font_path = "微軟正黑體.ttf"
    font_prop = FontProperties(fname=font_path)

    # 佈局
    st.set_page_config(layout="wide")

    # 縮短上方的留白
    st.markdown("""
    <style>
    header.stAppHeader {
        background-color: transparent;
    }
    section.stMain .block-container {
        padding-top: 1rem;
        z-index: 1;
    }
    </style>""", unsafe_allow_html=True)
    

    # 標題
    st.title("2025 年端午節旅運人數預測")
    st.divider()

    cols = st.columns([0.2, 1, 1, 1, 0.2])

    # 預測目標的起站
    cols[1].subheader("預測起站")
    start_station = cols[1].selectbox(
        "請選擇待預測的起站",
        options=[
            "臺北",
            "臺中",
            "高雄",
            "臺南",
            "基隆",
            "花蓮",
            "臺東",
            "宜蘭",
        ],
    )

    # 預測目標的結束站
    cols[2].subheader("預測迄站")
    end_station = cols[2].selectbox(
        "請選擇待預測的迄站",
        options=[
            "臺北",
            "臺中",
            "高雄",
            "臺南",
            "基隆",
            "花蓮",
            "臺東",
            "宜蘭",
        ],
    )

    # 要預測的時間
    cols[3].subheader("預測日期")
    target_date = cols[3].date_input(
        "請選擇待預測的日期",
        value=pd.to_datetime("2025-05-29"),
        min_value=pd.to_datetime("2025-05-29"),
        max_value=pd.to_datetime("2025-06-03"),
    )

    # 加一點間隔
    st.markdown("<br>", unsafe_allow_html=True)

    # 確定按鈕
    cols = st.columns([0.2, 3, 0.2])

    if cols[1].button("確定", key="confirm_button", use_container_width=True):
        # 顯示預測結果
        cols = st.columns([0.2, 1, 1, 1, 0.2])

        # 歷史端午節日期
        history_dates_2020 = [
            '2020-06-24',
            '2020-06-25',
            '2020-06-26',
            '2020-06-27',
            '2020-06-28',
            '2020-06-29',
        ]

        history_dates_2021 = [
            '2021-06-11',
            '2021-06-12',
            '2021-06-13',
            '2021-06-14',
            '2021-06-15',
        ]

        history_dates_2022 = [
            '2022-06-02',
            '2022-06-03',
            '2022-06-04',
            '2022-06-05',
            '2022-06-06',
        ]

        history_dates_2023 = [
            '2023-06-21',
            '2023-06-22',
            '2023-06-23',
            '2023-06-24',
            '2023-06-25',
            '2023-06-26',
        ]

        history_date_2024 = [
            '2024-06-09',
            '2024-06-10',
            '2024-06-11',
            '2024-06-12',
            '2024-06-13',
        ]

        this_year_holiday = [
            '2025-05-29',
            '2025-05-30',
            '2025-05-31',
            '2025-06-01',
            '2025-06-02',
        ]
        
        print(target_date)
        target_date_str = target_date.strftime('%Y-%m-%d')

        if target_date_str == '2025-05-29':
            day_order = '一'
            # ---
            # 取得 2024 年全部資料(加上絕對路徑)
            data_2024 = pd.read_csv(os.path.join(".", 'day_sum_20240609.csv'))
            
            # 取得 2024 年的起迄站運量
            print(data_2024.head())
            data_2024_value = data_2024.loc[data_2024['起站'] == start_station, end_station].values[0]
            print(data_2024_value)
            
            # ---
            # 取得 2023 年全部資料
            data_2023 = pd.read_csv(os.path.join(".", 'day_sum_20230621.csv'))
            
            # 取得 2023 年的起迄站運量
            print(data_2023.head())
            data_2023_value = data_2023.loc[data_2023['起站'] == start_station, end_station].values[0]
            print(data_2023_value)
            
            # ---
            # 取得 2022 年全部資料
            data_2022 = pd.read_csv(os.path.join(".", 'day_sum_20220602.csv'))
            
            # 取得 2022 年的起迄站運量
            print(data_2022.head())
            data_2022_value = data_2022.loc[data_2022['起站'] == start_station, end_station].values[0]
            print(data_2022_value)
            
            # ---
            # 取得 2021 年全部資料
            data_2021 = pd.read_csv(os.path.join(".", 'day_sum_20210611.csv'))
            
            # 取得 2021 年的起迄站運量
            print(data_2021.head())
            data_2021_value = data_2021.loc[data_2021['起站'] == start_station, end_station].values[0]
            print(data_2021_value)
            
            # ---
            # 取得 2020 年全部資料
            data_2020 = pd.read_csv(os.path.join(".", 'day_sum_20200624.csv'))
            
            # 取得 2020 年的起迄站運量
            print(data_2020.head())
            data_2020_value = data_2020.loc[data_2020['起站'] == start_station, end_station].values[0]
            print(data_2020_value)
            
            # 預測結果
            data_2025_value = (
                2.4 * data_2024_value + 1.1 * data_2023_value + 0.4 * data_2022_value + 0.0 * data_2021_value + 0.1 * data_2020_value) / 4
            
            print('***' + str(data_2025_value))
        
        if target_date_str == '2025-05-30':
            day_order = '一'
            # ---
            # 取得 2024 年全部資料(加上絕對路徑)
            data_2024 = pd.read_csv(os.path.join(".", 'day_sum_20240610.csv'))
            
            # 取得 2024 年的起迄站運量
            print(data_2024.head())
            data_2024_value = data_2024.loc[data_2024['起站'] == start_station, end_station].values[0]
            print(data_2024_value)
            
            # ---
            # 取得 2023 年全部資料
            data_2023 = pd.read_csv(os.path.join(".", 'day_sum_20230622.csv'))
            
            # 取得 2023 年的起迄站運量
            print(data_2023.head())
            data_2023_value = data_2023.loc[data_2023['起站'] == start_station, end_station].values[0]
            print(data_2023_value)
            
            # ---
            # 取得 2022 年全部資料
            data_2022 = pd.read_csv(os.path.join(".", 'day_sum_20220603.csv'))
            
            # 取得 2022 年的起迄站運量
            print(data_2022.head())
            data_2022_value = data_2022.loc[data_2022['起站'] == start_station, end_station].values[0]
            print(data_2022_value)
            
            # ---
            # 取得 2021 年全部資料
            data_2021 = pd.read_csv(os.path.join(".", 'day_sum_20210612.csv'))
            
            # 取得 2021 年的起迄站運量
            print(data_2021.head())
            data_2021_value = data_2021.loc[data_2021['起站'] == start_station, end_station].values[0]
            print(data_2021_value)
            
            # ---
            # 取得 2020 年全部資料
            data_2020 = pd.read_csv(os.path.join(".", 'day_sum_20200625.csv'))
            
            # 取得 2020 年的起迄站運量
            print(data_2020.head())
            data_2020_value = data_2020.loc[data_2020['起站'] == start_station, end_station].values[0]
            print(data_2020_value)
            
            # 預測結果
            data_2025_value = (
                2.4 * data_2024_value + 1.1 * data_2023_value + 0.4 * data_2022_value + 0.0 * data_2021_value + 0.1 * data_2020_value) / 4
            
            print('***' + str(data_2025_value))
        
        if target_date_str == '2025-05-31':
            day_order = '二'
            # ---
            # 取得 2024 年全部資料
            data_2024 = pd.read_csv(os.path.join(".", 'day_sum_20240611.csv'))
            
            # 取得 2024 年的起迄站運量
            print(data_2024.head())
            data_2024_value = data_2024.loc[data_2024['起站'] == start_station, end_station].values[0]
            print(data_2024_value)
            
            # ---
            # 取得 2023 年全部資料
            data_2023 = pd.read_csv(os.path.join(".", 'day_sum_20230623.csv'))
            
            # 取得 2023 年的起迄站運量-1
            print(data_2023.head())
            data_2023_value_1 = data_2023.loc[data_2023['起站'] == start_station, end_station].values[0]
            print(data_2023_value_1)

            data_2023 = pd.read_csv(os.path.join(".", 'day_sum_20230624.csv'))
            
            # 取得 2023 年的起迄站運量-2
            print(data_2023.head())
            data_2023_value_2 = data_2023.loc[data_2023['起站'] == start_station, end_station].values[0]
            print(data_2023_value_2)
            
            data_2023_value = (data_2023_value_1 + data_2023_value_2) / 2

            # ---
            # 取得 2022 年全部資料
            data_2022 = pd.read_csv(os.path.join(".", 'day_sum_20220605.csv'))
            
            # 取得 2022 年的起迄站運量
            print(data_2022.head())
            data_2022_value = data_2022.loc[data_2022['起站'] == start_station, end_station].values[0]
            print(data_2022_value)
            
            # ---
            # 取得 2021 年全部資料
            data_2021 = pd.read_csv(os.path.join(".", 'day_sum_20210614.csv'))
            
            # 取得 2021 年的起迄站運量
            print(data_2021.head())
            data_2021_value = data_2021.loc[data_2021['起站'] == start_station, end_station].values[0]
            print(data_2021_value)
            
            # ---
            # 取得 2020 年全部資料
            data_2020 = pd.read_csv(os.path.join(".", 'day_sum_20200628.csv'))
            
            # 取得 2020 年的起迄站運量
            print(data_2020.head())
            data_2020_value = data_2020.loc[data_2020['起站'] == start_station, end_station].values[0]
            print(data_2020_value)
            
            # 預測結果
            data_2025_value = (
                2.4 * data_2024_value + 1.1 * data_2023_value + 0.4 * data_2022_value + 0.0 * data_2021_value + 0.1 * data_2020_value) / 4       
        
        if target_date_str == '2025-06-01':
            day_order = '三'
            # ---
            # 取得 2024 年全部資料
            data_2024 = pd.read_csv(os.path.join(".", 'day_sum_20240612.csv'))
            
            # 取得 2024 年的起迄站運量
            print(data_2024.head())
            data_2024_value = data_2024.loc[data_2024['起站'] == start_station, end_station].values[0]
            print(data_2024_value)
            
            # ---
            # 取得 2023 年全部資料
            data_2023 = pd.read_csv(os.path.join(".", 'day_sum_20230625.csv'))
            
            # 取得 2023 年的起迄站運量
            print(data_2023.head())
            data_2023_value = data_2023.loc[data_2023['起站'] == start_station, end_station].values[0]
            print(data_2023_value)
            
            # ---
            # 取得 2022 年全部資料
            data_2022 = pd.read_csv(os.path.join(".", 'day_sum_20220605.csv'))
            
            # 取得 2022 年的起迄站運量
            print(data_2022.head())
            data_2022_value = data_2022.loc[data_2022['起站'] == start_station, end_station].values[0]
            print(data_2022_value)
            
            # ---
            # 取得 2021 年全部資料
            data_2021 = pd.read_csv(os.path.join(".", 'day_sum_20210614.csv'))
            
            # 取得 2021 年的起迄站運量
            print(data_2021.head())
            data_2021_value = data_2021.loc[data_2021['起站'] == start_station, end_station].values[0]
            print(data_2021_value)
            
            # ---
            # 取得 2020 年全部資料
            data_2020 = pd.read_csv(os.path.join(".", 'day_sum_20200628.csv'))
            
            # 取得 2020 年的起迄站運量
            print(data_2020.head())
            data_2020_value = data_2020.loc[data_2020['起站'] == start_station, end_station].values[0]
            print(data_2020_value)
            
            # 預測結果
            data_2025_value = (
                2.4 * data_2024_value + 1.1 * data_2023_value + 0.4 * data_2022_value + 0.0 * data_2021_value + 0.1 * data_2020_value) / 4
        
        # 繪圖
        cols = st.columns([0.5, 1, 0.5])
        with cols[1]:
            st.markdown(f"### 端午節假期運量 (第{day_order}天)")
            st.markdown(f"起站: {start_station}，迄站: {end_station}，日期: {target_date_str}")
            
            fig, ax = plt.subplots(figsize=(10, 5))
            
            # 指定 bar 顏色，最後一個設為紅色
            values = [data_2020_value, data_2021_value, data_2022_value, data_2023_value, data_2024_value, data_2025_value]
            colors = ['blue'] * (len(values) - 1) + ['red']
            
            # 在長條圖中的每個長條上加上數值標籤
            for i, value in enumerate(values):
                ax.text(i, value + 0.05 * max(values), str(int(value)), ha='center', va='bottom', fontproperties=font_prop)
            
            # 圖的 y 軸上界為最大值再加 20%
            ax.set_ylim(0, max(values) * 1.2)
            
            ax.bar(x=['2020', '2021', '2022', '2023', '2024', '2025'], height=values, color=colors)
            ax.set_title(f"歷年端午節假期運量 (第{day_order}天)", fontproperties=font_prop)
            ax.set_xlabel("年份", fontproperties=font_prop)
            ax.set_ylabel("運量", fontproperties=font_prop)
            ax.set_xticks(['2020', '2021', '2022', '2023', '2024', '2025'])
            ax.set_xticklabels(['2020', '2021', '2022', '2023', '2024', '2025(預測)'], fontproperties=font_prop)
            ax.grid()
            
            st.pyplot(fig, clear_figure=True)