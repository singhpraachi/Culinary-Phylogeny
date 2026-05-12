import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
from scipy.cluster.hierarchy import linkage
import numpy as np

# --- 1. PAGE CONFIG & ZOMATO THEMING ---
st.set_page_config(page_title="FlavorMap | Culinary DNA", layout="wide")

# Custom CSS to inject Zomato's brand colors (#E23744 is Zomato Red)
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #0F0F0F;
        color: #FFFFFF;
    }
    
    /* Zomato Red Sidebar */
    [data-testid="stSidebar"] {
        background-color: #1A1A1A;
        border-right: 2px solid #E23744;
    }
    
    /* Titles and Headers */
    h1, h2, h3 {
        color: #E23744 !important;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 800;
    }
    
    /* Card-like containers for data */
    div.stMetric {
        background-color: #1A1A1A;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #333;
    }

    /* Primary Buttons */
    .stButton>button {
        background-color: #E23744;
        color: white;
        border-radius: 20px;
        border: none;
        width: 100%;
        font-weight: bold;
    }

    .stButton>button:hover {
        background-color: #C12D38;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATA LOADING (SIMULATED FOR PROTOTYPE) ---
# Replace this section with your actual 'cuisine_profiles' loading code
@st.cache_data
def get_data():
    # This is a placeholder. Ensure your 'cuisine_profiles' from Colab is saved as a CSV
    # and loaded here: df = pd.read_csv('cuisine_profiles.csv', index_index=0)
    # For now, let's assume 'df' is ready.
    try:
        df = pd.read_csv('data/cuisine_profile.csv', index_col=0)
    except:
        st.error("Please upload your 'cuisine_profiles.csv' to the project folder!")
        st.stop()
    return df

df = get_data()

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/bd/Zomato_Logo.png", width=150)
    st.markdown("### Model Controls")
    method = st.selectbox("Clustering Algorithm", ["ward", "complete", "single", "average"])
    threshold = st.slider("Similarity Threshold", 0.1, 5.0, 1.5)
    st.info("Adjust the threshold to see how cuisines group into 'Flavor Families'.")

# --- 4. MAIN INTERFACE ---
st.title("🍴 Culinary Phylogeny")
st.markdown("##### Exploring the Global 'Family Tree' of Cuisines through Data Science")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("The Cuisine Dendrogram")
    # Perform math on the fly based on user 'method'
    Z = linkage(df, method=method)
    
    # Create Plotly Dendrogram (Interactive)
    fig = ff.create_dendrogram(df, labels=df.index, colorscale=['#E23744', '#FF828B', '#FFFFFF', '#666666'])
    fig.update_layout(
        width=800, height=500, 
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white")
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Flavor Insights")
    selected_cuisine = st.selectbox("Deep Dive into a Cuisine", df.index)
    
    # Show top ingredients for selected cuisine
    top_ingreds = df.loc[selected_cuisine].sort_values(ascending=False).head(5)
    
    st.write(f"Top Signature Ingredients for **{selected_cuisine}**:")
    for ing, val in top_ingreds.items():
        st.write(f"✅ {ing.title()}")
    
    st.divider()
    st.metric(label="Total Cuisines Analyzed", value=len(df))
    st.metric(label="Unique Ingredients", value=df.shape[1])

# --- 5. DATA TABLE ---
st.subheader("Explore the Raw Matrix")
st.dataframe(df.style.background_gradient(cmap='Reds'), use_container_width=True)