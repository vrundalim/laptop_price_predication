import streamlit as st
import pickle as pk
import pandas as pd
from sklearn.preprocessing import LabelEncoder

model = pk.load(open('model1.pkl','rb'))
scaler = pk.load(open('scaler.pkl','rb'))
st.header("Laptop Price Prediction")
Company = st.selectbox('Choose the Company Name',['Apple', 'HP', 'Acer', 'Asus', 'Dell', 'Lenovo', 'Chuwi', 'MSI','Microsoft', 'Toshiba', 'Huawei', 'Xiaomi', 'Vero', 'Razer','Mediacom', 'Samsung', 'Google', 'Fujitsu', 'LG'])
TypeName = st.selectbox('Choose the TypeName',['Ultrabook', 'Notebook', 'Netbook', 'Gaming', '2 in 1 Convertible','Workstation'])
Inches = st.slider('Choose the Inches',0,20)
Ram_GB = st.slider('Choose the Ram(GB)',0,64)
OpSys =st.selectbox('Choose the Operating System',['macOS', 'No OS', 'Windows 10', 'Mac OS X', 'Linux', 'Android','Windows 10 S', 'Chrome OS', 'Windows 7'])
Weight_kg = st.slider('Choose the Weight of Laptop',0,5)
Preprocessor = st.selectbox('Choose the Preprocessor',['Intel Core i5', 'Intel Core i7', 'Others', 'Intel Core i3'])
Screen_width =st.slider('Choose the width',0,4000)
Screen_height = st.slider('Choose the Height',0,2300)
Full_HD = st.selectbox('Full HD',['False','True'])
IPS  = st.selectbox('IPS',['False','True'])
Touchscreen = st.selectbox('Touchscreen',['False','True'])
Quad_HD = st.selectbox('Quad HD+',['False','True'])
Ultra_HD = st.selectbox('4K Ultra HD',['False','True'])
Gpu_Brand = st.selectbox('Gpu_Brand',['Intel', 'AMD', 'Nvidia', 'ARM'])
SSD = st.slider('Choose the SSD',0,1500)
HDD = st.slider('Choose the HDD',0,1500)
Flash_Storage = st.slider('Choose the Flash_Storage',0,1500)
Hybrid = st.slider('Choose the Hybrid',0,1500)
if Full_HD == "True" :
    Full_HD_s = 1
else:
    Full_HD_s = 0
if IPS == "True" :
    IPS_s = 1
else:
    IPS_s = 0
if Touchscreen == "True" :
    Touchscreen_s = 1
else:
    Touchscreen_s = 0
if Quad_HD == "True" :
    Quad_HD_s = 1
else:
    Quad_HD_s = 0
if Ultra_HD == "True" :
    Ultra_HD_s = 1
else:
    Ultra_HD_s = 0

if st.button("Predict"):
   pred_data = pd.DataFrame([[Company, TypeName, Inches, Ram_GB, OpSys, Weight_kg,Preprocessor, Screen_width, Screen_height, Full_HD_s, IPS_s,Touchscreen_s, Quad_HD_s, Ultra_HD_s, Gpu_Brand, SSD, HDD,Flash_Storage, Hybrid]],columns=['Company', 'TypeName', 'Inches', 'Ram_GB', 'OpSys', 'Weight_kg','Preprocessor', 'Screen_width', 'Screen_height', 'Full_HD', 'IPS','Touchscreen', 'Quad_HD', 'Ultra_HD', 'Gpu_Brand', 'SSD', 'HDD','Flash_Storage', 'Hybrid'])
   pred_data['Company'] = LabelEncoder().fit_transform(pred_data['Company'])
   pred_data['TypeName'] = LabelEncoder().fit_transform(pred_data['TypeName'])
   pred_data['OpSys'] = LabelEncoder().fit_transform(pred_data['OpSys'])
   pred_data['Preprocessor'] = LabelEncoder().fit_transform(pred_data['Preprocessor'])
   pred_data['Gpu_Brand'] = LabelEncoder().fit_transform(pred_data['Gpu_Brand'])
   pred_data = scaler.transform(pred_data)
   predict = model.predict(pred_data)
   st.success(f"Estimated Laptop Price(RS): {predict[0]}")