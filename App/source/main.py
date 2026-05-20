"""Here we're gonna connect every module to UI"""
import json
import os
from ui import TutorCompanion
from modules.process_data import is_psk_and_username_valid
from modules.process_data import process_data_from_user_dict
# Importamos tu nueva función asignada
from modules.process_data import obtener_todas_las_tutorias 
from modules.get_data import get_user_data
from modules.tuto_suggestions import get_key_hours_by_identifier
from modules.ranking import get_featured_tutors

class Main():
    def __init__(self) -> None:
        # Añadimos esto para que la lista exista desde el inicio:
        self.tutorias_disponibles = []
        
        self.user_data = []

        UI = TutorCompanion(check_login=self.check_login, get_key_hours=self.get_key_hours, get_ranking=self.get_rank_tutor)
        self.UI = UI
        UI.run()

        # Don't write anything here!!
        # This will execute when kill UI

    def get_rank_tutor(self):
        return get_featured_tutors(self.user_data)

    def get_key_hours(self, identifier) -> tuple | None:
        # 1. Intentamos extraer los datos reales (del servidor o del JSON local según qué cargó primero)
        try:
            # Si ya tenemos datos locales o del servidor cargados en las validaciones
            # Intentamos pasárselos a la función de tus compañeros
            datos = self.user_data if os.environ.get("CONNECTED") == "TRUE" else None
            if datos:
                resultado = get_key_hours_by_identifier(identifier=identifier, users=datos)

                # Si la funcion devuelve None es porque el usuario no es becado o no es tutor
                # No es un bug, es una feature 😎    
                return resultado
            
        except Exception:
            pass

        # 2. SALVADA DE DESARROLLADOR (FALLBACK MOCK): 
        # Si la función de ellos devuelve None o falla porque no hay red, 
        # devolvemos (25 horas aprobadas, de 70 requeridas) para que Kivy no colapse.
        # Nota de Carlos: Tenle m[a]s f[e] a Kivy, si es un None, no se mostrar[a]n las horas y ya jsjs
        return (25, 70) 

    def check_login(self, user, psk) -> bool:
        # =======================================================================
        # 1. INTENTO CON EL SERVIDOR DE CARLOS (PLAN A)
        # =======================================================================
        try:
            print("Intentando conectar con el servidor de Carlos...")
            datos_servidor = get_user_data()

            self.user_data = datos_servidor
            
            if datos_servidor:
                datos_procesados = process_data_from_user_dict(datos_servidor)
                if is_psk_and_username_valid(user=user, psk=psk, data=datos_procesados):
                    self.tutorias_disponibles = obtener_todas_las_tutorias(datos_servidor)
                    print(f"Tutorías cargadas desde el servidor: {len(self.tutorias_disponibles)} encontradas.")
                    
                    # Activamos bandera de que el servidor respondió exitosamente
                    os.environ["CONNECTED"] = "TRUE"
                    
                    # ENVIAMOS LOS DATOS REALES A LA UI
                    dashboard = self.UI.sm.get_screen("dashboard")
                    dashboard.actualizar_tarjetas_tutorias(self.tutorias_disponibles)
                    
                    return True
        except Exception as e:
            print(f"El servidor externo no está disponible: {e}")

        # =======================================================================
        # 2. PLAN B (FALLBACK): SI EL SERVIDOR FALLA, USAMOS EL JSON LOCAL
        # =======================================================================
        print("Activando modo local de prueba para cargar la app...")
        os.environ["CONNECTED"] = "FALSE"
        
        source_dir = os.path.dirname(os.path.abspath(__file__)) 
        app_dir = os.path.dirname(source_dir)
        json_path = os.path.join(app_dir, "Data", "return_example.json")
        
        try:
            if not os.path.exists(json_path):
                json_path = os.path.join(source_dir, "Data", "return_example.json")

            with open(json_path, "r", encoding="utf-8") as f:
                datos_locales = json.load(f)
            
            datos_procesados_locales = process_data_from_user_dict(datos_locales)
            
            # Saltamos directo si es el usuario de prueba o si valida bien con el JSON
            if is_psk_and_username_valid(user=user, psk=psk, data=datos_procesados_locales) or user == "taylor@keyinstitute.edu.sv":
                self.tutorias_disponibles = obtener_todas_las_tutorias(datos_locales)
                print("\n=================== TUS TUTORÍAS CARGADAS (LOCAL) ===================")
                print(self.tutorias_disponibles)
                print("=============================================================\n")
                
                # ENVIAMOS LOS DATOS LOCALES A LA UI
                dashboard = self.UI.sm.get_screen("dashboard")
                dashboard.actualizar_tarjetas_tutorias(self.tutorias_disponibles)
                
                return True
        except Exception as err_local:
            print(f"Error crítico al leer el archivo de respaldo en {json_path}: {err_local}")
            
        return False


if __name__ == "__main__":
    Main()