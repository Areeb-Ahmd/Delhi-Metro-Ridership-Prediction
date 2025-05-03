import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_daily_ridership_distribution(df):
    plt.figure(figsize=(12, 6))
    sns.histplot(df['Daily_Ridership'], bins=30, kde=True, color='skyblue')
    plt.title('Daily Ridership Distribution')
    plt.xlabel('Daily Ridership')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.tight_layout()
    return plt

def plot_ridership_by_station_age(df):
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x='Station_Age', y='Daily_Ridership', hue='Metro Line', data=df, palette='viridis', s=100, alpha=0.7)
    plt.title('Ridership by Station Age')
    plt.xlabel('Station Age (years)')
    plt.ylabel('Daily Ridership')
    plt.grid(True)
    plt.tight_layout()
    return plt

def plot_ridership_by_distance(df):
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x='Dist. From First Station(km)', y='Daily_Ridership', hue='Metro Line', data=df, palette='viridis', s=100, alpha=0.7)
    plt.title('Ridership by Distance from First Station')
    plt.xlabel('Distance from First Station (km)')
    plt.ylabel('Daily Ridership')
    plt.grid(True)
    plt.tight_layout()
    return plt

def plot_model_comparison(metrics):
    plt.figure(figsize=(10, 6))
    models = list(metrics.keys())
    rmse_values = [metrics[model]['RMSE'] for model in models]
    mae_values = [metrics[model]['MAE'] for model in models]
    
    x = range(len(models))
    
    plt.bar(x, rmse_values, width=0.4, label='RMSE', color='b', align='center')
    plt.bar([p + 0.4 for p in x], mae_values, width=0.4, label='MAE', color='r', align='center')
    
    plt.xticks([p + 0.2 for p in x], models)
    plt.title('Model Comparison: RMSE and MAE')
    plt.ylabel('Error')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    return plt

def plot_hourly_ridership_patterns(hourly_data):
    plt.figure(figsize=(15, 6))
    plt.plot(hourly_data['Hour'], hourly_data['Weekday'], label='Weekday', color='blue')
    plt.plot(hourly_data['Hour'], hourly_data['Weekend'], label='Weekend', color='orange')
    
    plt.title('Average Hourly Ridership Patterns')
    plt.xlabel('Hour of Day')
    plt.ylabel('Average Ridership')
    plt.xticks(hourly_data['Hour'])
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    return plt