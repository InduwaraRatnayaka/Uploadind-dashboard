import requests
import streamlit as st
import pandas as pd

st.write("Induwara Ratnayaka")
st.title("Induwara's Weather Dashboard")
st.sidebar.write("Type here to search")
st.sidebar.header("Enter Location Details")
latitude = st.sidebar.number_input("Enter Latitude", value=52.52, step=0.01)
longitude = st.sidebar.number_input("Enter Longitude", value=13.41, step=0.01)


api_url = f"https://api.open-meteo.com/v1/forecast?latitude=6.9355&longitude=79.8487&current=temperature_2m,relative_humidity_2m,is_day,precipitation,wind_speed_10m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,uv_index_max"


response = requests.get(api_url)
weather_data = response.json()


if 'current' in weather_data:
    current_weather = weather_data['current']
    
    # st.write(f"Temperature: {current_weather['temperature']}°C")
    # st.write(f"Wind Speed: {current_weather['windspeed']} km/h")
    # st.write(f"Rain: {current_weather.get('rain', 'No data available')} mm")
else:
    st.error("Failed to retrieve weather data. Please check the location or try again later.")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", current_weather['temperature_2m'], "1.2 °F")
col2.metric("Wind", current_weather['wind_speed_10m'], "-8%")
col3.metric("Rain",current_weather['relative_humidity_2m'],"4%")

# if 'hourly' in weather_data:
#     hourly_data = weather_data['hourly']
    
    
#     wind_data = pd.DataFrame({
#         'Hour': list(range(len(hourly_data['wind_speed_10m']))),
#         'Wind Speed (km/h)': hourly_data['wind_speed_10m']
#     })
    
#     st.subheader("Hourly Wind Speed")
#     st.table(wind_data)

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://img.freepik.com/free-photo/cloud-forest-landscape_23-2151794692.jpg ");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
        """
        <style>
        .custom-table {
            color: black; 
        }
        </style>
        """, 
        unsafe_allow_html=True
)
import streamlit as st

option = st.sidebar.selectbox(
    "Select an option",
    ("Sunrise", "Sunset", "UV Index", "Max Temperature", "Min Temperature"),
)

st.write("You selected:", option)

daily_max_temp_df = pd.DataFrame(weather_data["daily"]["temperature_2m_max"],weather_data["daily"]["time"])
daily_min_temp_df = pd.DataFrame(weather_data["daily"]["temperature_2m_min"],weather_data["daily"]["time"])
daily_uv_df = pd.DataFrame(weather_data["daily"]["uv_index_max"],weather_data["daily"]["time"])
daily_suns_df = pd.DataFrame(weather_data["daily"]["sunset"],weather_data["daily"]["time"])
daily_sunr_df = pd.DataFrame(weather_data["daily"]["sunrise"],weather_data["daily"]["time"])

if option == "Max Temperature":
    st.line_chart(daily_max_temp_df)
elif option == "Min Temperature":
  st.line_chart(daily_min_temp_df)
elif option == "UV Index":
  st.line_chart(daily_uv_df)
elif option == "Sunset":
  st.line_chart(daily_suns_df)
else:
   st.line_chart(daily_sunr_df)

st.subheader("(Asia/Colombo)")
st.image("image.jpg")
st.video("https://www.youtube.com/watch?v=vPZNAgfh470")