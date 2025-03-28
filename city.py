import streamlit as st
import json
import requests


st.title("Weather app 🌥️")
st.subheader("enter a city name ")

api_key = "9bdc5b38d8694d09b1c121938251403"

city = st.text_input("Enter a city name : ")

base_url = f"http://api.weatherapi.com/v1/current.json?key=9bdc5b38d8694d09b1c121938251403&q={city}&aqi=no"

# st.write(base_url)

if st.button('Display'):
    p = {
        "appid" : api_key,
        "q": city
    }


    respones = requests.get(base_url,params=p)
    if respones.status_code == 200:
        data = respones.json()



        pic = data["current"]['condition']['icon']

        pic = 'https:' + pic

        st.image(pic,width= 100)

        st.subheader(f"☁️Weather info on {city}")
        st.subheader(f"⏲️local data and time :{data['location']['localtime']}")
        st.write(f"🕛🔥Temperature in celsius:{data["current"]["temp_c"]}")
        st.write(f"🔥Temperature in fahrenheit:{data["current"] ["temp_f"]}")
        st.write(f'☁️ weather feels like :{data["current"][ "condition"]["text"]}')
        st.write(f'☁️ weather feels like :{data["current"]["wind_kph"]}')
        st.write(f'☁️ weather feels like :{data["current"]["humidity"]}')
        st.write(f'☁️ weather feels like :{data["current"]["uv"]}')
        st.write(f"location {data["location"]["region"]}")
    else:
        st.warning('pls enter a valid city name')
