import requests

API_KEY = "lCc4G9mP+5nOqtsX5Jaw6Q==u65jxP1s5yJ0fgFG" # Define as a constant

def fetch_data(animal_name):
    """
    Fetches animal data from the API Ninjas service.

    Parameters:
        Animal_name (str): The name of the animal to query.

    Returns:
        List: A list of dictionariesm each representing an animal with:
            - 'name'
            - 'taxonomy'
            - 'locations'
            - 'characteristics'

        If no animals are found or there's an error, returns and empy list.
    """

    # Construct the API endpoint dynamically using the animal name.
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {"X-Api-Key": API_KEY}  # Add API key to the request header.

    # Make the get request to the API
    response = requests.get(url, headers=headers)

    # Check for successful response
    if response.status_code == 200:
        data = response.json() # Parse JSON response

        if data:
            return data # Return the list of animal dictionaries'
        else:
            print("No animals found in that query.")
            return [] # Return empty list if response is empty
    else:
        # Print the error response if status code isn't 200
        print(f" API Error {response.status_code}: {response.text}")
        return []