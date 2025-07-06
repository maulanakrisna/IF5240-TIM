import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("fault_data.csv")

# Pisahkan kolom lokasi menjadi Latitude & Longitude
df[["Latitude", "Longitude"]] = df["Fault Location (Latitude, Longitude)"].str.strip("()").str.split(",", expand=True)
df["Latitude"] = df["Latitude"].astype(float)
df["Longitude"] = df["Longitude"].astype(float)

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
    zoom=10,
    height=500
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

