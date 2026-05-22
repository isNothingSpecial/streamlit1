import streamlit as st

# --- KONFIGURASI HALAMAN ---
# Halaman ini statis, gunakan layout wide agar teks tidak terlalu sempit
st.set_page_config(page_title="Profil Perusahaan HNI", page_icon="🏢", layout="wide")

# --- HEADER & GAMBAR UTAMA ---
# Membagi layar menjadi 2 kolom (Gambar di kiri, Teks di kanan dengan proporsi 1:2)
col_img, col_text = st.columns([1, 2])

with col_img:
    # use_container_width memastikan gambar tidak melebihi batas kolom
    st.image("1835901.png", use_container_width=True)
    st.caption("Logo Resmi Halal Network International (HNI)")

with col_text:
    st.title("🏢 Profil Perusahaan: PT HPAI (HNI)")
    st.markdown("""
    **PT Herba Penawar Alwahida Indonesia (HPAI)**, yang kini lebih dikenal sebagai **HNI**, 
    merupakan salah satu pelopor perusahaan Bisnis Halal Network di Indonesia. 
    Secara resmi didirikan pada **19 Maret 2012**, perusahaan ini berfokus pada penyediaan 
    produk barang konsumsi (*consumer goods*) yang terjamin kehalalan dan kualitasnya.
    """)

st.divider() # Garis pemisah horizontal

# --- KONTEN TENTANG PERUSAHAAN ---
st.subheader("Latar Belakang & Tujuan")
st.markdown("""
HPAI lahir dari perjuangan panjang untuk menjayakan produk-produk halal berkualitas yang berazaskan *Thibbunnabawi* (Pengobatan Ala Nabi). 
Fokus utama pergerakan bisnis ini ditujukan untuk:
*   **Membumikan dan memajukan** ekonomi Islam di Indonesia.
*   **Mengaktualisasikan *entrepreneurship*** (kewirausahaan) di kalangan masyarakat.
*   **Memberdayakan dan mengangkat** Usaha Mikro, Kecil, dan Menengah (UMKM) tingkat nasional.
""")

st.write("") # Memberikan sedikit ruang/spasi

# --- VISI & MISI (Menggunakan Block Warna) ---
st.subheader("Visi & Misi Perusahaan")

# Membagi Visi dan Misi ke dalam 2 kolom sejajar
col_visi, col_misi = st.columns(2)

with col_visi:
    # st.info memberikan background biru yang rapi
    st.info("""
    **🎯 VISI**  
    Menjadi Pemimpin Industri Halal Kelas Dunia (dari Indonesia).
    """)

with col_misi:
    # st.success memberikan background hijau yang cocok dengan tema herbal/halal
    st.success("""
    **🚀 MISI**  
    * Menjadi perusahaan jaringan pemasaran papan atas kebanggaan Ummat.
    * Menjadi wadah perjuangan penyediaan Produk Halal bagi umat Islam.
    * Menghasilkan pengusaha-pengusaha muslim yang dapat dibanggakan (pemasar, pembangun jaringan, maupun produsen).
    """)
