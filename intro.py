import streamlit as st
import pandas as pd



def main() : 
    st.write("Predicting Best Renewable Energy Investment on Sub-Saharan Countries for Electrification Acceleration")
    x=st.slider("select anumber")
    st.write("You selected",x)
    df=pd.read_excel("https://github.com/anitarohmawati/GATOTKACA/blob/ANITA/mydata.xlsx?raw=true")
    st.dataframe(df)
    st.line_chart(df)

if __name__ == '__main__' : 
    main()