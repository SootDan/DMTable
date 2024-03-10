import requests


def api_index(type: str, name: str=None, index: str=None):
    """Function through which all API requests go."""

    # Checks if API is online first.
    url = "https://www.dnd5eapi.co/api/"
    headers = {"Accept": "application/json"}
    response = requests.get(url + type, headers=headers)

    if response.status_code != 200:
        return "API offline. Check internet connection."

    # Now sends requests and gives output
    response_data = response.json()
    response_dict = response_data["results"]

    if name:
        # Gets index for name.
        return [n["index"] for n in response_dict if n["name"] == name]
    elif name == None:
        # Only gets one result.
        return [n["index"] for n in response_dict]
    elif index:
        # Only lists specific named data.
        ...


def bestiary(name: str=None, index: str=None):
    """Creates the bestiary."""
    return api_index(type="monsters", name=name)