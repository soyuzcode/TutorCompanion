from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class HelloWorld(MDScreen):
    pass

class TutorCompanion(MDApp):
    def __init__(
            self,
            check_login,
            **kwargs):
        
        super().__init__(**kwargs)

        self.check_login = check_login

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        return HelloWorld()

    def on_login(self, user, psk):
        if self.check_login(user=user, psk=psk):
            
            print("Alright! You're good!")
        
        else:

            print("Wrong!")