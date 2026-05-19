from kivy.lang import Builder
from kivy.core.window import Window

from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
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
        # 1. Obtenemos el contenedor de la columna izquierda por su ID
        columna_izquierda = self.ids.contenedor_izquierdo
        
        # 2. Buscamos la clase de tarjeta personalizada que hicieron tus compañeros
        # Usamos Factory para poder crear copias de TutoriaCard desde Python
        TutoriaCardClass = Factory.TutoriaCard
        
        # 3. Recorremos tus 5 tutorías reales del servidor
        for tutoria in lista_tutorias:
            id_tuto = tutoria[0]
            materia_tuto = tutoria[1]
            tema_tuto = tutoria[2]
            fecha_tuto = tutoria[3]
            hora_tuto = tutoria[4]
            
            # 4. Instanciamos una nueva tarjeta pasándole tus variables reales
            # Nota: Si tus compañeros definieron propiedades específicas en su componente 
            # como 'fecha' o 'hora', se las pasamos aquí. 
            nueva_tarjeta = TutoriaCardClass(
                materia=f"{materia_tuto}",
                # Si su componente usa una propiedad de texto interna, combinamos la info útil:
                # O si tiene campos dedicados en el kv, los adaptas aquí.
            )
            
            # Agregamos la tarjeta real al final de la columna izquierda
            columna_izquierda.add_widget(nueva_tarjeta)

# ================= APP =================

class TutorCompanion(MDApp):

    def __init__(self, check_login, **kwargs):

        super().__init__(**kwargs)

        self.check_login = check_login

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

    def on_login(self, user, psk):

        if self.check_login(user=user, psk=psk):

            print("Alright! You're good!")

            self.sm.transition.direction = "left"
            self.sm.current = "dashboard"

        else:

            print("Wrong!")