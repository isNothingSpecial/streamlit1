import streamlit as st
import pandas as pd # Pandas (version : 1.1.5) 
import numpy as np # Numpy (version : 1.19.2)
import matplotlib.pyplot as plt # Matplotlib (version :  3.3.2)
from sklearn.cluster import KMeans # Scikit Learn (version : 0.23.2)
import seaborn as sns # Seaborn (version : 0.11.1)

## data

df = pd.read_csv('Laporan_Penjualan1.csv')

df_proc = pd.read_csv('cleandata.csv')



st.set_page_config(page_title="Homepage",layout="wide")
#side bar
#st.sidebar.header("Segmentasi Pelanggan Produk HNI")
#st.sidebar.image("1835901.jpg")

##layout

st.title(''' SEGMENTASI PELANGGAN PEMEMBELIAN PRODUK HALAL NETWORK INTERNATIONAL (HNI) DENGAN MENGGUNAKAN ALGORITMA K-MEANS ''')
st.write('''
        ''')
st.markdown('''Aplikasi adalah berupa pengsegmentasian pelanggan,dan Kali ini,akan menganalisa data penjualan produk HNI di suatu cabang PT HPAI di kec Tunggulrejo,Kabupaten Purworejo,dimana mulai buka pada tahun 2021,dan data yang dianalisa hingga periode September 2023

Berikut adalah data Penjualannya ''')

st.write(df)
st.markdown('''Data diatas masih berupa RAW data,yang mana nantinya akan diolah melalui beberapa proses data Preprocessing antara lain:  
            - Menghapus kolom yang tidak diperlukan  
            - Mengubah Nama Kolom Customer Name menjadi Customer_Name 
            - Grouping berdasar Kolom Customer_Name  
            - Ditampilkan dalam bentuk diagram
            - Pemrosesan dengan menggunakan algoritma K Means
            - Penampilan data yang sudah ter Clusterisasi
            - Pengesampingan Outliers
            - Pengulangan metode sebelumnya
        
Berikut adalah contoh data yang sudah di Grouping berdasar Kolom Customer_Name: ''')

st.write(df_proc)


df_clusters = pd.read_csv('finaldata.csv')

kms = KMeans(n_clusters=3, init='k-means++')
kms.fit(df_clusters)

clusters = df_clusters.copy()
clusters['Cluster_Prediction'] = kms.fit_predict(df_clusters)
st.write((clusters))

st.write('Berikut adalah Centroid dari masing-masing Clusters')
kms.cluster_centers_

fig, ax = plt.subplots(figsize=(15,7))


plt.scatter(x=clusters[clusters['Cluster_Prediction'] == 0]['SUM Price'],
            y=clusters[clusters['Cluster_Prediction'] == 0]['SUM PV'],
            s=70,edgecolor='black', linewidth=0.3, c='deepskyblue', label='Cluster 1')

plt.scatter(x=clusters[clusters['Cluster_Prediction'] == 1]['SUM Price'],
            y=clusters[clusters['Cluster_Prediction'] == 1]['SUM PV'],
            s=70,edgecolor='black', linewidth=0.3, c='magenta', label='Cluster 2')

plt.scatter(x=clusters[clusters['Cluster_Prediction'] == 2]['SUM Price'],
            y=clusters[clusters['Cluster_Prediction'] == 2]['SUM PV'],
            s=70,edgecolor='black', linewidth=0.3, c='red', label='Cluster 3')



plt.scatter(x=kms.cluster_centers_[:, 0], y=kms.cluster_centers_[:, 1], s = 120, c = 'yellow', label = 'Centroids',edgecolor='black', linewidth=0.3)
plt.legend(loc='upper right')

plt.xlabel('Akumulasi Harga Barang yang Telah Dibeli')
plt.ylabel('Akumulasi Point Value yang Didapat')
plt.title('Clusters', fontsize = 20)
plt.show()
