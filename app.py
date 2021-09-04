import app2
import Tab1
import streamlit as st

PAGES = {"Prediction Module": app2,
         "Analytics": Tab1
        }
st. sidebar.title('Navigaton')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.main()