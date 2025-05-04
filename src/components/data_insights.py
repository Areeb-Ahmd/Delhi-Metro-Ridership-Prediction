import os
import pandas as pd
import streamlit as st

def load_data():
    """Load the dataset."""
    df = pd.read_csv(os.path.join('data', 'delhi_metro_final.csv'))
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
    return df

def display_overview(df):
    """Display an overview of the dataset."""
    st.markdown("## 📊 Data Overview")
    st.markdown(
        """
        <p style='font-size: 1.4rem; color: #333; margin-bottom: 1.5em;'>
           This section provides insights into the Delhi Metro ridership data.
        </p>
        """,
        unsafe_allow_html=True
    )

    
    st.markdown("#### 🧾 First 5 Rows")
    st.dataframe(df.head())

    st.markdown("#### 📈 Summary Statistics")
    st.dataframe(df.describe())


def display_analysis_graphs():
    """Display all graphs from the data_analysis_graphs directory."""
    st.markdown("<hr style='border: 2px solid #001f3f;'>", unsafe_allow_html=True)
    st.markdown("## 📉 Analysis Graphs")
    st.markdown(
        """
        <p style='font-size: 1.4rem; color: #333; margin-bottom: 1.5em;'>
           Below are the visualizations generated from the data analysis:
        </p>
        """,
        unsafe_allow_html=True
    )

    graphs_dir = os.path.join('assets', 'data_analysis_graphs')
    graph_files = sorted([f for f in os.listdir(graphs_dir) if f.endswith('.png')])

    # Display images one per row
    for graph_file in graph_files:
        st.image(os.path.join(graphs_dir, graph_file), use_container_width=True)

def show_data_insights():
    """Main function to display data insights."""
    st.markdown(
        """
        <h1 style='font-size: 3.2rem; font-weight: 900; color: #001f3f; margin-bottom: 0.2em;'>
            Delhi Metro Data Insights
        </h1>
        <hr style='border: 2px solid #001f3f; margin-top: 0; margin-bottom: 2em;'>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <p style='font-size: 1.8rem; color: #333; margin-bottom: 1.5em;'>
           Get a quick overview and visual analysis of the Delhi Metro ridership dataset.
        </p>
        """,
        unsafe_allow_html=True
    )
    df = load_data()
    display_overview(df)
    display_analysis_graphs()

if __name__ == "__main__":
    show_data_insights()