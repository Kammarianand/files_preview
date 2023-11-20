import streamlit as st
import pandas as pd
st.header("preview of files ")
st.subheader("supports only csv and excel files")
data_file = st.file_uploader("upload your file",type=['csv','xlsx'])

if data_file is not None:
    if 'csv' in data_file.type:
        df = pd.read_csv(data_file)
    elif 'xlxs' in data_file.type:
        df = pd.read_excel(data_file)
    st.table(df)



