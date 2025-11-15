import streamlit as st
import pandas as pd
import mysql.connector

# -----------------------------
# Optional: MySQL Connection
# -----------------------------
# Uncomment and adjust if database exists
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Password",
#     database="uses",
#     autocommit=True
# )
# mycursor = mydb.cursor()

# -----------------------------
# App Title
# -----------------------------
st.title('Welcome to Maramath')

# -----------------------------
# LOGIN SECTION
# -----------------------------
st.header("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

correct_username = "admin"
correct_password = "12345"

if st.button("Signin"):
    if username == correct_username and password == correct_password:
        st.success(f"Welcome, {username}! ✅")

        st.subheader('Query Registration')

        # Use form correctly with 'with' block
        with st.form('registration_form'):
            query_id = st.text_input('Query ID')
            client_email = st.text_input('Client Email')
            client_mobile = st.text_input('Client Mobile')
            query_heading = st.text_input('Query Heading')
            query_description = st.text_area('Query Description')
            status = st.text_input('Status')
            date_raised = st.date_input('Date Raised')
            date_closed = st.date_input('Date Closed')

            submit_button = st.form_submit_button(label='Submit Query')

        if submit_button:
            form_data_1 = {
                'Query ID': query_id,
                'Client Email': client_email,
                'Client Mobile': client_mobile,
                'Query Heading': query_heading,
                'Query Description': query_description,
                'Status': status,
                'Date Raised': date_raised,
                'Date Closed': date_closed
            }

            df1 = pd.DataFrame([form_data_1])
            st.write("Here are your details:")
            st.table(df1)

            # Example: Insert into MySQL (if connected)
            # mycursor.execute("""
            #     INSERT INTO queries (query_id, client_email, client_mobile, query_heading,
            #                          query_description, status, date_raised, date_closed)
            #     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            # """, (query_id, client_email, client_mobile, query_heading,
            #       query_description, status, date_raised, date_closed))
            # mydb.commit()

    else:
        st.error("Invalid username or password ❌")

# -----------------------------
# SIGNUP SECTION
# -----------------------------
st.markdown("---")
st.header("Not a Member? Sign Up")

with st.form(key='SignUp'):
    name = st.text_input("Name")
    email = st.text_input("Email")
    mobile_number = st.text_input("Mobile Number")
    password_signup = st.text_input("Password", type="password")
    gender = st.radio("Gender", ("Male", "Female", "Other"))
    user_type = st.radio("User Type", ("Client", "Support"))
    country = st.selectbox("Country", ["India"])

    SignUp_button = st.form_submit_button(label='Sign Up')

if SignUp_button:
    if st.radio='client':
     form_data_2 = {
        'Name': name,
        'Email': email,
        'Mobile Number': mobile_number,
        'Password': password_signup,
        'Gender': gender,
        'User Type': user_type,
        'Country': country

     df2 = pd.DataFrame([form_data_2])

     st.success("SignUp Successful! 🎉")
     st.write("Here are your details:")
     st.table(df2)
     }
    else:

    # Example: Insert into MySQL (if connected)
    # mycursor.execute("""
    #     INSERT INTO users (name, email, mobile, password, gender, user_type, country)
    #     VALUES (%s, %s, %s, %s, %s, %s, %s)
    # """, (name, email, mobile_number, password_signup, gender, user_type, country))
    # mydb.commit()
