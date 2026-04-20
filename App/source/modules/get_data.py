"""In this file we're gonna get data from an API hosted by Vercel"""

import requests 
from modules.config import BASE_URL

def get_json_data():
    """Fetches JSON from the API and returns it as a Python dictionary"""

    try:
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
        
    except Exception as e:
        print(f"Error: {e}")
        return None
    
if __name__ == "__main__":
    print('Pronando conexion con API')
    data = get_json_data()

    if data:
        print("Data received from API:")
        print(data) 
    else:
        print("Failed to retrieve data from API")
    
