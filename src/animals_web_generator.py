import json #Import the JSON module
import os

def load_data(file_path):
    """loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def print_animal_info(animal):
    """Prints selected fields from the animal record, if they exist"""

    if 'name' in animal:
        print(f"Name:{animal['name']}") # Print the animals name if available.

    if 'locations' in animal and isinstance(animal['locations'], list) and animal['locations']:
        print(f"Location: {animal['locations'][0]}") # Prints the animals location if available.


    if 'characteristics' in animal:
        characteristics = animal['characteristics']

        if 'diet' in characteristics:
            print(f"Diet: {characteristics['diet']}")  # Prints the animals diet if available.

        if 'type' in characteristics:
            print(f"Type: {characteristics['type']}") # Print the animals type if available.

    print()

def load_template(template_path):
    """Loads the HTML template and returns it as a string"""
    with open(template_path, "r", encoding='utf-8') as file:
        return file.read()

def generate_animal_info(data):
    output = ""
    for animal in data:
        name = animal.get("name", "Unknown") # Gets animal data, uses "unknown" as default fallback incase of missing data.
        location = animal.get("locations", ["Unknown"])[0] # Indexes first location
        characteristics = animal.get("characteristics", {}) # Retrieves the characteristics dictionary or empty one if non-existent
        diet = characteristics.get("diet","Unknown")
        animal_type = characteristics.get("type","Unknown")

        output += f"Name: {name}\n"
        output += f"Location: {location}\n"
        output += f"Diet: {diet}\n"
        output += f"animal_type: {animal_type}\n"

    return output



def main():
    # Load list of animals from the JSON file
    animals_data = load_data("../data/animals_data.json")

    # Load the HTML template
    template_content = load_template("../data/animals_template.html")

    #Generate the animal info string
    animal_info = generate_animal_info(animals_data)

    # Replace placeholder with generated info
    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animal_info)

    os.makedirs("../output", exist_ok=True)

    # Write final HTL to a new file
    with open("../output/animals.html", "w", encoding="utf-8") as file:
        file.write(final_html)

    for animal in animals_data:
        print_animal_info(animal)


if __name__ == "__main__":
    main()