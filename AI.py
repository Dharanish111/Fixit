import streamlit as st
import bcrypt
import sqlite3
from datetime import datetime
from AI1 import ai_page

# Create database connection and cursor
conn = sqlite3.connect('users.db', check_same_thread=False)
c = conn.cursor()

# Function to check if a btnumn exists in a table
def btnumn_exists(cursor, table_name, btnumn_name):
    cursor.execute(f"PRAGMA table_info({table_name})")
    btnumns = cursor.fetchall()
    for btnumn in btnumns:
        if btnumn_name == btnumn[1]:
            return True
    return False

# Add security_question and security_answer btnumns if they don't exist
if not btnumn_exists(c, 'users', 'security_question'):
    c.execute('ALTER TABLE users ADD btnUMN security_question TEXT')
if not btnumn_exists(c, 'users', 'security_answer'):
    c.execute('ALTER TABLE users ADD btnUMN security_answer TEXT')

# Function to register a user
def register_user(username, password, security_question, security_answer):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    hashed_answer = bcrypt.hashpw(security_answer.encode(), bcrypt.gensalt())
    c.execute('INSERT INTO users (username, password, date_joined, security_question, security_answer) VALUES (?, ?, ?, ?, ?)', 
              (username, hashed_password, datetime.now(), security_question, hashed_answer))
    conn.commit()

# Function to check login credentials
def check_login(username, password):
    c.execute('SELECT password FROM users WHERE username = ?', (username,))
    user = c.fetchone()
    if user and bcrypt.checkpw(password.encode(), user[0]):
        return True
    return False

# Function to reset password
def reset_password(username, security_answer, new_password):
    c.execute('SELECT security_answer FROM users WHERE username = ?', (username,))
    user = c.fetchone()
    if user and user[0] and bcrypt.checkpw(security_answer.encode(), user[0]):
        hashed_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
        c.execute('UPDATE users SET password = ? WHERE username = ?', (hashed_password, username))
        conn.commit()
        return True
    return False

# Function for registration page
def registration_page():
    st.title('User Registration')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    confirm_password = st.text_input('Confirm Password', type='password')
    security_question = st.text_input('Security Question')
    security_answer = st.text_input('Security Answer', type='password')
    btn1, btn2, btn3, btn4, btn5 = st.columns(5)
    
    with btn1:
        if st.button('Register'):
            if password == confirm_password:
                try:
                    register_user(username, password, security_question, security_answer)
                    st.success('User registered successfully!')
                    st.session_state['page'] = 'login'  # Redirect to login page after successful registration
                    st.experimental_rerun()
                except sqlite3.IntegrityError:
                    st.error('Username already exists')
            else:
                st.error('Passwords do not match')

    with btn2:
        if st.button('Go to Login'):
            st.session_state['page'] = 'login'
            st.experimental_rerun()

# Function for login page
def login_page():
    st.title('User Login')
    login_username = st.text_input('Username', key='login_username')
    login_password = st.text_input('Password', type='password', key='login_password')
    btn1, btn2, btn3, btn4 = st.columns(4)
    with btn1:
        if st.button('Login'):
            if check_login(login_username, login_password):
                st.success('Login successful!')
                st.session_state['logged_in'] = True
                st.session_state['username'] = login_username
                st.experimental_rerun()  # Rerun to show AI page
            else:
                st.error('Invalid username or password')
    with btn2:
        if st.button('Forgot Password'):
            st.session_state['page'] = 'forgot_password'
            st.experimental_rerun()

# Function for forgot password page
def forgot_password_page():
    st.title('Forgot Password')
    username = st.text_input('Username', key='forgot_username')
    security_answer = st.text_input('Security Answer', type='password', key='security_answer')
    new_password = st.text_input('New Password', type='password', key='new_password')
    confirm_new_password = st.text_input('Confirm New Password', type='password', key='confirm_new_password')
    if st.button('Reset Password'):
        if new_password == confirm_new_password:
            if reset_password(username, security_answer, new_password):
                st.success('Password reset successful!')
                st.session_state['page'] = 'login'  # Redirect to login page after successful reset
                st.experimental_rerun()
            else:
                st.error('Invalid username or security answer')
        else:
            st.error('Passwords do not match')

# Main function to control page flow
def main():
    # Initialize session state variables
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
        st.session_state['username'] = None  # Initialize username
    if 'page' not in st.session_state:
        st.session_state['page'] = 'registration'  # Start with registration page

    # Show the appropriate page
    if st.session_state['logged_in']:
        ai_page()  # Call the ai_page function
    elif st.session_state['page'] == 'registration':
        registration_page()
    elif st.session_state['page'] == 'login':
        login_page()
    elif st.session_state['page'] == 'forgot_password':
        forgot_password_page()

if __name__ == "__main__":
    main()
