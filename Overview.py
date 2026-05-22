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
    
    # 1. Dapatkan label acak bawaan K-Means
    clusters['Cluster_Raw'] = kms.fit_predict(df_clusters)
    
    # 2. Hitung rata-rata 'SUM Price' untuk masing-masing cluster acak
    # Lalu urutkan dari yang terkecil hingga terbesar
    rata_rata_cluster = clusters.groupby('Cluster_Raw')['SUM Price'].mean().sort_values()
    
    # 3. Buat dictionary pemetaan (mapping) label baru
    mapping_label = {old_id: new_id for new_id, old_id in enumerate(rata_rata_cluster.index)}
    
    # 4. Terapkan pemetaan ke kolom 'Cluster' akhir
    clusters['Cluster'] = clusters['Cluster_Raw'].map(mapping_label)
    
    # Hapus kolom raw agar tidak muncul di tabel atau popup hover grafik
    clusters = clusters.drop(columns=['Cluster_Raw'])
    
    # Mengubah tipe data cluster menjadi string untuk Plotly agar dianggap sebagai kategori
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
            # Warna diurutkan: 0 (Biru/Low), 1 (Kuning/Medium), 2 (Pink/High)
            color_discrete_sequence=['#00b4d8', '#fee440', '#f15bb5'], 
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
        * **Cluster 0 (Low Demand):** Fokus pada edukasi produk dan penawaran *bundling* terjangkau untuk memicu pembelian ulang.
        * **Cluster 1 (Medium Demand):** Tawarkan promo *upselling* untuk meningkatkan nilai keranjang belanja mereka.
        * **Cluster 2 (High Demand):** Pertahankan loyalitas dengan memberikan layanan prioritas atau program *reward* khusus agen/distributor.
        """)
