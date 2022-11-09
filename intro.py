import streamlit as st
import pandas as pd
st.write("Anita")
x=st.slider("select anumber")
st.write("You selected",x)
df=pd.read_excel("mydata.xlsx")
st.write(df)

