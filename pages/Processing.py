import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Prediksi Pelanggan HNI", layout="centered")

# --- CACHING MODEL ---
# Fit model hanya sekali saat aplikasi pertama kali dijalankan
@st.cache_resource
def train_model():
    df = pd.read_csv('finaldata.csv')
    
    # Pastikan hanya mengambil kolom numerik yang relevan sesuai urutan saat EDA
    X = df[['SUM Price', 'SUM PV']] 
    
    kms = KMeans(n_clusters=3, init='k-means++', random_state=42)
    
    # Dapatkan label acak (raw) untuk data latih
    df['Cluster_Raw'] = kms.fit_predict(X)
    
    # Hitung rata-rata 'SUM Price' dan buat dictionary mapping agar urut 0=Low, 1=Mid, 2=High
    rata_rata_cluster = df.groupby('Cluster_Raw')['SUM Price'].mean().sort_values()
    mapping_label = {old_id: new_id for new_id, old_id in enumerate(rata_rata_cluster.index)}
    
    # Kembalikan model dan dictionary mapping-nya
    return kms, mapping_label

# Panggil fungsi train model dan simpan variabel mapping-nya
kms, mapping_label = train_model()

# --- HEADER ---
st.title("🔍 Prediksi Segmen Pelanggan Baru (HNI)")
st.markdown("""
Masukkan data akumulasi transaksi pelanggan baru untuk memprediksi mereka akan masuk ke dalam klaster mana.
""")

st.divider()

# --- FORM INPUT ---
# Menggunakan st.form agar aplikasi tidak reload setiap kali angka diketik
with st.form("form_prediksi"):
    col1, col2 = st.columns(2)
    
    with col1:
        # Min value diatur 0.0 agar tidak menerima input negatif
        input_price = st.number_input("Total Harga Transaksi (Rp)", min_value=0.0, step=50000.0)
        
    with col2:
        input_pv = st.number_input("Total Point Value (PV)", min_value=0.0, step=10.0)
        
    # Tombol submit berada di dalam form
    submitted = st.form_submit_button("Prediksi Cluster", type="primary")

# --- LOGIKA PREDIKSI ---
if submitted:
    if input_price > 0 or input_pv > 0:
        
        # 1. Dapatkan prediksi mentah (raw) dari algoritma
        raw_prediction = kms.predict([[input_price, input_pv]])[0]
        
        # 2. Konversi/petakan prediksi mentah menjadi urutan yang benar menggunakan mapping
        prediction = mapping_label[raw_prediction]
        
        st.subheader("Hasil Analisis:")
        
        # --- UI HASIL PREDIKSI ---
        if prediction == 0:
            st.info("🎯 **Prediksi: CLUSTER 0 (Low Price, Low Demand)**")
            st.markdown("""
            **Rentang Transaksi:** Rp 0 - Rp 490.000
            
            **Analisis Profil:** 
            Pelanggan di klaster ini melakukan sedikit transaksi dengan nominal yang relatif terjangkau.
            
            **Faktor Penyebab:**
            * Pelanggan baru yang sedang mencoba produk HNI untuk pertama kalinya.
            * Pelanggan luar kota yang lebih memilih membeli di tempat yang secara geografis lebih dekat, sehingga transaksi di cabang ini minim.
            """)
            
        elif prediction == 1:
            st.warning("🎯 **Prediksi: CLUSTER 1 (Medium)**")
            st.markdown("""
            **Rentang Transaksi:** Rp 491.000 - Rp 965.000
            
            **Analisis Profil:** 
            Pelanggan dengan frekuensi belanja atau kuantitas barang tingkat menengah.
            
            **Faktor Penyebab:**
            * Pelanggan luar kota yang sesekali berbelanja.
            * Pelanggan lama yang sering bertransaksi, namun fokus pada produk-produk dengan harga yang sangat terjangkau secara konstan.
            """)
            
        elif prediction == 2:
            st.success("🎯 **Prediksi: CLUSTER 2 (High Price, High Demand)**")
            st.markdown("""
            **Rentang Transaksi:** > Rp 1.000.000
            
            **Analisis Profil:** 
            Pelanggan VIP. Sering melakukan transaksi dengan kuantitas borongan (banyak) dalam sekali waktu.
            
            **Faktor Penyebab:**
            * Pelanggan sangat konsisten berbelanja di cabang ini.
            * Memiliki daya beli tinggi atau merupakan distributor/agen yang menyetok ulang barang jualannya.
            """)
    else:
        st.error("Silakan masukkan nilai nominal Harga atau PV lebih dari 0 untuk memprediksi.")
