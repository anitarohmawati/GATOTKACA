import streamlit as st
import pandas as pd
st.write("Anita")

data=pd.read_excel("IRENA_RE_Public_Investment_July2022.xlsx").copy()
st.dataframe(data)