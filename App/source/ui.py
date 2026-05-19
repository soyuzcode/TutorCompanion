from kivy.lang import Builder
from kivy.core.window import Window

from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.screenmanager import MDScreenManager

from kivy.factory import Factory


# WINDOW CONFIG
#Window.size = (400, 700)
#Window.clearcolor = (0.05, 0.08, 0.15, 1)


# ================= SCREENS =================

class LoginScreen(MDScreen):
    pass


class DashboardScreen(MDScreen):
    
    def actualizar_tarjetas_tutorias(self, lista_tutorias):
        """
        Recibe la lista de listas generada por Yulissa:
        [[id, materia, tema, fecha, hora], ...] y pinta tarjetas reales.
        """
        columna_izquierda = self.ids.contenedor_izquierdo
        TutoriaCardClass = Factory.TutoriaCard
        
        for tutoria in lista_tutorias:
            materia_tuto = tutoria[1]
            estado_tuto = "Confirmada" # Un valor por defecto para el diseño
            
            # 1. Creamos la tarjeta VACÍA (así no lanza el error de propiedad)
            nueva_tarjeta = TutoriaCardClass()
            
            # 2. Si tus compañeros definieron la tarjeta con propiedades internas de texto,
            # intentamos asignárselas directamente al componente.
            if hasattr(nueva_tarjeta, "materia"):
                nueva_tarjeta.materia = materia_tuto
            if hasattr(nueva_tarjeta, "estado"):
                nueva_tarjeta.estado = estado_tuto
                
            # Agregamos la tarjeta real al contenedor
            columna_izquierda.add_widget(nueva_tarjeta)

# ================= CARDS =================

class ImpactCard(MDCard):
    pass

# ================= APP =================

class TutorCompanion(MDApp):

    def __init__(self, check_login, get_key_hours,**kwargs):

        super().__init__(**kwargs)

        self.check_login = check_login
        self.get_key_hours = get_key_hours

    def build(self):

        LabelBase.register(
            name="Emoji",
            fn_regular="C:/Windows/Fonts/seguiemj.ttf"
        )

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Cyan"

        # LOAD KV FILES
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
        approved_hours, total_hours = self.get_key_hours()

        progress = int((approved_hours / total_hours) * 100)

        dashboard = self.sm.get_screen("dashboard")

        dashboard.ids.impact_card.current_hours = approved_hours
        dashboard.ids.impact_card.total_hours = total_hours
        dashboard.ids.impact_card.progress_value = progress

    def on_login(self, user, psk):

        if self.check_login(user=user, psk=psk):

            print("Alright! You're good!")

            self.sm.transition.direction = "left"
            self.sm.current = "dashboard"

        else:

            print("Wrong!")