import streamlit as st
import requests
from flask import Flask, request
import threading

# Flask app
flask_app = Flask(__name__)

@flask_app.route('/connect-vpn', methods=['POST'])
def connect_vpn():
    # Logic to start OpenVPN connection
    return "VPN connected"

@flask_app.route('/disconnect-vpn', methods=['POST'])
def disconnect_vpn():
    # Logic to stop OpenVPN connection
    return "VPN disconnected"

def run_flask():
    flask_app.run(debug=False)

# Start Flask server in a separate thread
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

# Streamlit app
def main():
    st.title("Streamlit VPN Manager")

    # Sidebar menu
    menu = ["Home", "Connect to VPN", "Disconnect from VPN"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.write("Welcome to the Streamlit VPN Manager!")

    elif choice == "Connect to VPN":
        st.subheader("Connect to VPN")
        if st.button("Connect"):
            # Call API to connect to VPN
            response = requests.post("http://localhost:5000/connect-vpn")
            st.write(response.text)

    elif choice == "Disconnect from VPN":
        st.subheader("Disconnect from VPN")
        if st.button("Disconnect"):
            # Call API to disconnect from VPN
            response = requests.post("http://localhost:5000/disconnect-vpn")
            st.write(response.text)

if __name__ == '__main__':
    main()
