
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

# Streamlit 程式
if __name__ == "__main__":
    import streamlit as st
    
    st.set_page_config(layout="wide")
    st.title("📊 Data Profiling")

    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success("✅ Uploaded successfully!")
            
            st.subheader("📄 Data Review")
            st.dataframe(df.head())

            with st.spinner("🔍 Generating the report. Please waiting..."):
                profile = ProfileReport(df, explorative=True)
                html_report = profile.to_html()

            st.subheader("📋 Profiling Report")
            html(html_report, height=1000, scrolling=True)
            
        except Exception as e:
            st.error(f"❌ Error: {e}")
            st.warning("Please upload a valid CSV file.")
    else:
        st.info("Please upload a CSV file to get started.")
