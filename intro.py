import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Renewable Energy Investment", page_icon=":globe:")

# LOAD DATA ONCE
@st.experimental_singleton
def load_data_SSA():
    data = pd.read_excel(
        "SSH Rural Access to Electricity 2020.xlsx"
        # set as datetime instead of converting after the fact
    )

    return data


def main() : 
    st.markdown("<img src='header.png' />")
    st.markdown("### <div style='background-color: #63ebc6;border-radius: 10px; padding: 12px;color:#ffffff; line-height: .5;'> 2.2. Data Display Element </div>")
    st.title("Predicting Best Reneweable Energy Investment for Electrification Acceleration in Sub-Saharan Africa Rurals")
    df=load_data_SSA()
    st.dataframe(df)
    #st.bar_chart(df)


if __name__ == '__main__' : 
    main()