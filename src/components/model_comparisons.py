import os
import streamlit as st
import pandas as pd

def load_model_comparison_data():
    """
    Load the model performance metrics from a CSV file.
    """
    try:
        # Load the CSV file
        df = pd.read_csv(r'D:\Coding\Projects\Delhi Metro Ridership Prediction\delhi-metro-dashboard\src\data\model_performance_metrics.csv')
        return df
    except FileNotFoundError:
        st.error("The file 'model_performance_metrics.csv' was not found. Please ensure it exists in the 'data' directory.")
        return pd.DataFrame()  # Return an empty DataFrame if the file is missing

def plot_model_comparisons(df):
    """
    Plot comparisons of model performance metrics.
    """
    # Display the summary bar chart image instead of generating separate RMSE, MAE, R2 plots
    model_comparison_path = os.path.join(
        r"D:\Coding\Projects\Delhi Metro Ridership Prediction\delhi-metro-dashboard\src\assets\model_analysis_graphs",
        "model_comparison.png"
    )
    if os.path.exists(model_comparison_path):
        st.image(model_comparison_path, use_container_width=True)

def display_model_comparison_graphs():
    """Display all graphs from the model_analysis_graphs directory except model_comparison.png and model-specific graphs."""
    st.markdown(
        """
        <p style='font-size: 1.4rem; color: #333; margin-bottom: 1.5em;'>
           Below are the visualizations generated from the model comparisons:
        </p>
        """,
        unsafe_allow_html=True
    )
    graphs_dir = r"D:\Coding\Projects\Delhi Metro Ridership Prediction\delhi-metro-dashboard\src\assets\model_analysis_graphs"

    if not os.path.exists(graphs_dir):
        st.error(f"The directory '{graphs_dir}' does not exist. Please ensure the path is correct and contains the model comparison graphs.")
        return

    graph_files = sorted([f for f in os.listdir(graphs_dir) if f.endswith('.png')])

    if not graph_files:
        st.warning("No PNG files found in the directory.")
        return

    # List of graphs to exclude from the bottom section
    exclude_files = [
        "xgboost_feature_importance.png",
        "xgboost_actual_vs_predicted.png",
        "linear_regression_actual_vs_predicted.png",
        "linear_regression_coefficients.png",
        "ensemble_actual_vs_predicted.png",
        "model_comparison.png"
    ]

    for graph_file in graph_files:
        if graph_file not in exclude_files:
            st.image(os.path.join(graphs_dir, graph_file), use_container_width=True)
            st.markdown("---")

