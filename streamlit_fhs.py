import streamlit as st
import joblib
import pandas as pd

col1, col2, col3 = st.columns(3)

#getting user input
# 
gender = col1.selectbox("Cinsiyetinizi girin",["Erkek", "Female"])

age = col2.number_input("Yaşınızı girin")
education = col3.selectbox("Öğrenim durumunuz",["Lise", "Lisans", " Yüksek Lisans", "Doktora"])

isSmoker = col1.selectbox("Şu anda sigara içiyor musunuz?",["Evet","No"])

yearsSmoking = col2.number_input("Günlük sigara sayısı")

BPMeds = col3.selectbox("Tansiyon ilacı kullanıyor musunuz?",["Evet","No"])

stroke = col1.selectbox("Hiç felç geçirdiniz mi?",["Evet","No"])

hyp = col2.selectbox("Hipertansiyonunuz var mı?",["Evet","No"])

diabetes = col3.selectbox("Şeker hastalığınız var mı?",["Evet","No"])

chol = col1.number_input("Kolesterol değerini girin")

sys_bp = col2.number_input("Sistolik kan basıncınızı girin")

dia_bp = col3.number_input("Diyastolik kan basıncınızı girin")

bmi = col1.number_input("Beden-Kitle-İndeksi girin")

heart_rate = col2.number_input("İstarahat Kalp Atış hızını girin")

glucose = col3.number_input("Şeker değerinizi girin")



df_pred = pd.DataFrame([[gender,age,education,isSmoker,yearsSmoking,BPMeds,stroke,hyp,diabetes,chol,sys_bp,dia_bp,bmi,heart_rate,glucose]],

columns= ['gender','age','education','currentSmoker','cigsPerDay','BPMeds','prevalentStroke','prevalentHyp','diabetes','totChol','sysBP','diaBP','BMI','heartRate','glucose'])

df_pred['gender'] = df_pred['gender'].apply(lambda x: 1 if x == 'Erkek' else 0)

df_pred['prevalentHyp'] = df_pred['prevalentHyp'].apply(lambda x: 1 if x == 'Evet' else 0)

df_pred['prevalentStroke'] = df_pred['prevalentStroke'].apply(lambda x: 1 if x == 'Evet' else 0)

df_pred['diabetes'] = df_pred['diabetes'].apply(lambda x: 1 if x == 'Evet' else 0)

df_pred['BPMeds'] = df_pred['BPMeds'].apply(lambda x: 1 if x == 'Evet' else 0)

df_pred['currentSmoker'] = df_pred['currentSmoker'].apply(lambda x: 1 if x == 'Evet' else 0)


def transform(data):
    result = 3
    if(data=='Lise'):
        result = 0
    elif(data=='Lisans'):
        result = 1
    elif(data=='Yüksek Lisans'):
        result = 2
    return(result)
    
    
df_pred['education'] = df_pred['education'].apply(transform)


model = joblib.load('fhs_rf_model.pkl')
prediction = model.predict(df_pred)


if st.button('Tahmin et!'):

    if(prediction[0]==0):
        st.write('<p class="big-font">Muhtemelen 10 yıl içinde kalp hastalığı geliştirmeyeceksiniz..</p>',unsafe_allow_html=True)

    else:
        st.write('<p class="big-font">10 yıl içinde kalp hastalığı geliştirmeniz muhtemeldir.</p>',unsafe_allow_html=True)

