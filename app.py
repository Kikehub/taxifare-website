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

pred = obj.get('fare de Victor le gros boloss')
st.write(pred)
