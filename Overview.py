import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.cluster import KMeans

# Konfigurasi Halaman (Harus diletakkan paling atas)
st.set_page_config(
    page_title="HNI Customer Segmentation",
    page_icon="📊",
    layout="wide"
)

# --- FUNGSI CACHING ---
# Menggunakan cache agar data tidak di-load ulang setiap kali ada interaksi di UI
@st.cache_data
def load_data():
    df = pd.read_csv('Laporan_Penjualan1.csv')
    df_proc = pd.read_csv('cleandata.csv')
    df_clusters = pd.read_csv('finaldata.csv')
    return df, df_proc, df_clusters

df, df_proc, df_clusters = load_data()

# --- HEADER & KPI METRICS ---
st.title("🎯 Segmentasi Pelanggan Produk HNI (K-Means)")
st.markdown("Analisis data penjualan produk HNI di cabang PT HPAI Tunggulrejo, Kabupaten Purworejo (Periode: 2021 - Sep 2023).")

# Menampilkan Ringkasan Metrik Bisnis
col1, col2, col3 = st.columns(3)
col1.metric("Total Pelanggan Aktif", len(df_proc))
col2.metric("Total Transaksi", len(df))
col3.metric("Algoritma Clustering", "K-Means (k=3)")

st.divider()

# --- SISTEM TAB UNTUK LAYOUT ---
tab1, tab2, tab3 = st.tabs(["📝 Overview & Data Mentah", "⚙️ Data Preprocessing", "📊 Hasil Klastering & Insight"])

with tab1:
    st.subheader("Data Penjualan (Raw Data)")
    st.markdown("""
    Data di bawah ini merupakan data mentah sebelum dilakukan pemrosesan. Tahapan yang akan dilakukan meliputi:
    * Pembersihan kolom yang tidak relevan.
    * Standarisasi nama kolom.
    * Agregasi (Grouping) berdasarkan pelanggan.
    * Penanganan *Outliers*.
    """)
    st.dataframe(df, use_container_width=True)

with tab2:
    st.subheader("Hasil Preprocessing & Grouping")
    st.markdown("Berikut adalah data yang telah diagregasi untuk setiap `Customer_Name`, siap untuk dimasukkan ke dalam model K-Means.")
    st.dataframe(df_proc, use_container_width=True)

with tab3:
    # Modelling K-Means
    # Menambahkan random_state agar hasil cluster konsisten setiap kali direfresh
    kms = KMeans(n_clusters=3, init='k-means++', random_state=42)
    
    clusters = df_clusters.copy()
    clusters['Cluster'] = kms.fit_predict(df_clusters)
    
    # Mengubah tipe data cluster menjadi string untuk Plotly agar dianggap sebagai kategori, bukan skala kontinu
    clusters['Cluster'] = clusters['Cluster'].astype(str)

    st.subheader("Distribusi Klaster Pelanggan")
    
    # Membagi layout menjadi 2 kolom untuk memisahkan grafik dan tabel
    col_chart, col_table = st.columns([2, 1])
    
    with col_chart:
        # Visualisasi Interaktif dengan Plotly
        fig = px.scatter(
            clusters, 
            x='SUM Price', 
            y='SUM PV', 
            color='Cluster',
            color_discrete_sequence=['#00b4d8', '#f15bb5', '#fee440'],
            title="Persebaran Segmen: Akumulasi Harga vs Point Value (PV)",
            labels={'SUM Price': 'Total Belanja (Rp)', 'SUM PV': 'Total PV'},
            hover_data=clusters.columns # Menampilkan semua info saat titik di-hover
        )
        fig.update_traces(marker=dict(size=12, line=dict(width=1, color='DarkSlateGrey')))
        fig.update_layout(legend_title_text='Segmen')
        
        # Menampilkan grafik di Streamlit
        st.plotly_chart(fig, use_container_width=True)
        
    with col_table:
        st.markdown("**Tabel Hasil Klastering**")
        st.dataframe(clusters, use_container_width=True)
        
    # Area untuk Insight Bisnis
    with st.expander("💡 Rekomendasi & Insight Bisnis"):
        st.markdown("""
        Berdasarkan visualisasi di atas, Anda dapat memetakan strategi:
        * **Cluster 0:** Fokus pada peningkatan volume transaksi (Cross-selling).
        * **Cluster 1:** Pertahankan loyalitas dengan reward khusus.
        * **Cluster 2:** Evaluasi pelanggan pasif dan berikan promo *win-back*.
        *(Sesuaikan interpretasi cluster dengan letak centroid masing-masing kelompok)*
        """)
