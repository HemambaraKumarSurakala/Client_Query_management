👥 User Authentication


Secure signup with SHA-256 password hashing


Login with role detection


Supports two roles:


Client


Support Team




🧑‍💻 Client Dashboard


Submit new queries


View previously submitted queries


Track query status (Open / Closed)


🛠️ Support Dashboard


View all client queries


Close queries and update closure date


🗄️ Database
Automatically creates required tables:


users


client_queries



🏗️ Project Structure
├── app.py    # Main Streamlit application
└── README.md # Documentation


🛢️ MySQL Database Schema
Users Table
CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(50) PRIMARY KEY,
    hashed_password VARCHAR(100),
    role VARCHAR(20)
);

Client Queries Table
CREATE TABLE IF NOT EXISTS client_queries (
    query_id INT AUTO_INCREMENT PRIMARY KEY,
    client_email VARCHAR(100),
    client_mobile VARCHAR(20),
    query_heading VARCHAR(100),
    query_description TEXT,
    status VARCHAR(20),
    date_raised DATETIME,
    date_closed DATETIME
);


🧰 Tech Stack
ComponentTechnologyFrontendStreamlitBackendPythonDatabaseMySQLSecuritySHA-256 Password Hashing

⚙️ Installation & Setup
1️⃣ Install Python Dependencies
pip install streamlit mysql-connector-python pandas

2️⃣ Create MySQL Database
Open MySQL and run:
CREATE DATABASE query_management;

3️⃣ Update Database Credentials
Modify inside the code:
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YourPassword",
    database="query_management"
)

4️⃣ Run the Application
streamlit run app.py


🔐 Security Notes


Passwords are stored using SHA-256 hashing.


SQL queries use prepared statements to avoid SQL injection.


📄 License
This project is open-source and free to use for learning or development.

