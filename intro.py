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
    )
    data = data[["Country Name",2020]]
    data = data[data[2020] < 50].sort_values(by=2020, ascending=True)
    data=data.reset_index()
    data.drop(['index'],axis=1, inplace=True)

    return data

def get_optimize(target, final_df):
    delta = (final_df.prediction - target).abs().nsmallest(5)
    opt = final_df.iloc[delta.index.to_list()]
    return opt.iloc[:,1:-1].reset_index(drop=True)

def main() : 
    sns.set_theme(style="whitegrid")
    st.image("header.png")
    reference_df = pd.read_csv('reference_df.csv')
   
    st.title("Predicting Best Renewable Energy Investment for Electrification Acceleration in Sub-Saharan Africa Rurals")
    tab1, tab2 = st.tabs(['Background','Optimizer'])
    tab1.subheader("The Needs of Electification Acceleration on Rural Area within the Sub-Saharan Africa Countries")
    tab2.subheader("Optimizing Renewable Energy Investment for Electrification Acceleration in Sub-Saharan Africa Region")

    with tab1:
        #columns :
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### In 2020, there were countries in SSA whose rural area were still below 50% in electricity access as follows:")
            data_africa=pd.read_excel("SSH Rural Access to Electricity 2020.xlsx")
   
            fig, ax = plt.subplots(figsize=(10, 10))

            sns.set(rc={'axes.facecolor':'black'})
            sns.set_color_codes("pastel")
            sns.barplot(x=2020, y="Country Name", data=data_africa)
            ax.legend(ncol=2, loc="lower right", frameon=True)
            ax.set( ylabel="",
            xlabel="Access to Electricity in Rural Area (%)")
            sns.despine(left=True, bottom=True)
            for p in ax.patches:
                width = p.get_width()    # get bar length
                ax.text(width + 1,       # set the text at 1 unit right of the bar
                    p.get_y() + p.get_height() / 2, # get Y coordinate + X coordinate / 2
                    '{:1.2f}'.format(width), # set variable to display, 2 decimals
                ha = 'left',   # horizontal alignment
                va = 'center')  # vertical alignment
            st.pyplot(fig)
            st.markdown("#### Imagine the positive impacts we can accrue should the donor from developed countries position their investment to promote the electrification acceleration on those areas!")
            st.markdown("#### Investment shall be aligned to renewable energy mixture and optimise the success rate!")
        with col2:
            st.markdown("#")
            st.markdown("##")
            st.markdown("#")
            df=load_data_SSA()
            st.dataframe(df)
    with tab2:
        col1, col2= st.columns([2,4])
        with col1:
            #Input (Typing)
            num_input = st.number_input('Insert the Target of Electrification Growth', min_value=0.0, max_value=4.5)
            click_me_btn = st.button('Predict')
        with col2:
            if click_me_btn:
                if num_input > 0.0:
                    st.dataframe(get_optimize(num_input, reference_df))
                else:
                    st.write('Input Error')

if __name__ == '__main__' : 
    main()