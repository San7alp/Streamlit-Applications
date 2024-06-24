import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Line Chart")
chart=pd.DataFrame(np.random.randn(20,3),columns=["L1","L2","L3"])
st.line_chart(chart)
st.title("Area Chart")
st.area_chart(chart)
st.title("Bar Chart")
st.bar_chart(chart)

st.title("Data Visualization using sns and plt")
df =pd.read_csv('iris.csv')
st.dataframe(df)

st.text('2. Bar Plot using Matplotlib')
fig = plt.figure(figsize=(15,8))
df['variety'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.text('3. DistPlot with Seaborn')
fig = plt.figure(figsize = (15,8))
sns.distplot(df['sepal.length'])
st.pyplot(fig)

st.text('4. Display Multiple Graphs')
col1,col2 = st.columns(2)
with col1:
    col1.header('KDE = False')
    col1.write('KDE = False')
    fig1 = plt.figure()
    sns.distplot(df['sepal.length'],kde = False)
    st.pyplot(fig1)
with col2:
    col2.header('KDE = False')
    col2.write('KDE = False')
    fig2 = plt.figure()
    sns.distplot(df['sepal.length'],kde = False)
    st.pyplot(fig2)

st.text('6. Scatter Plot')
fig,ax = plt.subplots(figsize=(15,8))
ax.scatter(*np.random.random(size = (2,1000)))
st.pyplot(fig)

st.text('7. Count Plot')
fig = plt.figure(figsize = (15,8))
sns.countplot(data = df,x='variety')
st.pyplot(fig)

st.text('8. Box Plot')
fig = plt.figure(figsize = (15,8))
sns.boxplot(data = df, x = 'variety', y = 'petal.length')
st.pyplot(fig)

st.text('9. Violin Plot')
fig = plt.figure(figsize = (15,8))
sns.violinplot(data = df, x = 'variety', y = 'petal.length')
st.pyplot(fig)