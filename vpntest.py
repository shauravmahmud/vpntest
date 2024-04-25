import streamlit as st
import requests
import subprocess
import threading
import tornado.ioloop
import tornado.web

# Tornado handlers
class ConnectVPNHandler(tornado.web.RequestHandler):
    def post(self):
        # Logic to start OpenVPN connection
        subprocess.run(["sudo", "openvpn", "--config", "your_vpn_config.ovpn"])
        self.write("VPN connected")

class DisconnectVPNHandler(tornado.web.RequestHandler):
    def post(self):
        # Logic to stop OpenVPN connection
        subprocess.run(["sudo", "pkill", "openvpn"])
        self.write("VPN disconnected")

def make_app():
    return tornado.web.Application([
        (r"/connect-vpn", ConnectVPNHandler),
        (r"/disconnect-vpn", DisconnectVPNHandler),
    ])

# Start Tornado server in a separate thread
def run_tornado():
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

tornado_thread = threading.Thread(target=run_tornado)
tornado_thread.start()

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
            response = requests.post("http://localhost:8888/connect-vpn")
            st.write(response.text)

    elif choice == "Disconnect from VPN":
        st.subheader("Disconnect from VPN")
        if st.button("Disconnect"):
            # Call API to disconnect from VPN
            response = requests.post("http://localhost:8888/disconnect-vpn")
            st.write(response.text)

if __name__ == '__main__':
    main()
