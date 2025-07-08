import requests

animal_name = "cheetah"  # You can change this to any animal
url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
headers = {"X-Api-Key": "lCc4G9mP+5nOqtsX5Jaw6Q==u65jxP1s5yJ0fgFG "}  # Replace with your actual key

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    for animal in data:
        print(f"\n🐾 {animal['name']}")
        print(f"📚 Scientific Name: {animal['taxonomy']['scientific_name']}")
        print(f"🌍 Locations: {', '.join(animal['locations'])}")
        print(f"🧬 Diet: {animal['characteristics']['diet']}")
        print(f"⚠️ Threats: {animal['characteristics']['biggest_threat']}")
else:
    print("❌ Error:", response.status_code, response.text)


"""
NOTES:
Notes
Remember that when we get a JSON response, you can use response.json() instead of response.text.

What happens when you search for an animal that doesn’t exist in the database?
 - Let’s say you search for "dragon" or "fluffernoodle":

HTTP Status Code: 200 OK → The API still returns a success code, even if no results are found

JSON Response:

json
[]
→ An empty list, meaning no matches in the database


Did the error code change?

- No Error Code Change: → The status code stays 200 because the request was valid—just no data matched

What response did you get?

- This is a classic case of soft failure:

The API didn’t crash or reject your request

It simply returned an empty result set

So your code needs to check both:

response.status_code == 200

response.json() is not empty

Why “X-Api-Key”?
The "X-" prefix comes from a naming convention for custom or non-standard headers. So:

Api-Key is the name of the header

X-Api-Key signals it's not part of the official HTTP spec but still widely supported and expected by many APIs (like API Ninjas)

"""