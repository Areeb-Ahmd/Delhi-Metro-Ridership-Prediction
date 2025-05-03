import pandas as pd

def load_data():
    """Load the datasets for the Delhi Metro Ridership Prediction project."""
    delhi_metro_data = pd.read_csv('data/delhi_metro_final.csv')
    hourly_ridership_data = pd.read_csv('data/hourly_ridership.csv')
    
    return delhi_metro_data, hourly_ridership_data

def preprocess_data(df):
    """Preprocess the dataset for analysis and visualization."""
    # Example preprocessing steps
    df['Station Names'] = df['Station Names'].str.title()
    df['Daily_Ridership'] = df['Daily_Ridership'].astype(int)
    
    return df

def load_and_preprocess_data():
    """Load and preprocess the datasets."""
    delhi_metro_data, hourly_ridership_data = load_data()
    delhi_metro_data = preprocess_data(delhi_metro_data)
    
    return delhi_metro_data, hourly_ridership_data