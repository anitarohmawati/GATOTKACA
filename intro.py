import streamlit as st
import pandas as pd
st.write("Anita")


titanic = pd.read_csv("https://raw.githubusercontent.com/mofdac/-materi-das/main/01.%20Python%20for%20DA/titanic.csv")
#read json file dari data covid 


def main() : 
  st.write("Contoh dataframe")
  st.dataframe(titanic)

  st.write("Metrics")
  st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
  st.write("Menampilkan Dataframe dengan St AgGrid")
  AgGrid(titanic)
  st.table([x for x in range(1,5)])
if __name__ == "__main__" : 
  main()