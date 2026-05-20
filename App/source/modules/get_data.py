"""In this file we're gonna get data from an API hosted by Vercel"""

import requests 
import json
import os
from modules.config import get_base_Url

def get_user_data() -> dict | None:
    """Fetches JSON from the API and returns it as a Python dictionary.
       If the API is down, it loads the local backup file instantly."""

    # 1. Intentamos conectar al servidor de Vercel con un "timeout" de 10 segundos 
    # para que si está caído, no congele la app por minutos.
    try:
        response = requests.get(f"{get_base_Url()}/user", timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Server Error: Received status code {response.status_code}")
    except Exception as e:
        print(f"API connection failed ({e}). Switching to local backup data.")

    # =======================================================================
    # PLAN B (FALLBACK): Si la API falla, cargamos el JSON local automáticamente
    # =======================================================================
    try:
        # Encontramos la ruta correcta del archivo 'return_example.json'
        # Subimos un nivel desde la carpeta modules para buscar la carpeta Data
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        json_path = os.path.join(base_dir, "Data", "return_example.json")
        
        if os.path.exists(json_path):
            with open(json_path, "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            print(f"Critical Error: Backup file not found at {json_path}")
            return None
            
    except Exception as err_local:
        print(f"Error reading backup JSON: {err_local}")
        return None
    
def get_sugerencias_reales() -> list:
    """
    Obtiene las sugerencias/solicitudes desde el endpoint oficial de Carlos.
    """
    try:
        # Usamos la misma lógica de URL base que ya tienes configurada
        url = f"{get_base_Url()}/suggestions" 
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error al obtener sugerencias: {response.status_code}")
            return []
            
    except Exception as e:
        print(f"No se pudieron cargar las sugerencias: {e}")
        return []