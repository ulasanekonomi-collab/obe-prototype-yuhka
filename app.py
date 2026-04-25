import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Judul di Browser
st.title("Prototype OBE - Prodi Ekonomi")
st.subheader("Simulasi Capaian Profil Lulusan")

# 2. Membuat Input Interaktif di Sidebar
st.sidebar.header("Input Nilai Mahasiswa")
logika = st.sidebar.slider("CPL 01: Logika", 0, 100, 85)
ekonomi = st.sidebar.slider("CPL 02: Ekonomi", 0, 100, 78)
etika = st.sidebar.slider("CPL 03: Etika", 0, 100, 92)

# 3. Mengolah Data
df_radar = pd.DataFrame({
    'CPL': ['Logika', 'Ekonomi', 'Etika'],
    'Nilai': [logika, ekonomi, etika]
})

# 4. Membuat Grafik Radar
fig = px.line_polar(df_radar, r='Nilai', theta='CPL', line_close=True, range_r=[0,100])
fig.update_traces(fill='toself', fillcolor='rgba(31, 119, 180, 0.5)')

# 5. Menampilkan Grafik
st.plotly_chart(fig)

# 6. Menampilkan Tabel Data
st.table(df_radar)
