# Packet-apps
This script works with LINBPQ and fetches driving directions from https://gdir.telae.net/.
Here is an example of how your connect statement will look like 
ATTACH 2 
c 10.169.87.83 9005 REALTELNET NOCALL K S,,0

# Directions directions.py

This Python script sets up a simple server that fetches driving directions between two addresses using an online service. The server communicates with clients over a TCP connection, prompting them for origin and destination addresses, and then returns the driving directions.

## Features

- Prompts the user for origin and destination addresses.
- Fetches driving directions from an online service.
- Handles client disconnections and timeouts.
- Restarts the server on broken pipe errors.

## Requirements

- Python 3.6 or higher
- Docker

## Installation

### Running the Script Directly

1. Clone the repository or download the script.
2. Ensure you have Python 3.6 or higher installed.
3. Run the script:

    ```sh
    python3 directions.py
    ```

### Running the Script with Docker

1. Create a [Dockerfile](http://_vscodecontentref_/0) in the same directory as your script with the following content:

    ```Dockerfile
    # Use an official Python runtime as a parent image
    FROM python:3.9-slim

    # Set the working directory in the container
    WORKDIR /usr/src/app

    # Copy the current directory contents into the container at /usr/src/app
    COPY . .

    # Install any needed packages specified in requirements.txt
    # If you have a requirements.txt file, uncomment the following line
    # RUN pip install --no-cache-dir -r requirements.txt

    # Make port 9005 available to the world outside this container
    EXPOSE 9005

    # Run the script
    CMD ["sh", "-c", "while true; do python3 directions.py; sleep 1; done"]
    ```

  

2. Build the Docker image:
   #Be sure your in the directory that contains both the docker file and the script
   # cd into the the directory then issue the docker build command

    ```sh
    docker build -t directions-app .
 
    ```

    This command builds the Docker image and tags it as directions.py

4. Run the Docker container:

    ```sh
   docker run -p 9005:9005 directions-app

    ```

    This command runs the Docker container and maps port 9005 on your host to port 9005 in the container.

### Summary of Commands

```sh
# Step 1: Create Dockerfile (content provided above)

# Step 2: Build the Docker image
docker build -t directions-app .


# Step 3: Run the Docker container
docker run -p 9005:9005 directions-app


```markdown
# Directions directions.py

This Python script sets up a simple server that fetches driving directions between two addresses using an online service. The server communicates with clients over a TCP connection, prompting them for origin and destination addresses, and then returns the driving directions.

## Features

- Prompts the user for origin and destination addresses.
- Fetches driving directions from an online service.
- Handles client disconnections and timeouts.
- Restarts the server on broken pipe errors.

## Requirements

- Python 3.6 or higher
- Docker

## Installation

### Running the Script Directly

1. Clone the repository or download the script.
2. Ensure you have Python 3.6 or higher installed.
3. Run the script:

    ```sh
    python3 directions.py
    ```

### Running the Script with Docker

1. Create a 

Dockerfile

 in the same directory as your script with the following content:

    ```Dockerfile
    # Use an official Python runtime as a parent image
    FROM python:3.9-slim

    # Set the working directory in the container
    WORKDIR /usr/src/app

    # Copy the current directory contents into the container at /usr/src/app
    COPY . .

    # Install any needed packages specified in requirements.txt
    # If you have a requirements.txt file, uncomment the following line
    # RUN pip install --no-cache-dir -r requirements.txt

    # Make port 9005 available to the world outside this container
    EXPOSE 9005

    # Run the script
    CMD ["sh", "-c", "while true; do python3 directions.py; sleep 1; done"]
    ```


2. Build the Docker image:

    ```sh
   docker build -t directions-app .

    ```

    This command builds the Docker image and tags it as 

directions-app

.

3. Run the Docker container:

    ```sh
  docker run -p 9005:9005 directions-app

    ```

    This command runs the Docker container and maps port 9005 on your host to port 9005 in the container.

### Summary of Commands

```sh
# Step 1: Create Dockerfile (content provided above)

# Step 2: Build the Docker image
docker build -t directions-app .


# Step 3: Run the Docker container
docker run -p 9005:9005 directions-app

```

## Usage

1. Connect to the server using a TCP client (e.g., `telnet` or a custom client).
2. Follow the prompts to enter the origin and destination addresses.
3. Receive the driving directions.
4. Choose whether to fetch directions for another route or exit.

## Example

```sh
$ telnet localhost 9005
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
Enter origin address: 123 Main St, Anytown, USA
Enter destination address: 456 Elm St, Othertown, USA
Directions: ...
Do you want to fetch directions for another route? (yes/no): no
Goodbye!
Connection closed by foreign host.
```

## License

This project is licensed under the MIT License.
```

This `README.md` file provides an overview of the script, installation instructions, usage examples, and specific CLI commands for setting up and running the script in Docker. The Python script itself is omitted as requested.
This `README.md` file provides an overview of the script, installation instructions, usage examples, and specific CLI commands for setting up and running the script in Docker. The Python script itself is omitted as requested.
