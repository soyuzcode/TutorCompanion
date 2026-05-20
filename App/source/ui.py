from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase

from kivy.properties import (
    StringProperty,
    BooleanProperty
)

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.menu import MDDropdownMenu

# =========================================================
# WINDOW CONFIG
# =========================================================

# Window.size = (400, 700)
# Window.clearcolor = (0.05, 0.08, 0.15, 1)


# =========================================================
# CARDS
# =========================================================
class SolicitudCard(MDCard):
    # Estas variables deben coincidir con lo que usas en components.kv
    name = StringProperty("")
    materia = StringProperty("")

class TutoriaCard(MDCard):

    materia = StringProperty("")

    estado = StringProperty("")

    fecha = StringProperty("")


class ImpactCard(MDCard):
    pass


class TutorCard(MDCard):

    position = StringProperty("")

    name = StringProperty("")

    rating = StringProperty("0")


class TutorSelectCard(MDCard):

    name = StringProperty("")

    rating = StringProperty("")

    image = StringProperty("")

    tutor_id = StringProperty("")

    selected = BooleanProperty(False)


# =========================================================
# SCREENS
# =========================================================

class LoginScreen(MDScreen):
    pass

class SugerirTutoriaScreen(MDScreen):
    pass

class DashboardScreen(MDScreen):

    # =====================================================
    # NAVIGATION
    # =====================================================

    def ir_a_sugerir_tutoria(self):

        app = MDApp.get_running_app()

        app.load_tutors() # type: ignore

        app.setup_subject_dropdown() # type: ignore

        self.manager.transition.direction = "left"

        self.manager.current = "sugerir_tutoria"

    def ir_a_buscar_tutorias(self):

        print(
            "Acceso a: Buscador de Tutorías Disponibles"
        )

    def ir_a_mis_tutorias(self):

        print(
            "Acceso a: Historial de Tutorías"
        )

    def ver_ratings(self):

        print(
            "Acceso a: Panel de Calificaciones"
        )

    def ver_estadisticas(self):

        print(
            "Acceso a: Estadísticas"
        )

    # =====================================================
    # USER INFO
    # =====================================================

    def actualizar_usuario(self, nombre, rol):

        self.ids.label_nombre.text = (
            f"Hola, {nombre}! 👋"
        )

        self.ids.label_rol.text = (
            f"Rol: {rol}"
        )

    # =====================================================
    # TUTORIAS
    # =====================================================

    def actualizar_tarjetas_tutorias(
        self,
        lista_tutorias
    ):

        columna_izquierda = (
            self.ids.contenedor_izquierdo
        )

        columna_izquierda.clear_widgets()

        for tutoria in lista_tutorias:

            materia_tuto = tutoria[1]

            fecha_tuto = tutoria[3]

            hora_tuto = tutoria[4]

            estado_tuto = "Confirmada"

            nueva_tarjeta = TutoriaCard(

                materia = materia_tuto,

                estado = estado_tuto,
                fecha = f"{fecha_tuto} - {hora_tuto}"
            )
                
            # Agregamos la tarjeta real al contenedor con scroll
            columna_izquierda.add_widget(nueva_tarjeta)

    def actualizar_solicitudes(self, lista_solicitudes):
        contenedor = self.ids.contenedor_solicitudes
        
        # Limpiamos, dejando el título (asumiendo que es el primer hijo)
        while len(contenedor.children) > 1:
            contenedor.remove_widget(contenedor.children[0])
            
        for sol in lista_solicitudes:
            # AHORA ACCEDEMOS POR CLAVE, YA QUE 'sol' ES UN DICCIONARIO
            materia = sol.get("subject", {}).get("name", "Sin materia")
            tema = sol.get("topic", "Sin tema")
            estado = sol.get("status", "pending")
            
            # Ajusta esto según lo que acepte tu SolicitudCard
            # Si tu tarjeta solo acepta 'name' y 'materia', usa 'tema' como nombre o lo que prefieras
            card = SolicitudCard(name=tema, materia=f"{materia} ({estado})") 
            contenedor.add_widget(card)

# ================= APP =================

