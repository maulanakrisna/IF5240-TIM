import streamlit as st
import pandas as pd
import plotly.express as px

# Data
data = {
    "Fault ID": ["F001", "F002", "F003", "F004", "F005", "F006"],
    "Fault Type": ["Line Breakage", "Transformer Failure", "Overheating", "Line Breakage", "Transformer Failure", "Overheating"],
    "Latitude": [34.0522, 34.056, 34.0525, 34.055, 34.0545, 34.05],
    "Longitude": [-118.2437, -118.245, -118.244, -118.242, -118.243, -118.24],
    "Voltage (V)": [2200, 1800, 2100, 2050, 1900, 2150],
    "Current (A)": [250, 180, 230, 240, 190, 220],
    "Power Load (MW)": [50, 45, 55, 48, 50, 52],
    "Temperature (°C)": [25, 28, 35, 23, 30, 32],
    "Wind Speed (km/h)": [20, 15, 25, 10, 18, 22],
    "Weather Condition": ["Clear", "Rainy", "Windstorm", "Clear", "Snowy", "Thunderstorm"],
    "Maintenance Status": ["Scheduled", "Completed", "Pending", "Completed", "Scheduled", "Pending"],
    "Component Health": ["Normal", "Faulty", "Overheated", "Normal", "Faulty", "Overheated"],
    "Duration of Fault (hrs)": [2.0, 3.0, 4.0, 2.5, 3.5, 5.0],
    "Down time (hrs)": [1.0, 5.0, 6.0, 3.0, 4.0, 7.0]
}

df = pd.DataFrame(data)

st.set_page_config(page_title="Investment Decision Dashboard", layout="wide")
st.title("📊 Investment Decision Support Dashboard")

st.markdown(
    """
    Dashboard ini membantu mengidentifikasi area prioritas untuk investasi perbaikan infrastruktur listrik, 
    berdasarkan data fault historis, kondisi lingkungan, dan downtime.
    """
)

# Sidebar
st.sidebar.header("Filter Data")
fault_types = st.sidebar.multiselect(
    "Pilih Fault Type", options=df["Fault Type"].unique(), default=df["Fault Type"].unique()
)

weather = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca", options=df["Weather Condition"].unique(), default=df["Weather Condition"].unique()
)

health = st.sidebar.multiselect(
    "Pilih Component Health", options=df["Component Health"].unique(), default=df["Component Health"].unique()
)

df_filtered = df[
    (df["Fault Type"].isin(fault_types)) &
    (df["Weather Condition"].isin(weather)) &
    (df["Component Health"].isin(health))
]

# KPI
col1, col2, col3 = st.columns(3)
col1.metric("🔧 Jumlah Fault", len(df_filtered))
col2.metric("⏳ Rata-rata Downtime (jam)", round(df_filtered["Down time (hrs)"].mean(), 2))
col3.metric("💡 Total Power Load (MW)", df_filtered["Power Load (MW)"].sum())

# Map
st.subheader("📍 Lokasi Fault")
fig_map = px.scatter_mapbox(
    df_filtered,
    lat="Latitude",
    lon="Longitude",
    hover_name="Fault ID",
    hover_data=["Fault Type", "Down time (hrs)"],
    color="Fault Type",
    size="Down time (hrs)",
    zoom=12,
    height=400
)
fig_map.update_layout(mapbox_style="open-street-map")
fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig_map, use_container_width=True)

# Downtime by Fault Type
st.subheader("⏳ Rata-rata Downtime per Jenis Fault")
fig_downtime = px.bar(
    df_filtered.groupby("Fault Type")["Down time (hrs)"].mean().reset_index(),
    x="Fault Type",
    y="Down time (hrs)",
    color="Fault Type",
    text_auto=True
)
st.plotly_chart(fig_downtime, use_container_width=True)

# Weather impact
st.subheader("🌦️ Downtime Berdasarkan Kondisi Cuaca")
fig_weather = px.box(
    df_filtered,
    x="Weather Condition",
    y="Down time (hrs)",
    color="Weather Condition"
)
st.plotly_chart(fig_weather, use_container_width=True)

# Data table
st.subheader("📄 Data Detail")
st.dataframe(df_filtered)

