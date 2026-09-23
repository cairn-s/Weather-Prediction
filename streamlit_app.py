import streamlit as st
import eda as eda
import prediction as prediction

st.set_page_config(
  page_title='Weather Predict',
  layout='wide',
  initial_sidebar_state='collapsed'
)

page = st.sidebar.selectbox('Choose Page', ('Landing Page', 'Predict'))

if page == 'Landing Page':
    eda.run()
else:
    prediction.run()