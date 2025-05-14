
# automl/main.py

import sys
from pathlib import Path
import streamlit.web.cli as stcli
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit.components.v1 import html
import os, sys


def main():
    # 模擬命令列輸入 streamlit run <本檔案絕對路徑>
    sys.argv = ["streamlit", "run", str(Path(__file__).resolve())]
    stcli.main()

# Streamlit
if __name__ == "__main__":
    import streamlit as st
    import pandas as pd
    import pycaret.classification as clf
    import pycaret.regression as reg
    import tempfile

    st.set_page_config(page_title="PyCaret 自動前處理與建模", layout="wide")
    st.title("📊 PyCaret 自動前處理與建模介面")

    # (0) 選擇任務類型
    mode = st.radio("選擇任務類型", ["分類 (Classification)", "回歸 (Regression)"])

    # (1) 上傳 CSV 檔
    uploaded_file = st.file_uploader("上傳 CSV 檔案", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.subheader("📄 原始資料（前10筆）")
        st.dataframe(df.head(10))

        # 選擇目標欄位
        target = st.selectbox("選擇目標變數欄位", df.columns)

        # # (2) 前處理選項
        # st.subheader("⚙️ 前處理選項")
        # normalize = st.checkbox("標準化 (normalize)")
        # remove_outliers = st.checkbox("移除離群值 (remove_outliers)")
        # multicollinearity = st.checkbox("移除多重共線性 (remove_multicollinearity)")
        # fix_imbalance = st.checkbox("平衡類別樣本 (fix_imbalance)") if "分類" in mode else False

        if st.button("開始前處理與建模"):
            st.info("正在進行前處理與模型比較，請稍候...")

            with tempfile.TemporaryDirectory() as tmpdirname:
                if "分類" in mode:
                    module = clf
                else:
                    module = reg

                module.setup(data=df, target=target, session_id=123,
                            # normalize=normalize,
                            # remove_outliers=remove_outliers,
                            # remove_multicollinearity=multicollinearity,
                            # fix_imbalance=fix_imbalance if "分類" in mode else False,
                            html=False, verbose=False)
                best_model = module.compare_models()
                X_processed = module.get_config("X")
                y_processed = module.get_config("y")
                results = module.pull()

            # (3) 顯示前處理後資料
            st.subheader("🧹 前處理後的資料（前10筆）")
            st.dataframe(pd.concat([X_processed, y_processed], axis=1).head(10))

            # (4) 模型結果與圖示
            st.subheader("🤖 最佳模型比較結果")
            st.dataframe(results)

            st.subheader("📈 最佳模型效能視覺化")
            if "分類" in mode:
                # 顯示混淆矩陣 (逆向轉換標籤)
                module.plot_model(best_model, plot='confusion_matrix', display_format='streamlit',
                                  plot_kwargs = {'classes' : module.get_config('pipeline').steps[0][1].transformer.classes_})

            else:
                module.plot_model(best_model, plot='error', display_format='streamlit')
