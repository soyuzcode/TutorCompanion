from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class HelloWorld(MDScreen):
    pass

class TutorCompanion(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        return HelloWorld()

    def imprimir_datos(self, rol, nombre):
        print(f"Rol seleccionado: {rol} - Usuario: {nombre}")