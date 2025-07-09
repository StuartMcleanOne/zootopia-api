import os
import requests  # Needed to make API calls
from dotenv import load_dotenv  # Used to load API key securely from .env

# Load environment variables from the .env file
load_dotenv()

# Extract the API key from the environment
API_KEY = os.getenv("API_KEY")


def fetch_data(animal_name):
    """
    Fetches animal data from the API Ninjas service.

    Parameters:
        animal_name (str): The name of the animal to query.

    Returns:
        list: A list of dictionaries, each representing an animal with:
            - 'name'
            - 'taxonomy'
            - 'locations'
            - 'characteristics'

        If no animals are found or there's an error, returns an empty list.
    """

    # Construct the API endpoint dynamically using the provided animal name
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {"X-Api-Key": API_KEY}  # Attach API key to the request header

    # Make the GET request to the API
    response = requests.get(url, headers=headers)

    # Successful response
    if response.status_code == 200:
        data = response.json()  # Parse the JSON data from the API response

        if data:
            return data  # Return the list of animal dictionaries
        else:
            print(" No animals found in that query.")
            return []  # Return empty list when no results are found

    else:
        # Handle request error gracefully
        print(f" API Error {response.status_code}: {response.text}")
        return []


#  Allow direct testing of the module without importing it elsewhere
if __name__ == "__main__":
    animal = input("🔍 Enter an animal name to test the fetcher: ").strip()
    data = fetch_data(animal)
    print(data)

