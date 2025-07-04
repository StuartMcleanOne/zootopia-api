import json #Import the JSON module
import os

def load_data(file_path):
    """loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def print_animal_info(animal):
    """Prints selected fields from the animal record, if they exist"""

    if 'name' in animal:
        print(f"Name:{animal['name']}") # Print the animal's name if available.

    if 'locations' in animal and isinstance(animal['locations'], list) and animal['locations']:
        print(f"Location: {animal['locations'][0]}") # Prints the animal's location if available.


    if 'characteristics' in animal:
        characteristics = animal['characteristics']

        if 'diet' in characteristics:
            print(f"Diet: {characteristics['diet']}")  # Prints the animal's diet if available.

        if 'type' in characteristics:
            print(f"Type: {characteristics['type']}") # Print the animal's type if available.

    print()

def load_template(template_path):
    """Loads the HTML template and returns it as a string"""
    with open(template_path, "r", encoding='utf-8') as file:
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
    output += f'    <strong>Diet:</strong> {diet}<br/>\n'  # Bolder type face for clarity
    output += f'    <strong>Location:</strong> {location}<br/>\n'
    output += f'    <strong>Type:</strong> {animal_type}<br/>\n'
    output += '  </p>\n'
    output += '</li>\n\n'
    return output

def generate_animal_info(data):
    return ''.join(serialize_animal(animal) for animal in data)


def main():
    # Load list of animals from the JSON file
    animals_data = load_data("../data/animals_data.json")

    # Load the HTML template
    template_content = load_template("../data/animals_template.html")

    #Generate the animal info string
    animal_info = generate_animal_info(animals_data)

    # Replace the placeholder template
    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animal_info)

    # Make sure the output folder exists
    os.makedirs("../output", exist_ok=True)

    # Write final HTL to a new file
    with open("../output/animals.html", "w", encoding="utf-8") as file:
        file.write(final_html)

    for animal in animals_data:
        print_animal_info(animal)


if __name__ == "__main__":
    main()