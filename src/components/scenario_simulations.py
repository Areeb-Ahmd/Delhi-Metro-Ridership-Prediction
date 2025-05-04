import streamlit as st
import pandas as pd
import numpy as np
from utils.model_utils import load_model
import joblib
import os

# Load the trained models
xgb_model = load_model(os.path.join('src', 'models', 'xgb_model.pkl'))  

# Load the scaler
scaler = joblib.load(os.path.join('src', 'models', 'scaler.pkl'))
line_encoder = joblib.load(os.path.join('src', 'models', 'line_encoder.pkl'))

# Load the original dataset to calculate ridership thresholds
df = pd.read_csv(os.path.join('src', 'data', 'delhi_metro_data.csv'))
ridership_thresholds = (
    df['Daily_Ridership'].quantile(0.33),  # Low threshold
    df['Daily_Ridership'].quantile(0.67)  # High threshold
)

def categorize_ridership(prediction, thresholds):
    """
    Categorizes predicted ridership into Low, Medium, or High based on thresholds.

    Parameters:
    prediction (float): Predicted ridership value.
    thresholds (tuple): A tuple of two thresholds (low_threshold, high_threshold).

    Returns:
    str: Category of ridership ('Low', 'Medium', 'High').
    """
    low_threshold, high_threshold = thresholds

    if prediction <= low_threshold:
        return 'Low'
    elif prediction <= high_threshold:
        return 'Medium'
    else:
        return 'High'

def simulate_ridership(station_age, metro_line_encoded, distance_from_first_station, latitude, longitude, connectivity, station_density):
    features = np.array([[station_age, metro_line_encoded, distance_from_first_station, latitude, longitude, connectivity, station_density]])
    features_scaled = scaler.transform(features)
    xgb_prediction = xgb_model.predict(features_scaled)
    return xgb_prediction[0]

def display_simulation_results(xgb_pred):
    st.markdown("<hr style='border: 2px solid #001f3f;'>", unsafe_allow_html=True)
    st.subheader("Predicted Ridership")
    def format_pred(val):
        return f"{int(val):,}"
    xgb_category = categorize_ridership(xgb_pred, ridership_thresholds)
    category_colors = {
        'Low': '#FF6B6B',
        'Medium': '#FFD93D',
        'High': '#6BCB77'
    }
    category_icons = {
        'Low': '⬇️',
        'Medium': '⏺️',
        'High': '⬆️'
    }
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.markdown(
            f"""
            <div style='margin-bottom: 32px;'>
                <div style='font-size: 30px; font-weight: bold; color: black; margin-bottom: 24px;'>{format_pred(xgb_pred)} <span style='font-size:22px; font-weight:500;'>Passengers</span></div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            f"<div style='background-color: {category_colors[xgb_category]}; color: black; border-radius: 20px; padding: 8px 16px; margin-bottom: 8px; text-align: center; font-weight: bold;'>"
            f"{category_icons[xgb_category]} <span style='color:black;'>Ridership Category: {xgb_category}</span></div>",
            unsafe_allow_html=True)
        st.markdown(
            """
            <div style='background-color: #e3f0ff; color: black; border-radius: 20px; padding: 16px;'>
                <b>Ridership Categories:</b>
                <ul style='color: black;'>
                    <li><b>Low:</b> Below 33rd percentile of all stations</li>
                    <li><b>Medium:</b> Between 33rd and 67th percentile</li>
                    <li><b>High:</b> Above 67th percentile</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
    if xgb_pred < 0:
        st.warning("Predicted ridership is negative. Please check your input parameters.")

def run_scenario_simulation():
    # --- Professional header ---
    st.markdown(
        """
        <h1 style='font-size: 2.5rem; font-weight: 900; color: #001f3f; text-align:center; margin-bottom: 0.2em; margin-top: 0.5em;'>
            Delhi Metro Ridership Scenario Simulations
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<hr style='border: 2px solid #001f3f; margin-top: 0.5em; margin-bottom: 1.2em;'>", unsafe_allow_html=True)


    # Input section
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    st.header("Input Parameters")
    st.markdown("<span style='font-size:1.15rem; font-weight:700; color:#001f3f;'>Station Age (years)</span>", unsafe_allow_html=True)
    station_age = st.slider("", 0, 100, 10)

    line_options = {
        "Red Line": 0,
        "Yellow Line": 1,
        "Blue Line": 2,
        "Green Line": 3,
        "Violet Line": 4,
        "Airport Express": 5,
        "Magenta Line": 6,
        "Pink Line": 7,
        "Grey Line": 8,
        "Rapid Metro": 9,
        "Orange Line": 10
    }
    st.markdown("<div style='font-size: 1.3rem; font-weight: 700; margin-bottom: 0.5em; color: #001f3f;'>Select a Metro Line</div>", unsafe_allow_html=True)
    selected_line = st.selectbox("", list(line_options.keys()))
    metro_line_encoded = line_options[selected_line]

    st.markdown("<span style='font-size:1.15rem; font-weight:700; color:#001f3f;'>Distance from First Station (km)</span>", unsafe_allow_html=True)
    distance_from_first_station = st.slider("", 0.0, 50.0, 5.0)

    st.markdown("<span style='font-size:1.15rem; font-weight:700; color:#001f3f;'>Latitude</span>", unsafe_allow_html=True)
    latitude = st.number_input("", value=28.6139)

    st.markdown("<span style='font-size:1.15rem; font-weight:700; color:#001f3f;'>Longitude</span>", unsafe_allow_html=True)
    longitude = st.number_input("", value=77.2090)

    st.markdown("<span style='font-size:1.15rem; font-weight:700; color:#001f3f;'>Connectivity (number of lines)</span>", unsafe_allow_html=True)
    connectivity = st.slider("", 1, 10, 2)

    st.markdown(
        """
        <div style='margin-top:1.2em; margin-bottom:0.5em;'>
            <span style='font-size:1.15rem; font-weight:700; color:#001f3f;'>Station Density:</span>
            <div style='font-size:1.08rem; color:#222; margin-top:0.2em;'>
                Station Density refers to the number of metro stations within a certain radius (e.g., 2 km) of the selected station.<br>
                A higher value means the station is in a more densely connected area of the metro network.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    station_density = st.slider(
        "",
        min_value=0,
        max_value=10,
        value=1,
        step=1,
    )

    st.markdown("""
    <style>
    .centered-button-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 2.5em;
        margin-bottom: 1.5em;
        width: 100%;
    }
    div.stButton > button {
        background-color: #FFE066 !important;
        color: #001f3f !important;
        font-size: 1.15rem !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        padding: 0.7em 2.5em !important;
        border: 2px solid #001f3f !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        transition: background 0.2s, color 0.2s;
        margin: auto;
        display: block;
    }
    div.stButton > button:hover {
        background-color: #FFF9DB !important;
        color: #001f3f !important;
        border: 2px solid #001f3f !important;
    }
    </style>
    <div class="centered-button-container">
    """, unsafe_allow_html=True)
    button_clicked = st.button("🚇 Simulate Ridership")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)  # Close input container

    # --- Results Section ---
    if button_clicked:
        st.markdown('<div class="results-container">', unsafe_allow_html=True)
        xgb_pred = simulate_ridership(
            station_age, metro_line_encoded, distance_from_first_station,
            latitude, longitude, connectivity, station_density
        )
        display_simulation_results(xgb_pred)
        st.markdown('</div>', unsafe_allow_html=True)  

if __name__ == "__main__":
    run_scenario_simulation()