import requests

API_KEY = "lCc4G9mP+5nOqtsX5Jaw6Q==u65jxP1s5yJ0fgFG" # Define as a constant

def fetch_data(animal_name):
    """
    Fetches animal data from the API Ninjas service.

    Parameters:
        Animal_name (str): The name of the animal to query.

    Returns:
        List: A list of dictionaries each representing an animal with:
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

if __name__ == "__main__":
    animal = input("🔍 Enter an animal name to test the fetcher: ").strip()

    data = fetch_data(animal)
    print(data)



"""
    Your data_fetcher.py script is responsible for talking to the external API, grabbing detailed animal data based on a name you give it, and returning that data to the rest of your program—all in a clean, modular way.

🔍 In plain terms, here’s what it does:
Takes in an animal name like "lion", "armadillo", or "goadohjasgfas"

Calls the API Ninjas service using that name and your API key

Receives the data back from the server:

For valid animals, it returns a list of dictionaries containing:

Name

Taxonomy (like genus, order, etc.)

Locations

Characteristics

For nonexistent animals or errors:

It returns an empty list

And prints a little diagnostic message to your console

This function doesn’t care what you do with the data afterward—it’s designed to just fetch. That keeps your logic split into two roles:

data_fetcher.py = the librarian

animals_web_generator.py = the artist

🦊 Why It’s Awesome
Keeps your code modular, so you can later plug in fake data, a local JSON file, or a different API—without touching your web generator logic

Makes it super easy to test and isolate bugs, because the fetcher isn’t tangled up in HTML

Follows the coding principle of separation of concerns—something even senior engineers rely on
    """


