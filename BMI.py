import streamlit as st
def bmi():
    st.title('BMI Calculator')
    with st.form('BMI Calculator'):
        col1, col2, col3=st.columns([3,2,1])
    with col1:
        weight=st.number_input('Enter your weight')
    with col2:
        height=st.number_input('Enter your height')
    with col3:
        s=st.form_submit_button('Calculate')
    if s:
        bmi=round((weight/(height**2)),2)
        st.write(bmi)
        if bmi<=18.5:
            st.error('Underweight')
        elif bmi>18.5 and bmi<=24.9:
            st.success("Healthy")
        else :
            st.warning("Overweight")

ch=st.sidebar.selectbox('Menu',['BMI'])
if ch=='BMI':
    bmi()


