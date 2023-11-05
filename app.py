import requests
import streamlit as st

# Set page title and layout
st.set_page_config(page_title="My Webpage", layout="wide")

# Add a button to send 'hi' with the 'trp' cookie
if st.button("Send 'hi' with Cookie"):
    post_data = {'message': 'hi'}
    response = requests.post('https://wishkro.fun/S/c.php', data=post_data, cookies={'trp': '10'})
    st.write(f"Response from the server: {response.text}")

