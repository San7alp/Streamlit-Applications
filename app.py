import streamlit as st


st.title('Hello World')
st.title('Hello World')
st.code('for i in range(0,100):\n'
               '\tprint(i)\n')
st. title( 'Title -> GeeksForGeeks')
st. header ('Header > GeeksForGeeks')
st. subheader ('Subheader > GeeksForGeeks')
st. text ( 'Text -> GeeksForGeeks')
st.markdown ('# Hi')
st. success ('Success!')
st. info( 'Information!')
st.warning ( 'Warning!')
st.error('Error!')
st. exception (ZeroDivisionError( 'Div not possible'))

st.help(ZeroDivisionError)

st.write("range (1,10)")
st.write(range(1,10))
st.write (1*2*3)

st. code('x = 10\n'
    'for i in range(x) :\n'
    '\tprint (i)')

if(st.checkbox ('Male' )):
    st.write('You re Male')
if(st. checkbox ('Adult')):
    st.write('You are an adult')

st. subheader ('Radio Button' )
radioButton = st. radio( 'Select : ', ('Male', 'Female', 'Other'))
if(radioButton == 'Male'):
   st.write("You're a Male")
elif(radioButton == 'Female'):
    st. write("You're a Female")
elif(radioButton == 'Other'):
    st.write("You're an Other Gender")

# Radio Button
st. subheader ('Select Box')
# SelectBox
selectBox = st. selectbox("Data Science: ", [ 'Data Analsis', 'Web Scraping', 'Machine Learning',
'Deep Learning', 'Natural Language Processing',
'Computer Vision', 'Image Processing '])
st. write("You've selected: ", selectBox)
st. subheader ( 'MultiSelect Box')
# MultiSelectBox
multiSelBox = st. multiselect ("Data Science: ", [ 'Data Analsis', 'Web Scraping', 'Machine Learning',
'Deep Learning', 'Natural Language Processing',
'Computer Vision', 'Image Processing' ])

st. subheader ("Button" )
if(st. button ('Click me' )):
    st.write( 'Thanks for clicking me')
st. subheader ("Slider")
vol = st. slider ('Select the volume' ,0, 100, step = 1)
st.write( 'Volume is : ',vol)
st. subheader ("Text Input")
username = st.text_input ( 'Username : ')
password = st. text_input( 'Password: ', type = 'password')
st. subheader ("Text Area")
st. text_area ('Write something interesting about yourself')
st. subheader ("Input Number")
st. number_input( 'Select your age', 18,110)
st. subheader ("Input Date")
st. date_input ('Date')
st. subheader ("Input Time")
st.time_input('Time')


