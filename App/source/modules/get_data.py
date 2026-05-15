"""In this file we're gonna get data from an API hosted by Vercel"""

import requests 
from modules.config import get_base_Url

def get_user_data():
    """Fetches JSON from the API and returns it as a Python dictionary"""

    try:
        response = requests.get(f"{get_base_Url()}/user")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
        
    except Exception as e:
        print(f"Error: {e}")
        return None
