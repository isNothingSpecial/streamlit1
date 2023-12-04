import streamlit as st
import pandas as pd # Pandas (version : 1.1.5) 
import numpy as np # Numpy (version : 1.19.2)
import matplotlib.pyplot as plt # Matplotlib (version :  3.3.2)
from sklearn.cluster import KMeans # Scikit Learn (version : 0.23.2)
import seaborn as sns # Seaborn (version : 0.11.1)
from streamlit_webrtc import webrtc_streamer

st.image("1835901.png",width=500,align='center')
st.caption('Logo HNI')
st.write('''
        ''')
st.markdown(''' TENTANG HPAI
PT Herba Penawar Alwahida Indonesia, yang kemudian dikenal sebagai HPAI, merupakan salah satu perusahaan Bisnis Halal Network di Indonesia yang fokus pada penyediaan produk-produk barang konsumsi (consumer goods) yang halal dan berkualitas. HPAI, sesuai dengan akta pendirian perusahaan, secara resmi didirikan pada tanggal 19 Maret 2012.

HPAI merupakan hasil dari perjuangan panjang dengan tujuan untuk menjayakan produk-produk halal berkualitas yang berazaskan Thibbunnabawi; membumikan, memajukan, dan mengaktualisasikan ekonomi Islam di Indonesia melalui enterpreneurship, dan juga turut serta dalam memberdayakan dan mengangkat UMKM nasional.

VISI

Menjadi Pemimpin Industri Halal Kelas Dunia (dari Indonesia)

MISI

Menjadi perusahaan jaringan pemasaran papan atas kebanggaan Ummat.
Menjadi wadah perjuangan penyediaan Produk Halal bagi ummat Islam.
Menghasilkan pengusaha-pengusaha muslim yang dapat dibanggakan, baik sebagai pemasar, pembangun jaringan maupun produsen''')
