from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager


# ================= SCREENS =================

class LoginScreen(MDScreen):
    pass


class DashboardScreen(MDScreen):
    pass


# ================= APP =================

class TutorCompanion(MDApp):

    def __init__(self, check_login, **kwargs):
        super().__init__(**kwargs)

        self.check_login = check_login

    def build(self):

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Cyan"

        # LOAD KV FILES
        Builder.load_file("ui/login.kv")
        Builder.load_file("ui/dashboard.kv")

        # SCREEN MANAGER
        self.sm = MDScreenManager()

        self.sm.add_widget(LoginScreen(name="login"))
        self.sm.add_widget(DashboardScreen(name="dashboard"))

        return self.sm

    def on_login(self, user, psk):

        if self.check_login(user=user, psk=psk):

            print("Alright! You're good!")

            self.sm.current = "dashboard"

        else:

            print("Wrong!")