# API Examples

# This file provides examples of how to interact with APIs using the `requests` library in Python.

# 1. Installing the `requests` library
# Open your VS Code terminal (View -> Terminal).
# Run the following command to install the `requests` library:
#
# pip install requests

# 2. Making a GET request
import requests

# Replace with the URL of the API you want to access
url = "https://jsonplaceholder.typicode.com/todos/1"

# Make a GET request to the API
response = requests.get(url)

# 3. Handling the response
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the response data in JSON format
    data = response.json()

    # Print the data
    print("Data:", data)

    # Access specific values in the data
    print("Title:", data["title"])
    print("Completed:", data["completed"])
else:
    # Print an error message if the request was not successful
    print("Error:", response.status_code)

# 4. Making a POST request
# Replace with the URL of the API you want to access
url = "https://jsonplaceholder.typicode.com/posts"

# Create a dictionary with the data you want to send
data = {
    "userId": 1,
    "title": "My New Post",
    "body": "This is the body of my new post."
}

# Make a POST request to the API
response = requests.post(url, json=data)

# 5. Handling the POST response
# Check if the request was successful (status code 201)
if response.status_code == 201:
    # Get the response data in JSON format
    data = response.json()

    # Print the data
    print("Data:", data)

    # Access the ID of the new post
    print("ID:", data["id"])
else:
    # Print an error message if the request was not successful
    print("Error:", response.status_code)

# 6. Setting headers
# You can set custom headers in your requests.
headers = {
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

# 7. Authentication
# Some APIs require authentication. You can pass API keys or tokens in the headers.
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)

# Note: This is just a basic example. You may need to adjust the code depending on the specific API you are using.