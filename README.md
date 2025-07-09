# zootopia-api

# Zootopia API Animal Explorer

This Python-based project connects to the [API Ninjas Animal API](https://api-ninjas.com/api/animals) and retrieves real animal data based on user input. It dynamically generates an HTML page displaying animal profiles, including diet, type, and location.

Built as part of Masterschool’s frontend exercises, the code showcases modular architecture, clean API handling, and HTML generation via templates.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YourUsername/zootopia-api.git
   cd zootopia-api

2. Add your API key to a .env file in the root:

   ```.env
    API_KEY='your-api-key-here'
   
3. Install dependencies:

   ```bash
   pip install -requirements.txt
   
---

## Usage

To generate animal data into an HTML file:

   ```bash
python src/main.py
   ```
You will be prompted to enter an animal name (e.g., Lion). The result will be written to output/animals.html

---

## Contributing

Contributions are welcome. To propose changes or enhancements:

 - Fork the repository
 - Create a new branch
 - Submit a pull request with clear descriptions

For larger changes, open an issue first to discuss direction. 

---

## License 

This project is provided for educational purposes and is not licensed for commercial use. 