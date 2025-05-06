# Delhi Metro Ridership Prediction Dashboard

Welcome to the Delhi Metro Ridership Prediction Dashboard! This project provides an interactive platform for visualizing and analyzing ridership data for the Delhi Metro system. Built with Streamlit, it offers comprehensive analytics, real-time monitoring, and predictive capabilities for urban transit planning.

## Project Structure

```
delhi-metro-dashboard
├── src/
│   ├── app.py                     # Main Streamlit application entry point
│   ├── components/               # Dashboard components and visualizations
│   │   ├── __init__.py
│   │   ├── map_visualization.py   # Interactive metro station map
│   │   ├── data_insights.py       # Data analysis and visualizations
│   │   ├── model_comparisons.py   # ML model performance comparisons
│   │   ├── real_time_analysis.py  # Live ridership monitoring
│   │   ├── scenario_simulations.py # What-if analysis for ridership
│   │   └── optimization_insights.py # Peak hours and resource analysis
│   ├── utils/                    # Utility functions and helpers
│   │   ├── __init__.py
│   │   ├── data_loader.py        # Data loading and preprocessing
│   │   ├── model_utils.py        # ML model utilities
│   │   └── visualization_utils.py # Plotting and visualization helpers
│   └── assets/                   # Static assets
│       ├── metro_theme.css       # Custom styling
│       └── logo-passenger.png    # Application logo
├── data/                        # Data files
│   ├── delhi_metro_final.csv    # Processed metro station data
│   └── hourly_ridership.csv     # Time-series ridership data
├── requirements.txt             # Python dependencies
├── Procfile                    # Deployment configuration
├── runtime.txt                 # Python runtime specification
└── .streamlit/                 # Streamlit configuration
    └── config.toml            # App settings and theme
```

## Key Features

### 1. Interactive Dashboard
- Modern, responsive UI with custom styling
- Real-time data updates and visualizations
- Intuitive navigation with sidebar menu

### 2. Data Analytics
- Comprehensive ridership analysis
- Interactive visualizations (charts, graphs, heatmaps)
- Key performance metrics and statistics

### 3. Real-Time Monitoring
- Live ridership tracking by station
- Hourly and daily trend analysis
- Weekday vs weekend comparisons

### 4. Machine Learning Integration
- Multiple prediction models (XGBoost, Linear Regression, Ensemble)
- Model performance comparisons
- Automated model evaluation metrics

### 5. Scenario Planning
- What-if analysis for new stations
- Resource optimization insights


## Technical Implementation

### Frontend
- Built with Streamlit for rapid development and deployment
- Custom CSS for enhanced UI/UX
- Responsive design for various screen sizes

### Backend
- Python-based data processing
- Pandas for data manipulation
- Scikit-learn for machine learning models
- Matplotlib for visualizations

### Data Management
- Efficient data loading with caching
- Automated data preprocessing
- Error handling and validation

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd delhi-metro-dashboard
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run src/app.py
   ```

## Usage

1. **Home**: Overview of key metrics and navigation
2. **Map Visualization**: Interactive metro station map
3. **Data Insights**: Detailed ridership analysis
4. **Model Comparisons**: ML model performance metrics
5. **Real-Time Analysis**: Live ridership monitoring
6. **Scenario Simulations**: What-if analysis tools

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## Contact

For questions or support, please contact:
- Syed Areeb Ahmad
- Email: ahmad.syedareeb7@gmail.com


---

Thank you for using the Delhi Metro Ridership Prediction Dashboard! We hope it helps in making data-driven decisions for urban transit planning.