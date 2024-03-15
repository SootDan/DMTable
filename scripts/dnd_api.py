import requests

url = "https://www.dnd5eapi.co/api/"
headers = {"Accept": "application/json"}
is_online = requests.get(url, headers=headers).status_code == 200


def api_index(type: str, name: str = None, index: str = None):
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


def monsters(name: str = None, index: str = None):
    """Creates the bestiary."""
    index = api_index(type="monsters", name=name)
    return index


def fetch_bestiary():
    """Creates the bestiary."""
    indices = api_index(type="monsters")
    monster_count = len(indices)
    monster_list = []

    for i in range(monster_count):
        response = requests.get(
            url + "monsters/" + indices[i], headers=headers).json()

        monster_dict = {"name": "", "index": "",
                        "strength": 0, "dexterity": 0, "constitution": 0, "intelligence": 0, "wisdom": 0, "charisma": 0,
                        "armor_class": 0, "hit_points": 0, "size": "", "speed": 0, "xp": 0, "languages": "",
                        "image": "", "id": 0}

        for key in monster_dict:
            try:
                if key == "image":
                    # Checks if dict is at key. Some monsters don't have images.
                    monster_dict[key] = "https://www.dnd5eapi.co" + \
                        response[key]
                elif key == "armor_class":
                    # Gets AC. It's in a list and SQL doesn't like that.
                    monster_dict[key] = response[key][0]["value"]
                elif key == "speed":
                    monster_dict[key] = response[key]["walk"]
                elif key == "id":
                    # Sets ID. Necessary for database.
                    monster_dict[key] = i + 1
                else:
                    monster_dict[key] = response[key]

            except KeyError:
                if key == "image":
                    monster_dict[key] = "/static/assets/img/icon.png"
                else:
                    monster_dict[key] = "404: Monster data not found."
        monster_list.append(monster_dict)
    return monster_list