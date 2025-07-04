import json #Import the JSON module

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

def main():
    # Load list of animals from the JSON file
    animals_data = load_data("../data/animals_data.json")


    for animal in animals_data:
        print_animal_info(animal)


if __name__ == "__main__":
    main()