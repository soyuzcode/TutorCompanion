"""Here we're gonna connect every module to UI"""
import json
import os
from ui import TutorCompanion
from modules.process_data import is_psk_and_username_valid
from modules.process_data import process_data_from_user_dict
# Solo importamos tutorías (el viejo formato) y get_user_data/get_sugerencias_reales
from modules.process_data import obtener_todas_las_tutorias 
from modules.get_data import get_user_data, get_sugerencias_reales, post_review
from modules.process_data import find_user_id, submit_review_local
from modules.tuto_suggestions import get_key_hours_by_identifier
from modules.ranking import get_featured_tutors
from modules.process_data import extraer_tutores
from modules.process_data import process_user_stats

class Main():
    def __init__(self) -> None:
        self.tutorias_disponibles = []
        self.solicitudes_pendientes = [] # Nueva lista para solicitudes
        self.user_data = []

        UI = TutorCompanion(
            check_login=self.check_login,
            get_key_hours=self.get_key_hours,
            get_ranking=self.get_rank_tutor,
            get_tutors=self.extraer_tutor_plural,
            get_stats=self.get_stats,
            submit_review=self.submit_review,
        )
        self.UI = UI
        UI.run()

    def get_stats(self, user):
        return process_user_stats(self.user_data, user)

    def extraer_tutor_plural(self):
        return extraer_tutores(self.user_data)

    def get_rank_tutor(self):
        return get_featured_tutors(self.user_data)

    def submit_review(
        self,
        tutor_id: int,
        rating: int,
        comment: str = "",
    ) -> bool:
        if not self.user_data:
            return False

        student_id = find_user_id(
            self.user_data,
            self.UI.current_user,
        )

        if not student_id:
            print("No se pudo identificar al estudiante")
            return False

        if os.environ.get("CONNECTED") == "TRUE":
            result = post_review(
                tutor_id,
                student_id,
                rating,
                comment,
            )
            if result:
                datos = get_user_data()
                if datos:
                    self.user_data = datos
                return True
            return False

        return submit_review_local(
            self.user_data,
            tutor_id,
            student_id,
            rating,
            comment,
        )

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
                    # CARGAMOS TUTORÍAS DEL JSON VIEJO
                    self.tutorias_disponibles = obtener_todas_las_tutorias(datos_servidor)
                    
                    # CARGAMOS SOLICITUDES DEL NUEVO ENDPOINT
                    self.solicitudes_pendientes = get_sugerencias_reales() 
                    
                    print(f"DEBUG: Solicitudes reales encontradas: {self.solicitudes_pendientes}")

                    os.environ["CONNECTED"] = "TRUE"
                    
                    dashboard = self.UI.sm.get_screen("dashboard")
                    dashboard.actualizar_tarjetas_tutorias(self.tutorias_disponibles)
                    dashboard.actualizar_solicitudes(self.solicitudes_pendientes)
                    
                    return True
        except Exception as e:
            print(f"El servidor no está disponible: {e}")

        # =======================================================================
        # 2. PLAN B (LOCAL) - SI FALLA EL SERVIDOR
        # =======================================================================
        print("Activando modo local...")
        os.environ["CONNECTED"] = "FALSE"
        # Aquí puedes dejar que cargue las locales si quieres, 
        # pero ya tienes la lógica maestra arriba lista.
        
        return False

if __name__ == "__main__":
    Main()