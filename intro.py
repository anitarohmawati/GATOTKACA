import streamlit as st
import pandas as pd
st.write("Anita")


titanic = pd.read_excel("IRENA_RE_Public_Investment_July2022.xlsx")



def main() : 
  st.write("Contoh dataframe")
  st.dataframe(titanic)

  st.write("Metrics")

  st.write("Menampilkan Dataframe dengan St AgGrid")

  st.table([x for x in range(1,5)])
if __name__ == "__main__" : 
  main()