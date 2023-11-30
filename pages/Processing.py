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
        
    else:
        result = "Please complete form above!"
    
st.subheader(f"Prediction : {result}")
