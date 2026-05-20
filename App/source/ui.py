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

from kivy.properties import StringProperty, ObjectProperty

# =========================================================
# WINDOW CONFIG
# =========================================================

# Window.size = (400, 700)
# Window.clearcolor = (0.05, 0.08, 0.15, 1)


# =========================================================
# CARDS
# =========================================================
class SolicitudCard(MDCard):
    name = StringProperty("")
    materia = StringProperty("")
    solicitud_id = StringProperty("")       # <--- Añade esto
    data_original = ObjectProperty(None)    # <--- Añade esto

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

class StatsScreen(MDScreen):

    stats = {}

    def load_stats(self, users: list):
        """
        Recibe usuarios desde backend o app state
        y actualiza UI
        """

        app = MDApp.get_running_app()
        self.stats = app.get_stats() # type: ignore
        self.render_stats()

    def render_stats(self):
        """
        Aquí SOLO actualizas UI bindings
        (labels, cards, etc)
        """

        self.ids.total_users.text = str(self.stats.get("total_users", 0))
        self.ids.active.text = str(self.stats.get("active", 0))
        self.ids.tutors.text = str(self.stats.get("tutors", 0))
        self.ids.avg_rating.text = str(self.stats.get("avg_rating", 0))
        self.ids.sessions.text = str(self.stats.get("sessions", 0))
        self.ids.pending.text = str(self.stats.get("pending_suggestions", 0))

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

        self.manager.current = "stats"

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
        
        # Limpiamos, dejando el título
        while len(contenedor.children) > 1:
            contenedor.remove_widget(contenedor.children[0])
            
        for sol in lista_solicitudes:
            materia = sol.get("subject", {}).get("name", "Sin materia")
            tema = sol.get("topic", "Sin tema")
            sol_id = str(sol.get("id", "0")) # Asegúrate de obtener el ID real
            
            # PASAMOS LOS NUEVOS DATOS AQUÍ
            card = SolicitudCard(
                name=tema, 
                materia=f"{materia}", 
                solicitud_id=sol_id,    # <--- Esto es clave
                data_original=sol       # <--- Esto es clave
            ) 
            contenedor.add_widget(card)

    # =====================================================
    # LÓGICA DE SOLICITUDES (ACEPTAR/RECHAZAR)
    # =====================================================

    # Biomimetismo axial 47 :p
    # Falta cargar datos en el server luego de dar aceptar o rechazar

    def manejar_decision(self, sol_id, decision, sol_data):
        """
        sol_id: El identificador único de la sugerencia.
        decision: "accepted" o "rejected".
        sol_data: El diccionario completo con la info.
        """
        print(f"Usuario decidió: {decision} sobre la solicitud {sol_id}")
        
        # 1. Lógica Visual: Remover la tarjeta de la lista de solicitudes
        contenedor = self.ids.contenedor_solicitudes
        for card in contenedor.children:
            # Aquí asumimos que la tarjeta tiene un atributo 'sol_id'
            if hasattr(card, 'solicitud_id') and card.solicitud_id == str(sol_id):
                contenedor.remove_widget(card)
                break
        
        # 2. Si fue aceptada, agregar a la lista de "Próximas Tutorías"
        if decision == "accepted":
            self.agregar_tutoria_confirmada(sol_data)

    def agregar_tutoria_confirmada(self, solicitud):
        columna_izquierda = self.ids.contenedor_izquierdo
        materia = solicitud.get("subject", {}).get("name", "Materia")
        
        nueva_tarjeta = TutoriaCard(
            materia=materia,
            estado="Confirmada",
            fecha="Nueva sesión agregada"
        )
        columna_izquierda.add_widget(nueva_tarjeta)

# ================= APP =================

class TutorCompanion(MDApp):

    def __init__(
        self,
        check_login,
        get_key_hours,
        get_ranking,
        get_tutors,
        get_stats,
        **kwargs
    ):

        super().__init__(**kwargs)

        self.check_login = check_login

        self.get_key_hours = get_key_hours

        self.get_rank_tutor = get_ranking

        self.get_tutors = get_tutors

        self.get_stats = get_stats

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
        
        Builder.load_file("ui/stats.kv")

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

        self.sm.add_widget(
            StatsScreen(
                name="stats"
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

        tutores, nombres, imagenes = self.get_tutors()

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

                image = imagenes[tutor["userId"]],

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