import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Profil Kreator", page_icon="👨‍💻", layout="wide")

# --- HEADER PROFIL (Sistem 2 Kolom) ---
col_img, col_info = st.columns([1, 2.5])

with col_img:
    # Memastikan gambar profil menyesuaikan lebar kolom agar tidak terlalu besar
    st.image("me.png", use_container_width=True)

with col_info:
    st.title("Bagus Rahma Aulia Chandra")
    st.subheader("Data Analyst | Data Science & Graphic Design Enthusiast")
    st.markdown("📍 **Pati, Jawa Tengah**")
    
    st.write("""
    Lulusan S1 Teknik Informatika dengan fokus pada Analisis Data, *Machine Learning*, dan visualisasi informasi. 
    Memiliki ketertarikan mendalam dalam menerjemahkan data mentah menjadi *insight* bisnis yang dapat ditindaklanjuti 
    menggunakan Python dan Streamlit, serta memadukannya dengan sentuhan desain visual yang menarik.
    """)
    
    # Menambahkan link ke GitHub atau portofolio lain
    st.markdown("[🔗 GitHub: isNothingSpecial](https://github.com/isNothingSpecial)")

st.divider()

# --- PENGALAMAN & PENDIDIKAN (Sistem 2 Kolom) ---
col_exp, col_edu = st.columns(2)

with col_exp:
    st.subheader("💼 Pengalaman Profesional")
    
    st.markdown("""
    * **AI Creator Intern | Zerone Japan** *(Jan 2026 - Feb 2026)*
      * Memanfaatkan *platform* AI untuk merancang dan memproduksi konten pemasaran visual.
    * **Business Analyst | PT Solvera Global Teknologi** *(Nov 2025 - Des 2025)*
      * Bertanggung jawab dalam pemeliharaan dan analisis sistem ERP Odoo.
    * **Data Analyst Intern | Sribu.com** *(Nov 2024 - Jan 2025)*
      * Menganalisis data platform dan mempresentasikan hasil temuan kepada *stakeholder*.
    """)

with col_edu:
    st.subheader("🎓 Pendidikan & Sertifikasi")
    
    st.markdown("""
    * **S1 Teknik Informatika | Universitas Dian Nuswantoro** *(2017 - 2024)*
      * NIM: A11.2017.10295
    * **Bootcamp Data Science (Batch 39) | DigitalSkola** *(Jun 2025)*
      * Pelatihan intensif pemodelan *Machine Learning*, pengolahan data, dan portofolio teknis.
    """)

st.divider()

# --- KEAHLIAN (Skills) ---
st.subheader("🛠️ Keahlian & Teknologi")

# Menggunakan badge/tombol statis untuk menampilkan skill agar visualnya menarik
skill_col1, skill_col2, skill_col3, skill_col4 = st.columns(4)
with skill_col1:
    st.info("🐍 Python (Pandas, Scikit-Learn)")
with skill_col2:
    st.info("📊 Streamlit & Data Visualization")
with skill_col3:
    st.info("🤖 Machine Learning (K-Means)")
with skill_col4:
    st.info("🎨 Graphic Design & UI/UX")
