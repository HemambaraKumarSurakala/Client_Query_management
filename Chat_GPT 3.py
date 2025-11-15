import streamlit as st
import mysql.connector
import hashlib
import pandas as pd
from datetime import datetime

# -------------------- DATABASE CONNECTION --------------------
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",   # 👉 change this
    database="query_management" # 👉 ensure this DB exists
)
cursor = mydb.cursor()

# -------------------- CREATE TABLES IF NOT EXIST --------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(50) PRIMARY KEY,
    hashed_password VARCHAR(100),
    role VARCHAR(20)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS client_queries (
    query_id INT AUTO_INCREMENT PRIMARY KEY,
    client_email VARCHAR(100),
    client_mobile VARCHAR(20),
    query_heading VARCHAR(100),
    query_description TEXT,
    status VARCHAR(20),
    date_raised DATETIME,
    date_closed DATETIME
)
""")
mydb.commit()

# -------------------- STREAMLIT APP --------------------
st.title("📞 Client Query Management System")

# Track page navigation
if "page" not in st.session_state:
    st.session_state.page = "login"

# -------------------- SIGNUP PAGE --------------------
if st.session_state.page == "signup":
    st.subheader("📝 Signup Form")

    new_username = st.text_input("Choose Username")
    new_password = st.text_input("Choose Password", type="password")
    role = st.selectbox("Select Role", ["Client", "Support"])

    if st.button("Register"):
        if new_username and new_password:
            hashed_pw = hashlib.sha256(new_password.encode()).hexdigest()
            try:
                cursor.execute("INSERT INTO users VALUES (%s, %s, %s)", (new_username, hashed_pw, role))
                mydb.commit()
                st.success("✅ Signup Successful! You can now log in.")
                st.session_state.page = "login"
            except:
                st.error("❌ Username already exists.")
        else:
            st.warning("Please fill all fields.")

    st.button("⬅️ Back to Login", on_click=lambda: st.session_state.update(page="login"))

# -------------------- LOGIN PAGE --------------------
elif st.session_state.page == "login":
    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        hashed_pw = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute("SELECT role FROM users WHERE username=%s AND hashed_password=%s", (username, hashed_pw))
        result = cursor.fetchone()

        if result:
            role = result[0]
            st.success(f"✅ Logged in as {role}")
            if role == "Client":
                st.session_state.page = "client"
                st.session_state.username = username
            elif role == "Support":
                st.session_state.page = "support"
                st.session_state.username = username
        else:
            st.error("❌ Invalid credentials.")

    st.write("Don't have an account?")
    st.button("📝 Signup", on_click=lambda: st.session_state.update(page="signup"))

# -------------------- CLIENT PAGE --------------------
elif st.session_state.page == "client":
    st.subheader(f"👤 Welcome, {st.session_state.username} (Client)")

    email = st.text_input("Email ID")
    mobile = st.text_input("Mobile Number")
    heading = st.text_input("Query Heading")
    description = st.text_area("Query Description")

    if st.button("Submit Query"):
        if email and mobile and heading and description:
            now = datetime.now()
            cursor.execute("""
                INSERT INTO client_queries (client_email, client_mobile, query_heading, query_description, status, date_raised, date_closed)
                VALUES (%s, %s, %s, %s, %s, %s, NULL)
            """, (email, mobile, heading, description, "Open", now))
            mydb.commit()
            st.success("✅ Query submitted successfully!")
        else:
            st.warning("Please fill all fields.")

    st.write("View your submitted queries:")
    cursor.execute("SELECT query_id, query_heading, status, date_raised, date_closed FROM client_queries WHERE client_email=%s", (email,))
    rows = cursor.fetchall()

    if rows:
        df = pd.DataFrame(rows, columns=["Query ID", "Heading", "Status", "Raised", "Closed"])
        st.dataframe(df)
    else:
        st.info("No queries found.")

    st.button("🔒 Logout", on_click=lambda: st.session_state.update(page="login"))

# -------------------- SUPPORT PAGE --------------------
elif st.session_state.page == "support":
    st.subheader(f"🧑‍💼 Welcome, {st.session_state.username} (Support Team)")

    st.write("View and manage all client queries:")

    cursor.execute("SELECT * FROM client_queries")
    data = cursor.fetchall()
    if data:
        df = pd.DataFrame(data, columns=["Query ID", "Email", "Mobile", "Heading", "Description", "Status", "Raised", "Closed"])
        st.dataframe(df)
    else:
        st.info("No queries in the system yet.")

    query_id = st.text_input("Enter Query ID to close:")
    if st.button("Close Query"):
        now = datetime.now()
        cursor.execute("UPDATE client_queries SET status='Closed', date_closed=%s WHERE query_id=%s", (now, query_id))
        mydb.commit()
        st.success(f"✅ Query {query_id} marked as Closed.")

    st.button("🔒 Logout", on_click=lambda: st.session_state.update(page="login"))
