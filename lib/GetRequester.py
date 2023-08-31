# Importing the required modules
import requests  # Required for making HTTP requests
import json  # Required for parsing JSON data

# Define the GetRequester class
class GetRequester:

    # Initialization method (__init__) to set the instance variable 'url'
    def __init__(self, url):
        self.url = url  # Store the provided URL as an instance variable

    # Method to send an HTTP GET request and return the response body
    def get_response_body(self):
        # Send a GET request using 'requests.get' and store the response object in 'response'
        response = requests.get(self.url)
        # Return the content (body) of the response, which is in bytes
        return response.content

    # Method to load and parse JSON data from the response
    def load_json(self):
        # Call 'get_response_body' to get the response content
        response_content = self.get_response_body()
        # Parse the JSON content into a Python data structure (list or dictionary)
        return json.loads(response_content)

# Create an instance of the GetRequester class with a URL
people = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")

# Call the 'load_json' method on the 'people' object and store the returned data structure in 'loaded_data'
loaded_data = people.load_json()

# Check if 'loaded_data' is a non-empty list and if its first element contains the key "name"
if isinstance(loaded_data, list) and loaded_data and "name" in loaded_data[0]:
    # Iterate over each dictionary in the list
    for person in loaded_data:
        # Print the value associated with the key "name" in each dictionary
        print(person["name"])

