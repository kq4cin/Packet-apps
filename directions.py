#!/usr/bin/env python3

import urllib.parse
import urllib.request
import re
import socket
import time

def get_address_input(prompt, conn):
    conn.sendall(prompt.encode())
    data = conn.recv(1024).decode().strip()
    return data.replace(' ', '+')

def create_url(origin, destination):
    base_url = "https://gdir.telae.net/gdir/"
    params = {
        'country': 'us',
        'origin': origin,
        'destination': destination,
        'mode_of_travel': 'driving'
    }
    return base_url + '?' + urllib.parse.urlencode(params)

def fetch_directions(url):
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
        clean_text = re.sub('<[^<]+?>', '', html)
        return clean_text

def handle_client(conn):
    try:
        conn.settimeout(40)  # Set a timeout for the connection
        while True:
            origin = get_address_input("Enter origin address: ", conn)
            destination = get_address_input("Enter destination address: ", conn)
            url = create_url(origin, destination)
            directions = fetch_directions(url)
            conn.sendall(directions.encode())
            
            conn.sendall("Do you want to fetch directions for another route? (yes/no): ".encode())
            response = conn.recv(1024).decode().strip().lower()
            if not response:  # Handle client disconnection
                print("Client disconnected")
                break
            if response != 'yes':
                conn.sendall("Goodbye!\n".encode())
                break
    except socket.timeout:
        print("Connection timed out")
    except BrokenPipeError:
        print("Broken pipe error, restarting server...")
        start_server()
    except Exception as e:
        conn.sendall(f"An error occurred: {str(e)}\n".encode())
    finally:
        conn.close()

def start_server(host='0.0.0.0', port=9005):
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
                server_socket.bind((host, port))
                server_socket.listen(1)
                print(f"Server listening on {host}:{port}")
                while True:
                    conn, addr = server_socket.accept()
                    print(f"Connection from {addr}")
                    handle_client(conn)
        except BrokenPipeError:
            print("Broken pipe error, restarting server...")
            time.sleep(1)  # Wait a moment before restarting
            continue

if __name__ == "__main__":
    start_server()