def compare_models():
    st.markdown(
        """
        <h1 style='font-size: 3.2rem; font-weight: 900; color: #001f3f; margin-bottom: 0.2em;'>
            Model Comparisons
        </h1>
        <hr style='border: 2px solid #001f3f; margin-top: 0; margin-bottom: 2em;'>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <p style='font-size: 1.4rem; color: #333; margin-bottom: 1.5em;'>
           This section compares the performance of different models used for ridership prediction.
        </p>
        """,
        unsafe_allow_html=True
    )

    # Load model performance data
    df = load_model_comparison_data()

    # --- XGBoost Section ---
    st.header("🚀 XGBoost Model")
    st.markdown(
        """
        <p style='font-size: 1.4rem; color: #333; margin-bottom: 1.5em;'>
           Performance Metrics for XGBoost Model:
        </p>
        """,
        unsafe_allow_html=True
    )
    if not df.empty:
        xgb_row = df[df['Model'].str.lower().str.contains('xgboost')]
        if not xgb_row.empty:
            st.dataframe(xgb_row)
    st.markdown(
        """
        <p style='font-size: 1.4rem; color: #333; margin-bottom: 1.5em;'>
           Visualizations for XGBoost Model:
        </p>
        """,
        unsafe_allow_html=True
    )
    # Actual vs Predicted graph for XGBoost
    xgb_actual_vs_pred_path = os.path.join(
        r"D:\Coding\Projects\Delhi Metro Ridership Prediction\delhi-metro-dashboard\src\assets\model_analysis_graphs",
        "xgboost_actual_vs_predicted.png"
    )
    if os.path.exists(xgb_actual_vs_pred_path):
        st.image(xgb_actual_vs_pred_path, use_container_width=True)
    # Feature importance 
    xgb_graph_path = os.path.join(
        r"D:\Coding\Projects\Delhi Metro Ridership Prediction\delhi-metro-dashboard\src\assets\model_analysis_graphs",
        "xgboost_feature_importance.png"
    )
    if os.path.exists(xgb_graph_path):
        st.image(xgb_graph_path, use_container_width=True)

    # --- Linear Regression Section ---
    st.markdown("<hr style='border: 2px solid #001f3f;'>", unsafe_allow_html=True)
    st.header("📈 Linear Regression Model")
    st.markdown(
        """
        <p style='font-size: 1.4rem; color: #333; margin-bottom: 1.5em;'>
           Performance Metrics for Linear Regression Model:
        </p>
        """,
        unsafe_allow_html=True
    )
    lr_row = df[df['Model'].str.lower().str.contains('linear')]
    if not lr_row.empty:
        st.dataframe(lr_row)
    st.markdown(
        """
        <p style='font-size: 1.4rem; color: #333; margin-bottom: 1.5em;'>
           Visualizations for Linear Regression Model:
        </p>
        """,
        unsafe_allow_html=True
    )
    # Actual vs Predicted graph for Linear Regression
    lr_actual_vs_pred_path = os.path.join(
        r"D:\Coding\Projects\Delhi Metro Ridership Prediction\delhi-metro-dashboard\src\assets\model_analysis_graphs",
        "linear_regression_actual_vs_predicted.png"
    )
    if os.path.exists(lr_actual_vs_pred_path):
        st.image(lr_actual_vs_pred_path, use_container_width=True)
    # Linear Regression Coefficient graph
    lr_coeff_path = os.path.join(
        r"D:\Coding\Projects\Delhi Metro Ridership Prediction\delhi-metro-dashboard\src\assets\model_analysis_graphs",
        "linear_regression_coefficients.png"
    )
    if os.path.exists(lr_coeff_path):
        st.image(lr_coeff_path, use_container_width=True)

    # --- Ensemble Model Section ---
    st.markdown("<hr style='border: 2px solid #001f3f;'>", unsafe_allow_html=True)
    st.header("🤝 Ensemble Model")
    st.markdown(
        """
        <p style='font-size: 1.4rem; color: #333; margin-bottom: 1.5em;'>
           Performance Metrics for Ensemble Model:
        </p>
        """,
        unsafe_allow_html=True
    )
    ensemble_row = df[df['Model'].str.lower().str.contains('ensemble')]
    if not ensemble_row.empty:
        st.dataframe(ensemble_row)

    st.markdown(
        """
        <p style='font-size: 1.4rem; color: #333; margin-bottom: 1.5em;'>
           Visualizations for for Ensemble Model:
        </p>
        """,
        unsafe_allow_html=True
    )
    # Actual vs Predicted graph for Ensemble
    ensemble_actual_vs_pred_path = os.path.join(
        r"D:\Coding\Projects\Delhi Metro Ridership Prediction\delhi-metro-dashboard\src\assets\model_analysis_graphs",
        "ensemble_actual_vs_predicted.png"
    )
    if os.path.exists(ensemble_actual_vs_pred_path):
        st.image(ensemble_actual_vs_pred_path, use_container_width=True)

    # --- Performance Metric Table ---
    st.markdown("<hr style='border: 2px solid #001f3f;'>", unsafe_allow_html=True)
    st.header("📊 Performance Metric Comparison")
    
    st.markdown(
        """
        <p style='font-size: 1.4rem; color: #333; margin-bottom: 1.5em;'>
           Compare the key performance metrics of all models below.
        </p>
        """,
        unsafe_allow_html=True
    )

    if not df.empty:
        st.dataframe(df)

    # --- Model Performance Comparison (Bar Charts) ---
    st.markdown("<hr style='border: 2px solid #001f3f;'>", unsafe_allow_html=True)
    st.header("📉 Model Performance Comparison (Bar Charts)")
    plot_model_comparisons(df)

    # --- Cross Validation Graphs ---
    st.markdown("<hr style='border: 2px solid #001f3f;'>", unsafe_allow_html=True)
    st.header("🖼️ Cross Validation Graphs")
    display_model_comparison_graphs()

if __name__ == "__main__":
    compare_models()