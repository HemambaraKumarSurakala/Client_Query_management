import streamlit as st
import pandas as pd
# Title of the form

import mysql.connector

#SQL Connection
mydb = mysql.connector.connect(
       host = "localhost",
        user = "root",
        password = "Password",
        database='DataBase',
        autocommit = True)
mycursor = mydb.cursor()


st.title("Registration Form")
# Create the form
form = st.form(key='registration_form')
# Input fields
name = form.text_input("Name")
email = form.text_input("Email")
password = form.text_input("Password", type="password")
dob = form.date_input("Date of Birth")
gender = form.radio("Gender", ("Male", "Female", "Other"))
country = form.selectbox("Country", ["United States", "Canada", "United Kingdom", "Australia", "Other"])
# Form submit button
submit_button = form.form_submit_button(label='Register')
# If the form is submitted
if submit_button:
    # Create a dictionary with the form data
    form_data = {
        'Name': name,
        'Email': email,
        'Password': password,
        'Date of Birth': dob,
        'Gender': gender,
        'Country': country
    }
    
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame([form_data])
    
    # Display a success message
    st.success("Registration Successful!")
    
    # Display the form data as a table
    st.write("Here are your details:")
    st.table(df)
    insert_query = """
    INSERT INTO registrations (name, email, password, dob, gender, country)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    data = (name, email, password, dob.strftime('%Y-%m-%d'), gender, country)
    mycursor.execute(insert_query,data)
    st.success('Data inserted to sql')


    sql = "select * from registrations"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    st.write(data)

