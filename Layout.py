#import streamlit as st
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt

#data = {
 #   'num':[x for x in range(1,11)],
  #  'square': [x**2 for x in range(1,11)],
   # 'twice': [x*2 for x in range(1,11)],
    #'thrice':[x**3 for x in range(1,11)],
#}

#df=pd.DataFrame(data)
#st.write(df)

#col=st.sidebar.selectbox('select any number',df.columns)

#fig,ax=plt.subplots()
#ax.plot(df['num'],df[col])

#ax.set_title(f'plot of {col}vs num')
#ax.set_xlabel('num')
#ax.set_ylabel(col)

#st.pyplot(fig)


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#r=st.sidebar.radio('Navigation', ['Home', 'Operation'])
#data = {
 #   'num':[x for x in range(1,11)],
  #  'square': [x**2 for x in range(1,11)],
   # 'twice': [x*2 for x in range(1,11)],
    #'thrice':[x**3 for x in range(1,11)],
#}
#if r== 'Operation': 
 #df=pd.DataFrame(data)
 #st.write(df)

 #col=st.sidebar.selectbox('select any number',df.columns)

 #fig,ax=plt.subplots()
 #ax.plot(df['num'],df[col])

 #ax.set_title(f'plot of {col}vs num')
 #ax.set_xlabel('num')
 #ax.set_ylabel(col)

 #st.pyplot(fig)
#if r=='Home':
 #st. write('Welcome')
 #st.balloons()
 #st.success('Success!!!')
 #st.warning('Warning')
 #st.error('Error')
 #st.exception('Exception')
#st.title('Home')
#col1,col2= st.columns(2, gap='small')
#col1.image("D:\OIP.jpg")
#col2.image("D:\wp9040665.jpg")


import streamlit as st
import pandas as pd
# Title of the form



import mysql.connector

#SQL Connection
mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = ".........",
        database='uses',
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


    sql = "select * from registrations where name='Agatha'"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    st.table(data)

