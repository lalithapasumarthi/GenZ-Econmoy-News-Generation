import streamlit as st
import sqlite3
import os

# Class for interacting with the database
class Database:
    @staticmethod
    def path():
        current_directory = os.path.dirname(os.path.abspath(__file__))
        db_name = 'database_1.db'
        file_path = os.path.join(current_directory, db_name)
        return file_path

    @staticmethod
    def db_select():
        file_path = Database.path()
        conn = sqlite3.connect(file_path)
        cursor = conn.cursor()
        sql = 'SELECT * FROM entry ORDER BY id DESC'
        cursor.execute(sql)
        record = cursor.fetchall()
        conn.close()
        return record

# Function to render the web page
def render_page():
    st.markdown("<h1 style='text-align: center; font-size: 48px;'>Welcome to Gen Z Economy News</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Latest Posts</h2>", unsafe_allow_html=True)

    # Add data to the database
    record_set = Database.db_select()

    # Define background colors
    colors = ['#f9f9f9', '#e9e9e9']
    
    # Create a feed of previous posts
    for idx, record in enumerate(record_set):
        bg_color = colors[idx % 2]
        st.markdown(f"<div style='background-color: {bg_color}; padding: 10px; border-radius: 5px;'>", unsafe_allow_html=True)
        st.subheader(record[4])
        st.markdown(record[5], unsafe_allow_html=True)
        st.markdown("</div><br>", unsafe_allow_html=True)

if __name__ == "__main__":
    render_page()
