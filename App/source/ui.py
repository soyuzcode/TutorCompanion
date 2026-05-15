from kivymd.app import MDApp
from kivy.uix.widget import Widget

class HelloWorld(Widget):
    pass


class TutorCompanion(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Olive"
        return HelloWorld()

    def imprimir_datos(self, rol, nombre):
        print(f"Rol seleccionado: {rol} - Usuario: {nombre}")


if __name__ == "__main__":
    TutorCompanion().run()