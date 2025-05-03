# Delhi Metro Ridership Prediction Dashboard

Welcome to the Delhi Metro Ridership Prediction Dashboard! This project aims to provide an interactive platform for visualizing and analyzing ridership data for the Delhi Metro system. The dashboard is built using Streamlit and integrates various components for data insights, model comparisons, real-time analysis, and scenario simulations.

## Project Structure

The project is organized as follows:

```
delhi-metro-dashboard
├── src
│   ├── app.py                     # Main entry point for the Streamlit dashboard
│   ├── components                  # Contains various visualization and analysis modules
│   │   ├── __init__.py
│   │   ├── map_visualization.py    # Interactive map of Delhi Metro stations
│   │   ├── data_insights.py        # Data insights visualizations
│   │   ├── model_comparisons.py    # Comparison of prediction models
│   │   ├── real_time_analysis.py    # Real-time ridership data display
│   │   ├── scenario_simulations.py  # Hypothetical station ridership predictions
│   │   └── optimization_insights.py # Analysis of peak hours and resource allocation
│   ├── assets                       # Contains assets for the dashboard
│   │   ├── metro_theme.css         # Custom CSS for metro-inspired theme
│   │   └── metro_logo.svg          # Logo for the Delhi Metro
│   └── utils                       # Utility functions for data loading and visualization
│       ├── __init__.py
│       ├── data_loader.py          # Functions to load and preprocess datasets
│       ├── model_utils.py          # Utility functions for model predictions
│       └── visualization_utils.py   # Helper functions for visualizations
├── data
│   ├── delhi_metro_final.csv       # Cleaned dataset with station information
│   └── hourly_ridership.csv        # Synthetic hourly ridership data
├── requirements.txt                # Required Python packages
├── README.md                       # Project documentation
└── .streamlit
    └── config.toml                # Configuration settings for the Streamlit app
```

## Features

- **Interactive Map**: Visualize the locations of Delhi Metro stations with real-time ridership data.
- **Data Insights**: Generate various visualizations such as pie charts, bar charts, and heatmaps to understand ridership trends.
- **Model Comparisons**: Compare the performance of different prediction models (XGBoost, Linear Regression, Ensemble) using metrics like RMSE, MAE, and R².
- **Real-Time Analysis**: Display current ridership data and hourly trends for selected stations.
- **Scenario Simulations**: Input hypothetical station data to predict ridership and visualize the results.

## Installation

To run the dashboard, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd delhi-metro-dashboard
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```
   streamlit run src/app.py
   ```

## Usage

Once the app is running, you can navigate through the various sections using the sidebar. Each component is designed to provide insights and visualizations related to the Delhi Metro ridership data.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Thank you for using the Delhi Metro Ridership Prediction Dashboard! Enjoy exploring the data and insights!