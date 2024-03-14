import requests

url = "https://www.dnd5eapi.co/api/"
headers = {"Accept": "application/json"}
is_online = requests.get(url, headers=headers).status_code == 200

def api_index(type: str, name: str=None, index: str=None):
    """Function through which all API requests go."""

    # Checks if API is online first.
    if not is_online:
        return False
    response = requests.get(url + type, headers=headers).json()

    # Now sends requests and gives output
    response_dict = response["results"]

    if name:
        # Gets index for name.
        return [n["index"] for n in response_dict if n["name"] == name]
    elif name == None:
        # Only gets one result.
        return [n["index"] for n in response_dict]
    elif index:
        # Only lists specific named data.
        ...


def monsters(name: str=None, index: str=None):
    """Creates the bestiary."""
    index = api_index(type="monsters", name=name)
    return index


def fetch_beast(index: str):
    """Fetches monster data."""

    if not is_online:
        return False
    response = requests.get(url + "monsters/" + index, headers=headers).json()
    stats = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
    stats_list = []
    for key in stats:
        stats_list.append(response[key])

    return stats_list