from kivy.lang import Builder
from kivy.core.window import Window

from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.screenmanager import MDScreenManager
from kivy.properties import StringProperty
from kivy.factory import Factory


# WINDOW CONFIG
#Window.size = (400, 700)
#Window.clearcolor = (0.05, 0.08, 0.15, 1)


# =========================================================
# CARDS (¡Primero definimos las clases en Python!)
# =========================================================

class TutoriaCard(MDCard):
    materia = StringProperty("")
    estado = StringProperty("")
    fecha = StringProperty("")  # 🌟 Declarada explícitamente en Python antes del .kv

class ImpactCard(MDCard):
    pass

class TutorCard(MDCard):
    position = StringProperty("")
    name = StringProperty("")
    rating = StringProperty("0")


# ================= SCREENS =================

class LoginScreen(MDScreen):
    pass


class DashboardScreen(MDScreen):

    def ir_a_sugerir_tutoria(self):
        print(" Acceso a: Formulario de Sugerir Tutoría (Módulo en desarrollo)")

    def ir_a_buscar_tutorias(self):
        print(" Acceso a: Buscador de Tutorías Disponibles (Módulo en desarrollo)")

    def ir_a_mis_tutorias(self):
        print(" Acceso a: Historial de Tutorías del Usuario (Módulo en desarrollo)")
        
    def ver_ratings(self):
        print(" Acceso a: Panel de Calificaciones del Tutor (Módulo en desarrollo)")
        
    def ver_estadisticas(self):
        print(" Acceso a: Gráficas de Progreso y Horas (Módulo en desarrollo)")
    
    def actualizar_tarjetas_tutorias(self, lista_tutorias):
        """
        Recibe la lista de listas:
        [[id, materia, tema, fecha, hora], ...] y pinta tarjetas reales.
        """
        columna_izquierda = self.ids.contenedor_izquierdo
        
        # Limpiamos antes de agregar para que no se dupliquen al recargar
        columna_izquierda.clear_widgets()
        
        for tutoria in lista_tutorias:
            materia_tuto = tutoria[1]
            fecha_tuto = tutoria[3]  # Extraemos la fecha real
            hora_tuto = tutoria[4]   # Extraemos la hora real
            estado_tuto = "Confirmada" 
            
            # 🌟 CREAMOS LA TARJETA PASÁNDOLE LAS PROPIEDADES DIRECTAMENTE:
            nueva_tarjeta = TutoriaCard(
                materia = materia_tuto,
                estado = estado_tuto,
                fecha = f"{fecha_tuto} - {hora_tuto}"
            )
                
            # Agregamos la tarjeta real al contenedor con scroll
            columna_izquierda.add_widget(nueva_tarjeta)

    def actualizar_solicitudes(self, lista_solicitudes):
        """
        Esta es la función que tu main.py estaba buscando.
        """
        # Aquí conectamos con el ID que acabas de poner en el .kv
        contenedor = self.ids.contenedor_solicitudes
        
        # Limpiamos las tarjetas viejas (dejando el título "Solicitudes")
        # Si tienes hijos, removemos desde el último hacia atrás para no borrar el Label
        while len(contenedor.children) > 1:
            contenedor.remove_widget(contenedor.children[0])
            
        # Agregamos las nuevas tarjetas reales
        for sol in lista_solicitudes:
            nombre, materia, estado = sol
            # Creamos la tarjeta (asegúrate de que SolicitudCard acepte estos parámetros)
            card = SolicitudCard(name=nombre, materia=f"Solicita {materia}") 
            contenedor.add_widget(card)

# ================= APP =================

class TutorCompanion(MDApp):

    def __init__(self, 
                 check_login, 
                 get_key_hours,
                 get_ranking,
                 **kwargs):

        super().__init__(**kwargs)

        self.check_login = check_login
        self.get_key_hours = get_key_hours
        self.get_rank_tutor = get_ranking

        self.current_user = ""

    def build(self):

        LabelBase.register(
            name="Emoji",
            fn_regular="C:/Windows/Fonts/seguiemj.ttf"
        )

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Cyan"

        # LOAD KV FILES (Ahora sí, cuando Kivy lea esto, ya conocerá las propiedades de arriba)
        Builder.load_file("ui/login.kv")
        Builder.load_file("ui/components.kv")
        Builder.load_file("ui/dashboard.kv")

        # SCREEN MANAGER
        self.sm = MDScreenManager()

        self.sm.add_widget(LoginScreen(name="login"))
        self.sm.add_widget(DashboardScreen(name="dashboard"))

        self.sm.current = "login"

        return self.sm

    def load_data_on_dashboard(self):

        # RANKING CARDS
        data = self.get_rank_tutor()
        dashboard = self.sm.get_screen("dashboard")
        container = dashboard.ids.tutor_container

        container.clear_widgets()
        
        if data is not None:
            for i, tutor in enumerate(data):
                card = TutorCard(
                    position = str(i +1),
                    name = tutor["name"],
                    rating = str(tutor["rating"])
                )

                container.add_widget(card)

        # IMPACT CARD
        data = self.get_key_hours(self.current_user)

        dashboard = self.sm.get_screen("dashboard")
        card = dashboard.ids.impact_card

        if data is None:
            card.opacity = 0
            card.disabled = True
            card.height = 0
            return

        approved_hours, total_hours = data

        progress = int((approved_hours / total_hours) * 100)

        card.opacity = 1
        card.disabled = False

        card.current_hours = approved_hours
        card.total_hours = total_hours
        card.progress_value = progress

    def on_login(self, user, psk):

        self.current_user = user

        if self.check_login(user=user, psk=psk):
            print("Alright! You're good!")
            self.sm.transition.direction = "left"
            self.load_data_on_dashboard()
            self.sm.current = "dashboard"
        else:
            print("Wrong!")

# Ajuste pendiente: mejorar formato de fechas de tutorias 