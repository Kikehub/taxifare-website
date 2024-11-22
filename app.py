import streamlit as st
import requests


'''
# Skibidi
'''

st.write('Welcome to the Skibidi')

d = st.date_input(
    "Date of Fare")

t = st.time_input('Time')
st.write('You are leaving on ', d, ' at ', t, '.')

st.write('Center of NY at 40.7 -74.0')
p_long = st.number_input('pickup longitude')
p_lat = st.number_input('pickup latitude')
d_long = st.number_input('dropoff longitude')
d_lat = st.number_input('dropoff latitude')

st.write('Pickup at ', p_long, ',', p_lat)
st.write('Dropoff at ', d_long, ',', d_lat)

passenger_count = int(st.number_input('Passengers :'))

st.write(passenger_count, 'passengers')

url = 'https://taxifare.lewagon.ai/predict'

datetimer = f'{d} {t}'

dictio = {
    'pickup_datetime': datetimer,
    'pickup_longitude': p_long,
    'pickup_latitude' : p_lat,
    'dropoff_longitude' : d_long,
    'dropoff_latitude' : d_lat,
    'passenger_count' : passenger_count
}

obj = requests.get(url, dictio).json()
st.write(obj)

pred = obj.get('fare')
st.write(pred)
'''
# TaxiFareModel front
'''
st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
