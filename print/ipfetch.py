import socket
import requests

server_address = 'http://127.0.0.1:3000'

# server_address = 'https://pd.tmflimited.co.ke'


def get_local_ip():
    try:
        # Connect to a public server to get the local IP address
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))  # Google DNS server
            local_ip = s.getsockname()[0]
        return local_ip
    except Exception as e:
        return f"Error retrieving local IP: {e}"



def update_ip():
# updating the ip
    server_url = f'{server_address}/printserver/add'
    print(server_url)

    local_ip = get_local_ip()
    print('local ip', local_ip)

    res = requests.post(server_url, json={"ip": local_ip})
    # print(res.text)
    print(res.status_code)