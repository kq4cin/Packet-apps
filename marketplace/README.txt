# KQ4CIN Marketplace TCP Server

This is a TCP server script that functions as a classifieds program. It allows clients to create, edit, and delete listings with fields for buy/sell, call sign, contact info, and description. The server handles client connections, displays existing listings, and provides a menu for clients to interact with the listings.

## Features

- **TCP Server**: Listens for incoming client connections.
- **Classified Listings**: Allows clients to create, edit, and delete listings.
- **Graceful Timeout Handling**: Closes client connections gracefully on timeout.
- **Graceful Broken Pipe Handling**: Closes client connections gracefully on broken pipe errors.
- **Unique Listing IDs**: Assigns a unique 3-digit ID to each listing.
- **Listings Display**: Displays existing listings with separators and a title.
- **Menu Options**: Provides a menu for clients to choose actions (buy, sell, edit, delete).

## Installation

To install and run the TCP server script, follow these steps:

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/kq4cin/Packet-apps.git
    ```

2. **Navigate to the Directory**:
    ```sh
    cd Packet-apps
    cd marketplace
    ```

3. **Run the Server**:
    ```sh
    python3 MKT.py
    ```

## Usage

1. **Start the Server**:
    - Run the server script using the command mentioned above. The server will start listening on port 9004.

2. **Connect to the Server**:
    - Use any TCP client to connect to the server. For example, you can use `telnet`:
        ```sh
        telnet localhost 9004
        ```

3. **Interact with the Server**:
    - Upon connection, the server will display the title "KQ4CIN MARKETPLACE" and the current listings.
    - The server will then display a menu with options to buy, sell, edit, or delete a listing.
    - Follow the prompts to enter the required information for each action.

## Example

Here is an example of how to interact with the server:

1. **Connect to the Server**:
    ```sh
    telnet localhost 9004
    ```

2. **Server Display**:
    ```
    KQ4CIN MARKETPLACE
    ===================
    Current Listings:
    123 | buy | N1CALL | 555-1234 | Looking to buy a baofeng
    ********
    456 | sell | NOCALL | 555-5678 | Selling a baofeng
    ********

    Menu:
    1. Buy
    2. Sell
    3. Edit
    4. Delete
    Enter your choice:
    ```

3. **Create a Listing**:
    - Choose option 2 (Sell) and follow the prompts to enter the call sign, contact info, and description.

4. **Edit a Listing**:
    - Choose option 3 (Edit) and follow the prompts to enter the call sign, listing ID, and new details.

5. **Delete a Listing**:
    - Choose option 4 (Delete) and follow the prompts to enter the call sign and listing ID.

## Notes

- Ensure that the `listings.txt` file is in the same directory as the script to store and retrieve listings.
- The server will handle client connections gracefully and continue running even if a client connection times out or encounters a broken pipe error.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
