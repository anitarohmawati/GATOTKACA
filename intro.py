import streamlit as st 
import requests

def main() : 
  st.header('This is Header')
  st.subheader('This is SubHeader')
  st.markdown('# Rendering Markdown ')
  st.write('Some Phytagorean Equation : ')
  st.latex('c^2 = a^2+b^2')

from st_aggrid import AgGrid
#baca dataframe dari file csv 
titanic = pd.read_csv('https://raw.githubusercontent.com/mofdac/-materi-das/main/01.%20Python%20for%20DA/titanic.csv')
#read json file dari data covid 
st.dataframe(titanic)
if __name__ == '__main__' : 
  main()