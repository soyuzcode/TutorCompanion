"""File to manage user settings"""
import json

def get_base_Url():
    """Devuelve la URL Base"""

    # with open tal tal tal as file
    with open("Data/settings.json", "r+") as file:
        setting = json.load(file)

    return setting["BASE_URL"]
## recomendar funciones para settings (json)