class TutorCompanion(MDApp):

    def __init__(
        self,
        check_login,
        get_key_hours,
        get_ranking,
        **kwargs
    ):

        super().__init__(**kwargs)

        self.check_login = check_login

        self.get_key_hours = get_key_hours

        self.get_rank_tutor = get_ranking

        self.current_user = ""

    # =====================================================
    # BUILD
    # =====================================================

    def build(self):

        LabelBase.register(
            name = "Emoji",
            fn_regular = (
                "C:/Windows/Fonts/seguiemj.ttf"
            )
        )

        self.theme_cls.theme_style = "Light"

        self.theme_cls.primary_palette = "Cyan"

        # ================================================
        # LOAD KV FILES
        # ================================================

        Builder.load_file("ui/login.kv")

        Builder.load_file("ui/components.kv")

        Builder.load_file("ui/dashboard.kv")

        Builder.load_file("ui/sugerir_tutoria.kv")

        # ================================================
        # SCREEN MANAGER
        # ================================================

        self.sm = MDScreenManager()

        self.sm.add_widget(
            LoginScreen(name="login")
        )

        self.sm.add_widget(
            DashboardScreen(name="dashboard")
        )

        self.sm.add_widget(
            SugerirTutoriaScreen(
                name="sugerir_tutoria"
            )
        )

        self.sm.current = "login"

        return self.sm

    # =====================================================
    # SUBJECT DROPDOWN
    # =====================================================

    def setup_subject_dropdown(self):

        sugerir_screen = self.sm.get_screen(
            "sugerir_tutoria"
        )

        dropdown_item = (
            sugerir_screen.ids.materia_dropdown
        )

        materias = [

            "Calculo 1",

            "Fisica 1",

            "Programacion 1",

            "Desarrollo Personal",

            "Introduccion a la Ingenieria"
        ]

        menu_items = []

        for materia in materias:

            menu_items.append(
                {
                    "text": materia,

                    "viewclass": "OneLineListItem",

                    "on_release":
                    lambda x=materia:
                    self.set_subject(x)
                }
            )

        self.subject_menu = MDDropdownMenu(

            caller = dropdown_item,

            items = menu_items,

            width_mult = 5,

            md_bg_color = (
                0.15,
                0.17,
                0.25,
                1
            )
        )


    def set_subject(self, materia):

        sugerir_screen = self.sm.get_screen(
            "sugerir_tutoria"
        )

        dropdown_item = (
            sugerir_screen.ids.materia_dropdown
        )

        dropdown_item.text = materia

        self.subject_menu.dismiss()

    # =====================================================
    # LOAD TUTORS
    # =====================================================

    def load_tutors(self):

        # ================================================
        # PLACEHOLDER DATA
        # ================================================

        tutores = [

            {
                "userId": 6,
                "rating": 4.8
            },

            {
                "userId": 8,
                "rating": 4.5
            },

            {
                "userId": 10,
                "rating": 5.0
            }
        ]

        nombres = {

            6: "Andrea López",

            8: "Carlos Méndez",

            10: "María Fernanda"
        }

        # ================================================
        # GET SCREEN
        # ================================================

        sugerir_screen = self.sm.get_screen(
            "sugerir_tutoria"
        )

        container = (
            sugerir_screen.ids.tutor_container
        )

        container.clear_widgets()

        # ================================================
        # GENERATE CARDS
        # ================================================

        for i, tutor in enumerate(tutores):

            card = TutorSelectCard(

                name = nombres[tutor["userId"]],

                rating = str(tutor["rating"]),

                image = (
                    f"https://i.pravatar.cc/"
                    f"150?img={i+10}"
                ),

                tutor_id = str(
                    tutor["userId"]
                )
            )

            container.add_widget(card)

    # =====================================================
    # DASHBOARD DATA
    # =====================================================

    def load_data_on_dashboard(self):

        # ================================================
        # RANKING
        # ================================================

        data = self.get_rank_tutor()

        dashboard = self.sm.get_screen(
            "dashboard"
        )

        container = dashboard.ids.tutor_container

        container.clear_widgets()

        if data is not None:

            for i, tutor in enumerate(data):

                card = TutorCard(

                    position = str(i + 1),

                    name = tutor["name"],

                    rating = str(
                        tutor["rating"]
                    )
                )

                container.add_widget(card)

        # ================================================
        # IMPACT CARD
        # ================================================

        data = self.get_key_hours(
            self.current_user
        )

        dashboard = self.sm.get_screen(
            "dashboard"
        )

        card = dashboard.ids.impact_card

        if data is None:

            card.opacity = 0

            card.disabled = True

            card.height = 0

            return

        approved_hours, total_hours = data

        progress = int(
            (approved_hours / total_hours) * 100
        )

        card.opacity = 1

        card.disabled = False

        card.current_hours = approved_hours

        card.total_hours = total_hours

        card.progress_value = progress

    # =====================================================
    # LOGIN
    # =====================================================

    def on_login(self, user, psk):

        self.current_user = user

        if self.check_login(
            user=user,
            psk=psk
        ):

            print("Alright! You're good!")

            self.sm.transition.direction = "left"

            self.load_data_on_dashboard()

            self.sm.current = "dashboard"

        else:

            print("Wrong!")