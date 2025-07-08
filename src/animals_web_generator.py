import json  # Import the JSON module
import os
import requests

from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def load_data(file_path):
    """loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def fetch_animals_from_api(query,api_key):
    """Fetch animal data from API Ninjas"""
    url = f"https://api.api-ninjas.com/v1/animals?name={query}"
    headers = {"X-Api-Key": api_key}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data:
            return data
        else:
            print(" No animals found for that query.")
            return []
    else:
        print(f" API error {response.status_code}: {response.text}")
        return []


def print_animal_info(animal):
    """Prints selected fields from the animal record, if they exist"""

    if "name" in animal:
        print(f"Name:{animal['name']}")  # Print the animal's name if available.

    if (
        "locations" in animal
        and isinstance(animal["locations"], list)
        and animal["locations"]
    ):
        print(
            f"Location: {animal['locations'][0]}"
        )  # Prints the animal's location if available.

    if "characteristics" in animal:
        characteristics = animal["characteristics"]

        if "diet" in characteristics:
            print(
                f"Diet: {characteristics['diet']}"
            )  # Prints the animal's diet if available.

        if "type" in characteristics:
            print(
                f"Type: {characteristics['type']}"
            )  # Print the animal's type if available.

    print()


def load_template(template_path):
    """Loads the HTML template and returns it as a string"""
    with open(template_path, "r", encoding="utf-8") as file:
        return file.read()


def serialize_animal(animal_obj):
    """Generates the HTML string for a single animal card"""
    name = animal_obj.get("name", "Unknown")
    location = animal_obj.get("locations", ["Unknown"])[0]
    characteristics = animal_obj.get("characteristics", {})
    diet = characteristics.get("diet", "Unknown")
    animal_type = characteristics.get("type", "Unknown")

    output = ""
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'  # Wraps name in div
    output += '  <p class="card__text">\n'  # Paragraph blocks for better formatting
    output += (
        f"    <strong>Diet:</strong> {diet}<br/>\n"  # Bolder type face for clarity
    )
    output += f"    <strong>Location:</strong> {location}<br/>\n"
    output += f"    <strong>Type:</strong> {animal_type}<br/>\n"
    output += "  </p>\n"
    output += "</li>\n\n"
    return output


def generate_animal_info(data):
    return "".join(serialize_animal(animal) for animal in data)


def main():
    # Load list of animals from the JSON file
    api_key = "lCc4G9mP+5nOqtsX5Jaw6Q==u65jxP1s5yJ0fgFG "
    query = input("Enter a name of an animal: ").strip()
    animals_data = fetch_animals_from_api(query, api_key)

    if not animals_data:
        animal_info =f'<h2> The animal "{query}" doesn\'t exist. </h2>'
    else:
        animal_info = generate_animal_info(animals_data)

    # Load the HTML template
    template_content = load_template("../data/animals_template.html")
    # Replace the placeholder template
    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animal_info)

    # Make sure the output folder exists
    os.makedirs("../output", exist_ok=True)

    # Write final HTL to a new file
    with open("../output/animals.html", "w", encoding="utf-8") as file:
        file.write(final_html)

    print("\n✅ Website was successfully generated to the file animals.html.\n")
    for animal in animals_data:
        print_animal_info(animal)


if __name__ == "__main__":
    main()
