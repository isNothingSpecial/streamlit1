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
    # Sesuaikan nama kolom ini jika di CSV Anda berbeda
    X = df[['SUM Price', 'SUM PV']] 
    
    kms = KMeans(n_clusters=3, init='k-means++', random_state=42)
    kms.fit(X)
    return kms

# Panggil fungsi train model
kms = train_model()

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
        # PENTING: Urutan array harus sama dengan saat fitting model [Price, PV]
        prediction = kms.predict([[input_price, input_pv]])[0]
        
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
