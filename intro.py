import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st
#import plotly.express as px 
import matplotlib.pyplot as plt
import seaborn as sns

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Renewable Energy Investment", page_icon=":globe:")

# LOAD DATA ONCE
@st.experimental_singleton
def load_data_SSA():
    data = pd.read_excel(
        "SSH Rural Access to Electricity 2020.xlsx"
        # set as datetime instead of converting after the fact
    )
    data=data[["Country Name", 2020]]
    return data


def main() : 
    sns.set_theme(style="whitegrid")
    st.image("header.png")
    st.title("Background")
    st.markdown("#### In 2020, there were countries in SSA whose rural area were still below 50% in electricity access as follows:")
    df=load_data_SSA()
    st.dataframe(df)
   
    fig = plt.subplots()
    plt.scatter(df['Country Name'],df[2020])
    st.pyplot(fig)
  
    st.markdown("#### Imagine the positive impacts we can accrue should the donor from developed countries position their investment to promote the electrification acceleration on those areas!")
   
    #st.bar_chart(df)
    st.title("Predicting Best Renewable Energy Investment for Electrification Acceleration in Sub-Saharan Africa Rurals")


if __name__ == '__main__' : 
    main()