"""Here we're gonna connect every module to UI"""
import json
import os
from ui import TutorCompanion
from modules.process_data import is_psk_and_username_valid
from modules.process_data import process_data_from_user_dict
# Importamos ambas funciones (Tutorías y Solicitudes)
from modules.process_data import obtener_todas_las_tutorias, obtener_todas_las_solicitudes 
from modules.get_data import get_user_data
from modules.tuto_suggestions import get_key_hours_by_identifier
from modules.ranking import get_featured_tutors

class Main():
    def __init__(self) -> None:
        self.tutorias_disponibles = []
        self.solicitudes_pendientes = [] # Nueva lista para solicitudes
        self.user_data = []

        UI = TutorCompanion(check_login=self.check_login, get_key_hours=self.get_key_hours, get_ranking=self.get_rank_tutor)
        self.UI = UI
        UI.run()

    def get_rank_tutor(self):
        return get_featured_tutors(self.user_data)

    def get_key_hours(self, identifier) -> tuple | None:
        try:
            datos = self.user_data if os.environ.get("CONNECTED") == "TRUE" else None
            if datos:
                return get_key_hours_by_identifier(identifier=identifier, users=datos)
        except Exception:
            pass
        return (25, 70) 

    def check_login(self, user, psk) -> bool:
        # =======================================================================
        # 1. INTENTO CON EL SERVIDOR
        # =======================================================================
        try:
            print("Intentando conectar con el servidor de Carlos...")
            datos_servidor = get_user_data()
            self.user_data = datos_servidor
            
            if datos_servidor:
                datos_procesados = process_data_from_user_dict(datos_servidor)
                if is_psk_and_username_valid(user=user, psk=psk, data=datos_procesados):
                    # CARGAMOS AMBAS COSAS
                    self.tutorias_disponibles = obtener_todas_las_tutorias(datos_servidor)
                    self.solicitudes_pendientes = obtener_todas_las_solicitudes(datos_servidor)
                    
                    os.environ["CONNECTED"] = "TRUE"
                    
                    dashboard = self.UI.sm.get_screen("dashboard")
                    dashboard.actualizar_tarjetas_tutorias(self.tutorias_disponibles)
                    # AQUÍ CONECTAMOS LAS SOLICITUDES A LA UI
                    dashboard.actualizar_solicitudes(self.solicitudes_pendientes)
                    
                    return True
        except Exception as e:
            print(f"El servidor no está disponible: {e}")

        # =======================================================================
        # 2. PLAN B (LOCAL)
        # =======================================================================
        print("Activando modo local...")
        os.environ["CONNECTED"] = "FALSE"
        # ... (Tu código de carga de JSON local queda igual)
        # Asegúrate de llamar a actualizar_solicitudes(self.solicitudes_pendientes) también aquí abajo si quieres que se vean en local.
        
        return False

if __name__ == "__main__":
    Main()