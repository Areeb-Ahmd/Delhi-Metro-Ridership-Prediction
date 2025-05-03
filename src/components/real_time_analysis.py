import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt

# Load the hourly ridership data
@st.cache_data
def load_hourly_data():
    data = pd.read_csv('data/hourly_ridership.csv')
    return data

# Function to display real-time ridership data for selected stations
def display_real_time_analysis():
    """
    Display real-time ridership data for selected stations.
    """
    st.markdown(
        """
        <h1 style='font-size: 3.2rem; font-weight: 900; color: #001f3f; margin-bottom: 0.2em;'>
            Real-Time Ridership Analysis
        </h1>
        <hr style='border: 2px solid #001f3f; margin-top: 0; margin-bottom: 2em;'>
        """,
        unsafe_allow_html=True
    )
    # Load data
    hourly_data = load_hourly_data()

    # Sort station names alphabetically
    stations = sorted(hourly_data['Station_Name'].unique())

    # Create the dropdown for station selection
    st.markdown(
        "<div style='font-size: 1.3rem; font-weight: 700; margin-bottom: 0.1em; color: #001f3f;'>Select a Station</div>",
        unsafe_allow_html=True
    )
    selected_station = st.selectbox("", stations)

    # Filter data for the selected station
    station_data = hourly_data[hourly_data['Station_Name'] == selected_station]

    # Display current ridership and current time
    current_hour = datetime.datetime.now().hour
    current_time_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    current_ridership = station_data[f'Weekday_{current_hour}'].values[0] if current_hour < 24 else 0
    st.subheader("Current Ridership and Time:")
    st.markdown(f'<div class="ridership-box">{current_ridership} Passengers</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="font-size: 1.8rem; margin-top: 0.5rem;">Current Time: <b>{current_time_str}</b></div>', unsafe_allow_html=True)

    # Plot hourly ridership trends
    st.markdown("<hr style='border: 2px solid #001f3f;'>", unsafe_allow_html=True)
    st.subheader("Hourly Ridership Trends")
    hours = list(range(24))
    station_row = station_data.iloc[0]
    weekday_ridership = [station_row[f'Weekday_{i}'] for i in hours]
    weekend_ridership = [station_row[f'Weekend_{i}'] for i in hours]

    plt.figure(figsize=(12, 6))
    plt.plot(hours, weekday_ridership, label='Weekday', color='blue')
    plt.plot(hours, weekend_ridership, label='Weekend', color='red')
    plt.title(f'Hourly Ridership Trends for {selected_station}')
    plt.xlabel('Hour of Day')
    plt.ylabel('Ridership')
    plt.xticks(hours)
    plt.legend()
    st.pyplot(plt)

# Call the function to display the real-time analysis
if __name__ == "__main__":
    display_real_time_analysis()