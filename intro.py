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
        "SSH Rural Access to Electricity 2020.xlsx",
        # set as datetime instead of converting after the fact
    )

    return data


def main() : 
   
    st.title("Predicting Best Reneweable Energy Investment for Electrification Acceleration in Sub-Saharan Africa Rurals")
    c = alt.Chart(load_data_SSA()).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

    st.altair_chart(c, use_container_width=True)
if __name__ == '__main__' : 
    main()