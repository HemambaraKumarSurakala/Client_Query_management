import streamlit as st
Name = st.text_input('Enter your name: ')
if st.button('Click'):
    st.write(Name)
Address=st.text_area('Address')
st.write(Address)
st.date_input('Pick a Date')
st.time_input('select a time')
if st.checkbox('accept terms & conditions'):
    st.write('Thank You')  
r=st.radio('color',['R', 'y', 'B','G'])      