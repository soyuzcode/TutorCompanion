"""File to manage user settings"""
import json

BASE_URL = "https://tutorcompanionv1.onrender.com/get/users/"


def get_base_Url():
    """Devuelve la URL Base"""

    # with open tal tal tal as file
    file = ""

    setting = json.load(file)

    return setting["BASE_URL"]
## recomendar funciones para settings (json)