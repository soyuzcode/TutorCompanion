"""Here we're gonna connect every module to UI"""
import json
import os
from ui import TutorCompanion
from modules.process_data import is_psk_and_username_valid
from modules.process_data import process_data_from_user_dict
# Importamos tu nueva función asignada
from modules.process_data import obtener_todas_las_tutorias 
from modules.get_data import get_user_data

class Main():
    def __init__(self) -> None:
        # Inicializamos la lista donde tu función guardará las tutorías
        self.tutorias_disponibles = []
        
        UI = TutorCompanion(check_login=self.check_login)
        UI.run()

        # Don't write anything here!!
        # This will execute when kill UI

    def check_login(self, user, psk) -> bool:
        # 1. INTENTO CON EL SERVIDOR DE CARLOS
        try:
            print("Intentando conectar con el servidor de Carlos...")
            datos_servidor = get_user_data()
            if datos_servidor:
                datos_procesados = process_data_from_user_dict(datos_servidor)
                if is_psk_and_username_valid(user=user, psk=psk, data=datos_procesados):
                    # Guardamos las tutorías reales del servidor usando tu función
                    self.tutorias_disponibles = obtener_todas_las_tutorias(datos_servidor)
                    print(f"Tutorías cargadas desde el servidor: {len(self.tutorias_disponibles)} encontradas.")
                    return True
        except Exception as e:
            print(f"El servidor externo no está disponible: {e}")

        # =======================================================================
        # 2. PLAN B (FALLBACK): SI EL SERVIDOR FALLA, USAMOS EL JSON LOCAL
        # =======================================================================
        print("Activando modo local de prueba para cargar la app...")
        
        # Ajustamos la ruta según tu estructura real de carpetas:
        # base_dir es 'APP/source'
        base_dir = os.path.dirname(os.path.abspath(__file__)) 
        # Subimos un nivel a 'APP' y entramos a 'Data/return_example.json'
        json_path = os.path.join(os.path.dirname(base_dir), "Data", "return_example.json")
        
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                datos_locales = json.load(f)
            
            datos_procesados_locales = process_data_from_user_dict(datos_locales)
            if is_psk_and_username_valid(user=user, psk=psk, data=datos_procesados_locales):
                # Usamos tu función con los datos del JSON local de prueba
                self.tutorias_disponibles = obtener_todas_las_tutorias(datos_locales)
                print("\n=================== TUS TUTORÍAS CARGADAS ===================")
                print(self.tutorias_disponibles)
                print("=============================================================\n")
                return True
        except Exception as err_local:
            print(f"Error crítico al leer el archivo de respaldo en {json_path}: {err_local}")
            
        return False


if __name__ == "__main__":
    Main()