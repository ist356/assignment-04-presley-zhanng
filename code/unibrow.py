'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

# TODO Write code here to complete the unibrow.py
''
uploaded_file = st.file_uploader("Upload dataset.", type = ["csv", "xslx", "json"])

if uploaded_file is not None:
    ext = pl.get_file_extension(uploaded_file)
    df = pl.load_file(uploaded_file, ext)