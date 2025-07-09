import json
import os
from dotenv import load_dotenv
import data_fetcher  # Modularized fetcher script

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")  # Access for legacy compatibility

def load_data(file_path):
    """Loads animal data from a static JSON file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def print_animal_info(animal):
    """Prints selected fields from the animal record, if they exist."""
    if "name" in animal:
        print(f"Name: {animal['name']}")

    if (
        "locations" in animal
        and isinstance(animal["locations"], list)
        and animal["locations"]
    ):
        print(f"Location: {animal['locations'][0]}")

    if "characteristics" in animal:
        characteristics = animal["characteristics"]

        if "diet" in characteristics:
            print(f"Diet: {characteristics['diet']}")

        if "type" in characteristics:
            print(f"Type: {characteristics['type']}")

    print()

def load_template(template_path):
    """Loads the HTML template and returns it as a string."""
    with open(template_path, "r", encoding="utf-8") as file:
        return file.read()

def serialize_animal(animal_obj):
    """Generates the HTML string for a single animal card."""
    name = animal_obj.get("name", "Unknown")
    location = animal_obj.get("locations", ["Unknown"])[0]
    characteristics = animal_obj.get("characteristics", {})
    diet = characteristics.get("diet", "Unknown")
    animal_type = characteristics.get("type", "Unknown")

    output = ""
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'
    output += '  <p class="card__text">\n'
    output += f"    <strong>Diet:</strong> {diet}<br/>\n"
    output += f"    <strong>Location:</strong> {location}<br/>\n"
    output += f"    <strong>Type:</strong> {animal_type}<br/>\n"
    output += "  </p>\n"
    output += "</li>\n\n"
    return output

def generate_animal_info(data):
    """Generates all animal card HTML blocks from data."""
    return "".join(serialize_animal(animal) for animal in data)

def main():
    # Request animal name from user
    query = input("Enter a name of an animal: ").strip()

    # Fetch data using the modular fetcher
    animals_data = data_fetcher.fetch_data(query)

    if not animals_data:
        animal_info = f'<h2>The animal "{query}" doesn\'t exist.</h2>'
    else:
        animal_info = generate_animal_info(animals_data)

    # Load HTML template
    template_content = load_template("../data/animals_template.html")

    # Replace placeholder with generated HTML
    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animal_info)

    # Ensure output folder exists
    os.makedirs("../output", exist_ok=True)

    # Write the final HTML to a new file
    with open("../output/animals.html", "w", encoding="utf-8") as file:
        file.write(final_html)

    print("\nWebsite was successfully generated to the file animals.html.\n")
    for animal in animals_data:
        print_animal_info(animal)

if __name__ == "__main__":
    main()
