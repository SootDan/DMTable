import requests

url = "https://www.dnd5eapi.co/api/"
headers = {"Accept": "application/json"}

def is_online():
    # Checks if API is online.
    response = requests.get(url, headers=headers)
    return response.status_code == 200

def spell_data(spell_name = None):
    if is_online():
        spell_url = f"{url}spells"
        response = requests.get(spell_url, headers=headers)
        spells_data = response.json()
        spells = spells_data["results"]
        return spells["name"]
    
    else:
        return "API is currently offline. Check your connection."

spell_data("Wish")

def database():
    # Creates a database.
    # TODO: Character Data
    ...