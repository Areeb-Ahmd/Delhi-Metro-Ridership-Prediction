import folium
import pandas as pd
from folium.plugins import MarkerCluster, HeatMap
import streamlit as st
import streamlit.components.v1 as components
import os

def create_map(df):
    """
    Create an interactive map with markers, a heatmap layer, and metro lines.
    """
    # Create a base map centered on Delhi
    delhi_map = folium.Map(location=[28.6139, 77.2090], zoom_start=11, tiles='CartoDB positron')

    # Create a marker cluster
    marker_cluster = MarkerCluster().add_to(delhi_map)

    # Add markers for each metro station
    for idx, row in df.iterrows():
        popup_content = f"""
        <b>Station:</b> {row['Station Names']}<br>
        <b>Daily Ridership:</b> {row['Daily_Ridership']}<br>
        <b>Metro Line:</b> {row['Metro Line']}<br>
        <b>Opened:</b> {row['Opening_Year']}<br>
        <b>Distance from First Station:</b> {row['Dist. From First Station(km)']} km
        """

        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=folium.Popup(popup_content, max_width=300),
            tooltip=row['Station Names']
        ).add_to(marker_cluster)

    # Add metro lines to the map
    metro_lines = df.groupby('Metro Line')
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'yellow']  # Colors for different metro lines
    color_map = {line: colors[i % len(colors)] for i, line in enumerate(metro_lines.groups.keys())}

    for line, stations in metro_lines:
        line_coords = stations[['Latitude', 'Longitude']].values.tolist()
        folium.PolyLine(
            locations=line_coords,
            color=color_map[line],
            weight=4,
            opacity=0.7,
            tooltip=f"{line} Line"
        ).add_to(delhi_map)

    # Add a heatmap layer based on ridership
    heat_data = df[['Latitude', 'Longitude', 'Daily_Ridership']].values.tolist()
    HeatMap(heat_data, radius=15, blur=10, max_zoom=13).add_to(delhi_map)

    return delhi_map

def load_data(file_path):
    """
    Load the dataset containing metro station details.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        st.error(f"The file '{file_path}' was not found. Please ensure it exists in the 'data' directory.")
        return pd.DataFrame()

def display_map():
    """
    Display the pre-generated interactive map in the Streamlit app.
    """
    st.markdown(
        """
        <h1 style='font-size: 3.8rem; font-weight: 900; color: #001f3f; margin-bottom: 0.2em;'>
            Interactive Map of Delhi Metro Stations
        </h1>
        <hr style='border: 2px solid #001f3f; margin-top: 0; margin-bottom: 2em;'>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <p style='font-size: 1.8rem; color: #333; margin-bottom: 1.5em;'>
            Explore the Delhi Metro stations, their ridership, and metro lines.
        </p>
        """,
        unsafe_allow_html=True
    )

    # Path to the pre-generated map HTML file
    map_file_path = os.path.join('data', 'delhi_metro_map.html')

    try:
        # Read the HTML file and embed it in the Streamlit app
        with open(map_file_path, 'r', encoding='utf-8') as f:
            map_html = f.read()
        components.html(map_html, height=600, scrolling=True)
    except FileNotFoundError:
        st.error(f"The file '{map_file_path}' was not found. Please ensure it exists in the specified directory.")