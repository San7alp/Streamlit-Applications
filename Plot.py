import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
chart_data = pd. DataFrame(np. random. randn(20,3), columns = ['Line-1', 'Line-2', 'Line-3'])
st.title('Charts with Random Number')
st. subheader('Line Chart')
st. line_chart(chart_data)
st. subheader('Area Chart')
st.area_chart(chart_data)
st. subheader('Bar Chart')
st.bar_chart(chart_data)

st.header("Data Visualization with Matplotlib and Seaborn")
df1= pd.read_excel(r'C:\Users\KIIT\Desktop\Data Analytics\DA_CLASS_2.xlsx')
st.subheader('The DataFrame')
st.dataframe(df1)

st.header("Data Visualization with Matplotlib and Seaborn")
df = pd.read_csv(r'C:\Users\KIIT\PycharmProjects\Py projects\iris.csv')
st.subheader('The DataFrame')
st.dataframe(df)

st.subheader("Bar graph using matplotlib")
fig=plt.figure(figsize=(18,5))
df['variety'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader("Bar graph using Seaborn")
fig1=plt.figure(figsize=(18,5))
sns.distplot(df['sepal.length'])
st.pyplot(fig1)

st.header ('3. Multiple Graphs in one columns')
col1, col2 = st. columns (2)
with col1:
    col1.header = 'KDE = False'
    fig1 = plt. figure(figsize = (5,5))
    sns.distplot(df['sepal.length'], kde = False)
    st.pyplot(fig1)
with col2:
    col2. header = 'Hist = False'
    fig2 = plt. figure(figsize = (5,5))
    sns.distplot(df ['sepal.length'], hist = False)
    st.pyplot (fig2)
st.header ('4. Changing Style')
col1, col2 = st. columns (2)
with col1:
    fig= plt. figure()
    sns. set_style( 'darkgrid')
    sns. set_context ( 'notebook' )
    sns.distplot(df['petal.length'],hist = False)
    st.pyplot(fig)
with col2:
    col2.header = 'Hist = False'
    fig2 = plt. figure(figsize = (5,5))
    sns.distplot(df ['sepal.length'], hist = False)
    st.pyplot (fig2)

st. header('5. Exploring Different Graphs')
st. subheader('5.1 Scatter Plot')
fig, ax=plt.subplots(figsize=(15,8))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)
st. subheader('5.2 Count-Plot')
fig = plt. figure(figsize=(15,8))
sns. countplot(data=df, x='variety')
st.pyplot(fig)
st. subheader('5.3 Box-Plot')
fig = plt.figure(figsize=(15,8))
sns. boxplot(data=df, x='variety', y='petal.length')
st. pyplot(fig)
st. subheader('5.4 Violin-Plot')
fig = plt. figure(figsize=(15,8))
sns.violinplot(data=df, x ='variety', y='petal.length')
st. pyplot(fig)


