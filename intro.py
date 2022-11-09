
import streamlit as st
import pandas as pd
st.write("Anita")
x=st.slider("select anumber")
st.write("You selected",x)
df=pd.read_excel("https://github.com/anitarohmawati/GATOTKACA/blob/ANITA/mydata.xlsx")
st.line_chart(df)

