import requests
import streamlit as st

# Set the domain and cookie values
domain = "https://wishkro.fun/S"
cookie_name = "hie"
cookie_value = "1"
cookie_expiration = 5 * 60  # 5 minutes in seconds

# Create the Set-Cookie header value
set_cookie_header = f"{cookie_name}={cookie_value}; Max-Age={cookie_expiration}; Domain={domain}"

# Set the response header to include the Set-Cookie header
st.set_page_config(page_title="My Webpage", layout="wide", initial_sidebar_state="collapsed", key=set_cookie_header)

# Add a button to send 'hi' with Cookie
if st.button("Send 'hi' with Cookie"):
    post_data = {'message': 'hi'}
    response = requests.post('https://wishkro.fun/S/c.php', data=post_data, cookies={'trp': '10'})
    st.write(f"Response from the server: {response.text}")
