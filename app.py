#import libraries
st.balloons()
import streamlit as st

#matplotlib.use('Agg')

import pickle

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Crop Recommendation")
pickle_in = open('RandomForest.pkl', 'rb')
classifier = pickle.load(pickle_in)

st.sidebar.header('Team Cygnus')
select = st.sidebar.selectbox('Choose option', ['crop recommendation','Disease Detection'], key='1')
#if not st.sidebar.checkbox("Hide", True, key='1'):
st.text("You can enter the field to get the suitable crop recomendation")


#from PIL import Image 
#img = Image.open("logo.png")
#st.image(img,width=300,caption='Streamlit Images')
st.text("Enter the soil compositions")

n = st.number_input('Nitrogen',5,100)

p = st.number_input('Phosphorous',5,100)

po = st.number_input('Pottasium',5,100)

ph = st.number_input('ph level',5,15)

r = st.number_input('Rainfall (in mm)',5,100)

temp = st.number_input('Normal Temperature (°C)',5,100)

h = st.number_input('Average Humidity (%rh)',5,100)
#st.write("You are in level",level)
import datetime,time
today = st.date_input("Expected time",datetime.datetime.now())

submit = st.button('Predict')

if submit:
    prediction = classifier.predict([[n,p,po,temp,h,ph,r]])
    st.write('Most suitable crop will be : ')
    st.success(prediction)
