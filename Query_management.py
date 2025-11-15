import streamlit as st
import pandas as pd
# Title of the form

import mysql.connector

#SQL Connection
mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Password",
        database='Query_management',
        autocommit = True)
#mycursor = mydb.cursor()

st.title ('Welcome to Maramath')

# Set page title
st.title("Login")
#User=form.radio('User', ('client', 'Support'))
# Input fields
username = st.text_input("Username")
password = st.text_input("Password", type="password")
user_type = st.radio("User Type", ("Client", "Support"))
#client=form.radio('Client')
#Support=form.radio('Support')
# Define correct credentials (for demo only)
correct_username = "admin"
correct_password = "12345"
button = st.button(label='Login')

# Login button
if st.button("Login"):
    if username == correct_username and password == correct_password:
        {
         if user_type == 'Client':
           st.success(f"Welcome, {username}! ✅")
           form= st.form('registration_form')
           form=st.text_input('query_id')
           form=st.text_input('client_email')
           form=st.text_input('client_mobile')
           form=st.text_input('query_heading')
           form=st.text_input('query_description')
           form=st.text_input('query_status')
           form=st.text_input('date_raised')
           form=st.text_input('date_closed')
        }
st.button = form.form_submit_button(label='Submit Query')
       # }
       # if st.button:
        #  form_data_1={
         #          'query_id':query_id,
          #         'client_email':client_email,
           #        'client_mobile':client_mobile,
            #       'query_heading':query_heading,
             #      'query_description':query_description,
              #     'query_status':status,
               #    'date_raised': date_raised,
                #   'date_closed': date_closed,
df1 = pd.DataFrame([form_data_1])
st.write("Here are your details:")
st.table(df1)
        
        #else:    

           
    else:
        st.error("Invalid username or password ❌")
            #Query submission form

st.write('Not a Member ? SignUp')
st.button('SignUp')
form = st.form(key='SigUp')
# Input fields
name = form.text_input("Name")
email = form.text_input("Email")
Mobile_Number = form.text_input("Date of Birth")
password = form.text_input("Password", type="password")
gender = form.radio("Gender", ("Male", "Female", "Other"))
User= form.radio('User', ('Client', 'Support'))
country = form.selectbox("Country", ["India"])
# Form submit button
SignUp_button = form.form_submit_button(label='SignUp')
# If the form is submitted
if SignUp_button:
    # Create a dictionary with the form data
    form_data2 = {
        'Name': name,
        'Email': email,
        'Mobile_number': Mobile_Number,
        'Password': password,
        'Gender': gender,
        'User': User,
        'Country': country
    }
    
    # Convert the dictionary to a DataFrame
    df2 = pd.DataFrame([form_data2])
    
    # Display a success message
    st.success("SignUp Successful!")
    
    # Display the form data as a table
    st.write("Here are your details:")
    st.table(df2)
