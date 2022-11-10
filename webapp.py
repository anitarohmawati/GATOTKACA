
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
    
    data = data[data[2020] < 50].sort_values(by=2020, ascending=True)
    return data

def get_optimize(target, final_df):
    delta = (final_df.prediction - target).abs().nsmallest(5)
    opt = final_df.iloc[delta.index.to_list()]
    return opt.iloc[:,1:-1].reset_index(drop=True)

def main() :

    df = load_data_SSA()
    reference_df = pd.read_csv('reference_df.csv')
    
    st.image("header.png")
    st.title("Background")
    
    tab1, tab2 = st.tabs(['Background','Optimizer'])
    tab1.subheader("The Needs of Electification on Sub-Sahara Africa")
    tab2.subheader("Optimizing Renewable Energy Investment for Electrification Acceleration in Sub-Saharan Africa Region")
    
    with tab1:
        #columns :
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### In 2020, there were countries in SSA whose rural area were still below 50% in electricity access as follows:")
            st.markdown("#### Imagine the positive impacts we can accrue should the donor from developed countries position their investment to promote the electrification acceleration on those areas!")

        with col2:
            st.dataframe(df)
    with tab2:
        col1, col2= st.columns([2,4])
        with col1:
            #Input (Typing)
            num_input = st.number_input('Insert the Target of Electrification Growth', min_value=0.0, max_value=4.5)
            click_me_btn = st.button('Click Me')
        with col2:
            if click_me_btn:
                if num_input > 0.0:
                    st.dataframe(get_optimize(num_input, reference_df))
                else:
                    st.write('Input Error')

    
if __name__ == '__main__' : 
    main()
