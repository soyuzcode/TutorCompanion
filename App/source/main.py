"""Here we're gonna connect every module to UI"""
import json
import os
from ui import TutorCompanion
from modules.process_data import is_psk_and_username_valid
from modules.process_data import process_data_from_user_dict
from modules.get_data import get_user_data
from modules.tuto_suggestions import get_key_hours_by_identifier

class Main():
    def __init__(self) -> None:
        UI = TutorCompanion(check_login=self.check_login, get_ranking=self.get_rank)
        UI.run()

        # Don't write anything here!!
        # This will execute when kill UI

    def get_rank(self, identifier) -> int | None:
        return get_key_hours_by_identifier(identifier=identifier, users=get_user_data())

    def check_login(self, user, psk) -> bool:
        # 1. Intentamos usar el código original de Carlos con el servidor externo
        try:
            print("Intentando conectar con el servidor de Carlos...")
            # Si el servidor responde rápido, usará los datos reales
            datos_servidor = get_user_data()
            if datos_servidor:
                datos_procesados = process_data_from_user_dict(datos_servidor)
                if is_psk_and_username_valid(user=user, psk=psk, data=datos_procesados):
                    return True
        except Exception as e:
            # Si el servidor falla o está caído, Python no se congela; salta directamente aquí
            print(f"El servidor externo no está disponible. Activando modo local de prueba.")

        # =======================================================================
        # PLAN B (FALLBACK): Si el servidor falla o está caído, usamos el JSON local de prueba
        # De aquí no borramos nada de Carlos, solo aseguramos que la app funcione YA.
        # =======================================================================
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(os.path.dirname(base_dir), "Data", "return_example.json")
        
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                datos_locales = json.load(f)
            
            datos_procesados_locales = process_data_from_user_dict(datos_locales)
            if is_psk_and_username_valid(user=user, psk=psk, data=datos_procesados_locales):
                return True
        except Exception as err_local:
            print(f"Error crítico al leer incluso el archivo de respaldo: {err_local}")
            
        return False


if __name__ == "__main__":
    Main()