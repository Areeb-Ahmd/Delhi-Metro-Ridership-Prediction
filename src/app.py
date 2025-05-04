import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import os

# Inject custom CSS
def set_background_color_and_text():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: #ffffff !important;
            color: #000000 !important;
        }}
        h1, h2, h3, h4, h5, h6, p, span, label {{
            color: #000000 !important;
        }}
        /* Sidebar styling */
        section[data-testid="stSidebar"] {{
            background-color: #001f3f !important;
            color: #ffffff !important;
        }}
        section[data-testid="stSidebar"] * {{
            color: #ffffff !important;
        }}
        /* Dropdown styling */
        div[data-baseweb="select"] {{
            background-color: #003366 !important;
            color: #ffffff !important;
        }}
        div[data-baseweb="select"] > div {{
            background-color: #003366 !important;
            color: #ffffff !important;
        }}
        div[data-baseweb="select"] > div:hover {{
            background-color: #003366 !important; /* Darker navy on hover */
        }}
        /* Dropdown expanded menu styling */
        ul[role="listbox"] {{
            background-color: #003366 !important;
            color: #ffffff !important;
        }}
        ul[role="listbox"] > li {{
            background-color: #003366 !important;
            color: #ffffff !important;
        }}
        ul[role="listbox"] > li:hover {{
            background-color: #003366 !important; /* Darker navy on hover */
        }}
        /* Force button text to white and set background */
        .stButton > button {{
            color: white !important;
            background-color: #FF0000 !important;
            border: 2px solid #000000 !important;
            font-weight: bold !important;
            border-radius: 5px !important;
            padding: 10px 20px !important;
            font-size: 16px !important;
            cursor: pointer !important;
            transition: background-color 0.3s ease, color 0.3s ease !important;
        }}

        /* On hover */
        .stButton > button:hover {{
            background-color: #ffffff !important;
            color: white !important;
            border: 2px solid #000000 !important;
        }}

        /* Optional: slider labels and values to white */
        div[data-baseweb="slider"] label,
        div[data-baseweb="slider"] span {{
            color: white !important;
        }}

        /* Number input background (Latitude & Longitude boxes) */
        input[type="number"] {{
            background-color: #ccc !important;  /* Light grey */
            color: black !important;
            border: 1px solid #888 !important;
            border-radius: 5px !important;
        }}

        /* Custom ridership display box */
        .ridership-box {{
            background-color: #e0e0e0 !important;  /* Light grey */
            color: black !important;
            padding: 10px 10px;
            border: 1px solid #888 !important;
            border-radius: 8px;
            font-size: 34px;
            display: inline-block;
            margin-top: 3px;
        }}

        .metric-card {{
            border-radius: 12px;
            padding: 1.5rem 1rem 1rem 1rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
            text-align: center;
            color: #000000;
        }}
        .blue-bg {{ background-color: #e3f2fd; color: #000000; }}
        .green-bg {{background-color: #e8f5e9; color: #000000; }}
        .orange-bg {{ background-color: #fff3e0; color: #000000; }}
        .metric-caption {{
            font-size: 0.95rem;
            color: #555;
            margin-top: 0.5rem;
        }}
        .nav-card {{
            border-radius: 10px;
            background: #f5f5f5;
            padding: 1rem;
            margin: 0.5rem;
            text-align: center;
            box-shadow: 0 1px 4px rgba(0,0,0,0.03);
            color: #000000;
        }}
        .metric-number {{
            font-size: 2.2rem;
            font-weight: bold;
            color: #000000 !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# Example usage
set_background_color_and_text()

st.markdown(
    """
    <style>
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)


# Inject custom CSS to move the logo upwards
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] img {
        display: block;
        margin: 0 auto 10px auto !important;
        max-width: 100% !important;
        height: 75% !important;
        padding: 10px 0 10px 0 !important;
        background: none !important;
        border-radius: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Inject custom CSS to make the main content larger
st.markdown(
    """
    <style>
    /* Adjust the width of the main content */
    div.block-container {
        padding: 1rem 5rem; /* Adjust padding for better spacing */
        max-width: 95%;    /* Increase the width of the main content */
        margin-top: -50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load the dataset for key metrics
@st.cache_data
def load_data():
    return pd.read_csv(os.path.join('src', 'data', 'delhi_metro_final.csv'))

def load_model_comparison_data():
    """
    Load the model performance metrics from a CSV file.
    """
    try:
        df = pd.read_csv(os.path.join('src', 'data', 'model_performance_metrics.csv'))
        return df
    except FileNotFoundError:
        st.error("The file 'model_performance_metrics.csv' was not found. Please ensure it exists in the 'data' directory.")
        return pd.DataFrame()
    except UnicodeDecodeError:
        st.error("There was an issue decoding the file. Please ensure it is properly encoded.")
        return pd.DataFrame()

def get_local_time(timezone='Asia/Kolkata'):
    """
    Get the current time in the desired timezone.
    """
    server_time = datetime.now(pytz.utc)
    local_timezone = pytz.timezone(timezone)
    return server_time.astimezone(local_timezone)

def get_current_ridership(station_name, hourly_ridership, timezone='Asia/Kolkata'):
    """
    Calculate the ridership at the current time for a given station, adjusted for timezone.
    """
    now = get_local_time(timezone)
    current_hour = now.hour
    current_day = now.weekday()  # Monday=0, Sunday=6

    # Determine whether it's a weekday or weekend
    if current_day < 5:  # Weekday (Monday to Friday)
        ridership_column = f"Weekday_{current_hour}"
    else:  # Weekend (Saturday and Sunday)
        ridership_column = f"Weekend_{current_hour}"

    # Filter the hourly ridership DataFrame for the given station
    station_data = hourly_ridership[hourly_ridership['Station_Name'] == station_name]

    if not station_data.empty:
        current_ridership = station_data.iloc[0][ridership_column]
        return int(current_ridership)
    else:
        raise ValueError(f"Station '{station_name}' not found in the data.")

def plot_model_comparisons(df):
    """
    Plot comparisons of model performance metrics.
    """
    st.subheader("Model Performance Comparison")
    
    # RMSE Comparison
    st.write("### Root Mean Squared Error (RMSE) Comparison")
    fig, ax = plt.subplots()
    ax.bar(df['Model'], df['RMSE'], color='skyblue')
    ax.set_ylabel('RMSE')
    ax.set_title('Root Mean Squared Error (RMSE) Comparison')
    st.pyplot(fig)

    # MAE Comparison
    st.write("### Mean Absolute Error (MAE) Comparison")
    fig, ax = plt.subplots()
    ax.bar(df['Model'], df['MAE'], color='lightgreen')
    ax.set_ylabel('MAE')
    ax.set_title('Mean Absolute Error (MAE) Comparison')
    st.pyplot(fig)

    # R2_Score Comparison
    st.write("### R² Score Comparison")
    fig, ax = plt.subplots()
    ax.bar(df['Model'], df['R2_Score'], color='salmon')  # Updated column name
    ax.set_ylabel('R² Score')
    ax.set_title('R² Score Comparison')
    st.pyplot(fig)

def display_home():
    st.markdown("<h1 style='text-align: center; color: #001f3f; font-size: 3rem; font-weight: 900;'>Delhi Metro Ridership Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'><span style='font-size: 1.8rem; color: #333; font-weight: 600;'>Advanced Analytics & Predictive Insights for Urban Transit Planning</span></div>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 2px solid #001f3f;'>", unsafe_allow_html=True)
    # --- Key Metrics Section ---
    st.markdown("### Key Metrics")
    df = load_data()
    total_stations = df.shape[0]
    avg_daily_ridership = int(df['Daily_Ridership'].mean())
    highest_ridership_station = df.loc[df['Daily_Ridership'].idxmax(), 'Station Names']
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="metric-card blue-bg">🚇<br><span class="metric-number">{}</span><div class="metric-caption"><b>Total metro stations currently operational</b></div></div>'.format(total_stations), unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card green-bg">👥<br><span class="metric-number">{}</span><div class="metric-caption"></b>Avg. daily ridership across the network<b></div></div>'.format(avg_daily_ridership), unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card orange-bg">🏆<br><span class="metric-number">{}</span><div class="metric-caption"><b>Highest ridership station</b></div></div>'.format(highest_ridership_station), unsafe_allow_html=True)
    st.markdown("<hr style='border: 2px solid #001f3f;'>", unsafe_allow_html=True)

    # --- Navigation Section ---
    st.markdown("### Explore the Dashboard")
    nav1, nav2, nav3 = st.columns(3)
    with nav1:
        st.markdown('<div class="nav-card">📊<br><b>Ridership Analytics</b><br><span style="font-size:0.95rem;">View trends and patterns in metro ridership data.</span></div>', unsafe_allow_html=True)
    with nav2:
        st.markdown('<div class="nav-card">🗺️<br><b>Station Map</b><br><span style="font-size:0.95rem;">Explore the interactive map of all metro stations.</span></div>', unsafe_allow_html=True)
    with nav3:
        st.markdown('<div class="nav-card">🔮<br><b>Predict Ridership</b><br><span style="font-size:0.95rem;">Simulate and forecast ridership for any station.</span></div>', unsafe_allow_html=True)

# Sidebar navigation using streamlit-option-menu
with st.sidebar:
    st.image(os.path.join("src", "assets", "logo-passenger.png"))
    
    selected = option_menu(
        menu_title="NAVIGATION",
        options=["Home", "Map Visualization", "Data Insights", "Model Comparisons", "Real-Time Analysis", "Scenario Simulations"],
        icons=["house", "map", "bar-chart", "cpu", "clock", "activity"],
        default_index=0,
        orientation="vertical",
        styles={
            "container": {"padding": "0!important", "background-color": "#001f3f"},
            "icon": {"color": "white", "font-size": "22px"},
            "nav-link": {"color": "white", "font-size": "18px", "text-align": "left", "margin":"0 0 0 0"},
            "nav-link-selected": {"background-color": "#003366", "color": "#FFD93D"},
        }
    )
    st.markdown("---")
    st.markdown("### About")
    st.sidebar.info("This dashboard leverages advanced analytics and machine learning to deliver actionable insights and accurate ridership forecasts for the Delhi Metro network. Designed for planners, policymakers, and transit enthusiasts, it empowers data-driven decisions for urban mobility.")
    st.sidebar.markdown("---")
    st.markdown("### Contact Developer")
    st.sidebar.markdown(
        """
        Syed Areeb Ahmad<br>
        <a href="mailto:ahmad.syedareeb7@gmail.com" style="color:#FFD93D;">ahmad.syedareeb7@gmail.com</a>
        """,
        unsafe_allow_html=True
    )

# Main content based on selection
if selected == "Home":
    display_home()
elif selected == "Map Visualization":
    from components.map_visualization import display_map
    display_map()
elif selected == "Data Insights":
    from components.data_insights import show_data_insights
    show_data_insights()
elif selected == "Model Comparisons":
    from components.model_comparisons import compare_models
    compare_models()
elif selected == "Real-Time Analysis":
    from components.real_time_analysis import display_real_time_analysis
    display_real_time_analysis()
elif selected == "Scenario Simulations":
    from components.scenario_simulations import run_scenario_simulation
    run_scenario_simulation()
