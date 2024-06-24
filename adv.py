import time
import numpy as np
import pandas as pd
import streamlit as st
cases = []
for i in range(100):
    cases.append(np.random.randint(1,7))
data = []
for i in range(1,7):
    data.append(cases.count(1))
st.header("Frequency of getting a Face ")
st.bar_chart({'data' : data})
with st.expander('See Explanation'):
    st.write('''The chart shows some numbers I got from rolling a dice 100 times and its
         basically about how many times each face appears''')

st.image("https://static.streamlit.io/exanples/dice.jpg")
with st.spinner('Wait for it'):
    time.sleep(5)
    st.write('Thanks for being patient')