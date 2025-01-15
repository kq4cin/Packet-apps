import socket
import threading
import random

#This classifieds app was created by Joey Scarlett KQ4CIN
# Template for a classified listing
class Listing:
    def __init__(self, action, call_sign, contact_info, description, listing_id=None):
        self.action = action
        self.call_sign = call_sign
        self.contact_info = contact_info
        self.description = description
        self.listing_id = listing_id if listing_id is not None else random.randint(100, 999)

    def __str__(self):
        return f"{self.listing_id} | {self.action} | {self.call_sign} | {self.contact_info} | {self.description}"

# Function to handle client connections
def handle_client(client_socket):
    try:
        client_socket.settimeout(240)  # Set a timeout of 240 seconds
        # Display title
        client_socket.send("KQ4CIN MARKETPLACE\n".encode('utf-8'))
        client_socket.send("===================\n".encode('utf-8'))

        # Display existing listings
        client_socket.send("Current Listings:\n".encode('utf-8'))
        try:
            with open("listings.txt", "r") as file:
                listings = file.readlines()
                if listings:
                    for listing in listings:
                        client_socket.send(listing.encode('utf-8'))
                        client_socket.send("********\n".encode('utf-8'))  # Separator
                else:
                    client_socket.send("No listings available.\n".encode('utf-8'))
        except FileNotFoundError:
            client_socket.send("No listings available.\n".encode('utf-8'))

        # Display menu
        menu = "\nMenu:\n1. Buy\n2. Sell\n3. Edit\n4. Delete\nEnter your choice: "
        client_socket.send(menu.encode('utf-8'))
        choice = client_socket.recv(1024).decode('utf-8').strip()

        if choice == '1':
            action = 'buy'
        elif choice == '2':
            action = 'sell'
        elif choice == '3':
            client_socket.send("Enter your call sign to edit your listing: ".encode('utf-8'))
            call_sign = client_socket.recv(1024).decode('utf-8').strip()
            client_socket.send("Enter your listing ID to edit: ".encode('utf-8'))
            listing_id = client_socket.recv(1024).decode('utf-8').strip()
            edit_listing(client_socket, call_sign, listing_id)
            return
        elif choice == '4':
            client_socket.send("Enter your call sign to delete your listing: ".encode('utf-8'))
            call_sign = client_socket.recv(1024).decode('utf-8').strip()
            client_socket.send("Enter your listing ID to delete: ".encode('utf-8'))
            listing_id = client_socket.recv(1024).decode('utf-8').strip()
            delete_listing(client_socket, call_sign, listing_id)
            return
        else:
            client_socket.send("Invalid choice. Connection closing.\n".encode('utf-8'))
            return

        # Prompt for call sign
        client_socket.send("Enter call sign: ".encode('utf-8'))
        call_sign = client_socket.recv(1024).decode('utf-8').strip()

        # Prompt for contact info
        client_socket.send("Enter contact info: ".encode('utf-8'))
        contact_info = client_socket.recv(1024).decode('utf-8').strip()

        # Prompt for description
        client_socket.send("Enter description: ".encode('utf-8'))
        description = client_socket.recv(1024).decode('utf-8').strip()

        # Create and display the listing
        listing = Listing(action, call_sign, contact_info, description)
        print(f"Received listing: {listing}")
        client_socket.send(f"Listing received: {listing}\n".encode('utf-8'))

        # Save the listing to a file
        with open("listings.txt", "a") as file:
            file.write(str(listing) + "\n")
    except socket.timeout:
        print("Client connection timed out. Closing connection...")
    except BrokenPipeError:
        print("Broken pipe error. Closing connection...")
    finally:
        client_socket.close()

def edit_listing(client_socket, call_sign, listing_id):
    try:
        with open("listings.txt", "r") as file:
            listings = file.readlines()

        updated_listings = []
        found = False
        for listing in listings:
            if call_sign in listing and listing_id in listing:
                found = True
                client_socket.send("Enter new action (buy/sell): ".encode('utf-8'))
                action = client_socket.recv(1024).decode('utf-8').strip()
                client_socket.send("Enter new contact info: ".encode('utf-8'))
                contact_info = client_socket.recv(1024).decode('utf-8').strip()
                client_socket.send("Enter new description: ".encode('utf-8'))
                description = client_socket.recv(1024).decode('utf-8').strip()
                updated_listing = Listing(action, call_sign, contact_info, description, listing_id)
                updated_listings.append(str(updated_listing) + "\n")
                client_socket.send(f"Listing updated: {updated_listing}\n".encode('utf-8'))
            else:
                updated_listings.append(listing)

        if not found:
            client_socket.send("No listing found with your call sign and listing ID.\n".encode('utf-8'))
        else:
            with open("listings.txt", "w") as file:
                file.writelines(updated_listings)
    finally:
        client_socket.close()

def delete_listing(client_socket, call_sign, listing_id):
    try:
        with open("listings.txt", "r") as file:
            listings = file.readlines()

        updated_listings = []
        found = False
        for listing in listings:
            if call_sign in listing and listing_id in listing:
                found = True
                client_socket.send(f"Listing deleted: {listing}".encode('utf-8'))
            else:
                updated_listings.append(listing)

        if not found:
            client_socket.send("No listing found with your call sign and listing ID.\n".encode('utf-8'))
        else:
            with open("listings.txt", "w") as file:
                file.writelines(updated_listings)
    finally:
        client_socket.close()

# Main function to start the TCP server
def start_server(host='0.0.0.0', port=9004):  # Changed port to 9004
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
