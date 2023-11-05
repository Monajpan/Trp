import requests
import streamlit as st

# Set page title and layout
st.set_page_config(page_title="My Webpage", layout="wide")

# Function to set a cookie
def set_cookie(name, value, domain, duration):
    st.set_page_config(page_title="My Webpage", layout="wide")

    # Add a button to set the 'hie' cookie
    if st.button("Set 'hie' Cookie for 5 Minutes"):
        expiration_time = int(time.time()) + 300  # 5 minutes
        st.set_cookie(name, value, domain, expiration_time)
        st.write(f"Cookie '{name}' set for {duration} minutes on domain {domain}")

# Add a button to send 'hi' with the 'trp' cookie
if st.button("Send 'hi' with Cookie"):
    post_data = {'message': 'hi'}
    response = requests.post('https://wishkro.fun/S/c.php', data=post_data, cookies={'trp': '10'})
    st.write(f"Response from the server: {response.text}")

# Add a button to set the 'hie' cookie
set_cookie('hie', '1', 'https://wishkro.fun/S', 5)
