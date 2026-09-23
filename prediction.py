import pickle
import pandas as pd
import streamlit as st


with open('best_model.pkl', 'rb') as file_1:
  best_model = pickle.load(file_1)

def run():
  st.header('Weather Prediction Form')
  #============== WEATHER FORM ==============
  with st.form('Weather Prediction'):
    month = st.selectbox('Choose Month', ('1', '2', '3', '4', '5', '6',
                                         '7', '8', '9', '10', '11', '12'), help='Month in Numerical Order')
    
    location = st.text_input('Location', value='-')

    st.markdown('---')
    mintemp = st.number_input('Minimum Temperature During The Day', value=0, help='Lowest Temp Must be Less Than Highest Temp ')

    maxtemp = st.number_input('Highest Temperature During The Day', value=0)
    st.markdown('---')

    temp9am = st.number_input('Temp at 9am', value=0)

    temp3pm = st.number_input('Temp at 3pm', value=0)

    rainfall = st.number_input('Rainfall In MM', value=0)

    evaporation = st.number_input('Pan Evaporation (mm)', value=0)

    sunshine = st.slider('Hours of Bright Sunshine in the day', min_value=0, max_value=24)

    windgustdir = st.selectbox('Wind Direction', ('N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
                                             'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'))
    

    winddir9am = st.selectbox('Wind Direction at 9am', ('N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
                                             'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'))
    
    winddir3pm = st.selectbox('Wind Direction at 3pm', ('N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
                                             'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'))
    
    windspeed = st.number_input('Strongest Wind Gust Speed in km/h During The Day', value=0)
    
    windspeed9am = st.number_input('Strongest Wind Gust Speed in km/h at 9am', value=0)

    windspeed3pm = st.number_input('Strongest Wind Gust Speed in km/h at 3pm', value=0)

    humidity9am = st.slider('Air Humidity During 9am', min_value=0, max_value=100, value=50, help='Humidity (Percent)')

    humidity3pm = st.slider('Air Humidity During 3pm', min_value=0, max_value=100, value=50, help='Humidity (Percent)')

    pressure9am = st.number_input('Air Pressure at 9am: ', value=0.0, help='Atmospheric pressure (hpa) reduced to mean sea level', step=0.01)    

    pressure3pm = st.number_input('Air Pressure at 3pm: ', value=0.0, help='Atmospheric pressure (hpa) reduced to mean sea level', step=0.01)

    cloud9am = st.slider('Cloud Level at 9am', min_value=0, max_value=8, help='Fraction on Cloud obscuring the sky, Measured in Oktas (0-8)')

    cloud3pm = st.slider('Cloud Level at 3pm', min_value=0, max_value=8, help='Fraction on Cloud obscuring the sky, Measured in Oktas (0-8)')


    raintoday = st.radio('Is it Raining Today?', ('Yes', 'No'))


    st.markdown('---')
    submitted = st.form_submit_button('Predict')

#============== INFERENCE DATA ==============
  data_inf_dict = {
    'Month': month,
    'Location' : location,
    'MinTemp' : mintemp,
    'MaxTemp' : maxtemp,
    'Rainfall' :  rainfall,
    'Evaporation' : evaporation,
    'Sunshine' : sunshine,
    'WindGustDir' : windgustdir,
    'WindGustSpeed' : windspeed ,
    'WindDir9am' : winddir9am,
    'WindDir3pm' : winddir3pm,
    'WindSpeed9am' : windspeed9am,
    'WindSpeed3pm' : windspeed3pm,
    'Humidity9am' : humidity9am,
    'Humidity3pm' : humidity3pm,
    'Pressure9am' : pressure9am,
    'Pressure3pm' : pressure3pm,
    'Cloud9am' : cloud9am,
    'Cloud3pm' : cloud3pm,
    'Temp9am' : temp9am,
    'Temp3pm' : temp3pm,
    'RainToday' : raintoday, 
}
  data_inf = pd.DataFrame([data_inf_dict])
  st.dataframe(data_inf)

  if submitted:
    # - Logical Error Check
    if data_inf_dict['MinTemp'] >= data_inf_dict['MaxTemp']:
        st.error('Minimal Temp Cant Be Greater or Equal To Maximum Temp')
    else:
      y_pred_inf = best_model.predict(data_inf)

      if y_pred_inf == 1: # - Tomorrow Is Raining
        st.write('## Result: ')
        st.html('''
          <p style="font-size:40px">Its Raining Tomorrow</p>
          <p style="font-size:40px">Suggested Articles:</p> # - Articles
          <ul>
            <li>a href="https://wilderness-society.org/rain-its-importance-process-and-challenges/", target="_blank", style="text-decoration:none">Rain Importance And Its Challenges</a></li>
            <li><a href="https://resiliencehealthinc.com/blog/f/rainy-spring-heres-how-wet-weather-impacts-you%E2%80%94and-what-to-do", target="_blank", style="text-decoration:none">How Wet Weather Impacts You</a></li>
            <li><a href="https://www.nesdis.noaa.gov/about/k-12-education/atmosphere/what-makes-it-rain", target="_blank", style="text-decoration:none">What Makes it Rain</a></li>
            <li><a href="https://ncas.ac.uk/learn/what-causes-weather/", target="_blank", style="text-decoration:none">What Causes Weather</a></li>
          </ul>
           
        ''')
      else: # - Tomorrow Will not be Raining
        st.write('## Result: ')
        st.html('''
          <p style="font-size:40px">Its not Raining Tomorrow</p>
          <p style="font-size:40px">Suggested Articles:</p> # - Articles
          <ul>
            <li><a href="https://www.nesdis.noaa.gov/about/k-12-education/atmosphere/what-makes-it-rain", target="_blank", style="text-decoration:none">What Makes it Rain</a></li>
            <li><a href="https://ncas.ac.uk/learn/what-causes-weather/", target="_blank", style="text-decoration:none">What Causes Weather</a></li>
          </ul>
        ''')
if __name__ == '__main__':
  run()