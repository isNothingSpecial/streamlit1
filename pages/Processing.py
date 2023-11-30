import streamlit as st
import pandas as pd # Pandas (version : 1.1.5) 
import numpy as np # Numpy (version : 1.19.2)
import matplotlib.pyplot as plt # Matplotlib (version :  3.3.2)
from sklearn.cluster import KMeans # Scikit Learn (version : 0.23.2)
import seaborn as sns # Seaborn (version : 0.11.1)
from streamlit_webrtc import webrtc_streamer

df = pd.read_csv('finaldata.csv')

kms = KMeans(n_clusters=3, init='k-means++')
kms.fit(df)

st.title(''' SEGMENTASI PELANGGAN PEMEMBELIAN PRODUK HALAL NETWORK INTERNATIONAL (HNI) DENGAN MENGGUNAKAN ALGORITMA K-MEANS ''')
st.write('Prediksi Data Baru')

input_pv = st.number_input ("Total Point Value", )
#min_value=df('precipation').min()
#max_value=df('precipation').max()

input_price = st.number_input ("Total Harga")
#min_value=df('precipation').min()
#max_value=df('precipation').max()

result = "-"

if st.button("Predict"):
    if input_pv != str(0.00) and input_price != str(0.00):
        pv = float(input_pv)
        price = float(input_price)
        prediction = kms.predict([[pv, price]])[0]
        result = str(prediction)
        elif result ='0':
            st.write('Cluster 0 merupakan Cluster dimana Cluster dimana termasuk cluster Low Price Low Demand,Cluster tersebut merupakan dimana Pelanggan melakukan sedikit sekali  transaksi dengan harga barang yang relatif terjangkau,dimana Cluster ini dikisaran Rp 0 hingga Rp 490.000,00,dimana Cluster ini bisa terjadi karena banyak faktor,apakah mereka merupakan pelanggan baru,dimana mereka masih mencoba dengan membeli produk HNI untuk pertama kalinya,apakah mereka pelanggan yang berada di luar kota,sehingga lebih memilih beli di tempat yang relatif dengan mereka')
        elif result ='1':
            st.write('Cluster 1 merupakan Cluster dimana Cluster dimana termasuk cluster Medium, Cluster tersebut merupakan dimana Pelanggan melakukan sedikit sekali  transaksi dengan harga barang yang relatif terjangkau dimana Cluster ini dikisaran Rp 491.000,00 hingga Rp 965.000,00,dimana Cluster ini bisa terjadi karena banyak faktor,apakah mereka pelanggan yang berada di luar kota,sehingga lebih memilih beli di tempat yang relatif dengan mereka,atau apakah pelanggan lama dimana sering melakukan transaksi akan tetapi dengan kuantitas dan harga barang yang terjangkau')
        elif result ='2':
            st.write('Cluster 2 merupakan Cluster dimana Cluster dimana termasuk cluster High Price,High Demands,dimana Cluster tersebut merupakan dimana Pelanggan melakukan sering sekali melakukan transaksi dengan kuantitas yang tergolong banyak dalam sekali transaksi dimana Cluster ini dikisaran > Rp 1.000.000,00,dimana Cluster ini bisa terjadi karena Pelanggan sering melakukan transaksi kuantitas yang cukup banyak dengan sekali transaksi,dan termasuk pelanggan yang konsisten beli di cabang tersebut')
    else:
        result = "Please complete form above!"
    
st.subheader(f"Prediction : {result}")
