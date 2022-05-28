# ---- Modules ------- 
import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Fruits List")

@st.experimental_memo(suppress_st_warning=True)
def skipComputation():
    # ---- Creating Dictionary ----
    _dic = { 'Name': ['Mango', 'Apple', 'Banana'],
            'Quantity': [45, 38, 90]}

    _df = pd.DataFrame(_dic)
    st.info("Only first time you will be seeing me!")
    return _df   

load = st.button('Load Data')

# --- Initialising SessionState ---
if "load_state" not in st.session_state:
    st.session_state.load_state = False

if load or st.session_state.load_state:
    st.session_state.load_state = True
    _df = skipComputation()
    st.write(_df)

    # ---- Plot types -------
    opt = st.radio('Plot type :',['Bar', 'Pie'])
    if opt == 'Bar':
        fig = px.bar(_df, x= 'Name',
                    y = 'Quantity',title ='Bar Chart')
        st.plotly_chart(fig)

    else:     
        fig = px.pie(_df,names = 'Name',
                    values = 'Quantity',title ='Pie Chart')
        st.plotly_chart(fig)
        