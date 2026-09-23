# - Import Libraries
import streamlit as st
from PIL import Image

def run():
    st.html("""
        <h1 style="text-align:center">Weather Prediction</h1>
    """)

    st.markdown('---')

    st.subheader('About Project')
    st.write('### This Project Is Used To Predict Rain Using Today Weather Data')

    st.write('#### To Start Predict, Press the Sidebar Icon on Top Left & Choose Predict')

    st.html('<br>')

    image = Image.open('hero.jpg')
    st.image(image)
    
    st.html("""
    <div style="width: 100%; text-align: center;">
        <h2>Factors That Could Affect Weather</h2>
    </div>
    """)

    st.html('<br>')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("### Temperature")
        st.write("Temperature measurements throughout the day.")

    with col2:
        st.markdown("### Wind")
        st.write("Wind Speed & Directions")

    with col3:
        st.markdown("### Humidity & Pressure")
        st.write("Humidity and atmospheric pressure measurements.")
    with col4:
        st.markdown("### Rain & Cloud")
        st.write("Rain, Cloud Condition")



if __name__ == '__main__':
    run()