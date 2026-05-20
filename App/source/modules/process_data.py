"""Here we're gonna process every data when we need on ui"""

def validar_correo(texto):
    if texto.endswith("@keyinstitute.edu.sv"):
        if " " not in texto:
            return True
    return False


# Asignado: Michelle
def obtener_todas_las_tutorias(data: list | dict | None) -> list[list[str]]:
    """
    Función universal: intenta extraer datos de 'sessions' (servidor) 
    o de 'subjects'/'sentSuggestions' (prueba).
    """
    if data is None:
        return []

    resultado = []
    ids_visitados = set()

    for user in data:
        # --- ESTRATEGIA 1: Intentar buscar en 'sessions' (Formato Servidor) ---
        sessions = user.get("sessions", [])
        for sess in sessions:
            sess_id = str(sess.get("id"))
            if sess_id not in ids_visitados:
                ids_visitados.add(sess_id)
                full_start = sess.get("startTime", "T--")
                fecha, hora = full_start.split("T") if "T" in full_start else (full_start, "No definida")
                resultado.append([sess_id, user.get("subjects", [{}])[0].get("name", "Materia"), sess.get("topic", "General"), fecha, hora])

        # --- ESTRATEGIA 2: Intentar buscar en 'sentSuggestions' (Formato Prueba) ---
        # --- ESTRATEGIA 2: Intentar buscar en 'sentSuggestions' (Formato Prueba) ---
        suggestions = user.get("sentSuggestions", [])
        for sug in suggestions:
            sug_id = str(sug.get("id"))
            if sug_id not in ids_visitados:
                ids_visitados.add(sug_id)
                full_date = sug.get("createdAt", "T--")
                
                # AQUÍ ESTÁ EL CAMBIO: 'full_date' en lugar de 'full_start'
                fecha, hora = full_date.split("T") if "T" in full_date else (full_date, "12:00 PM")
                
                resultado.append([sug_id, sug.get("subject", {}).get("name", "Materia"), sug.get("topic", "General"), fecha, hora])

    return resultado


# Asignado: Cristina
def process_data_from_user_dict(data:dict | None):
    """Dado un diccionario (llamado data) de la forma escrita en Data/return_example.json
        Retorne una lista de listas asi:
            [
                [NOMBRE1, EMAIL1, KEYCODE1, PASSWORD1],
                [NOMBRE2, EMAIL2, KEYCODE2, PASSWORD2],
                [NOMBRE3, EMAIL3, KEYCODE3, PASSWORD3]
            ]
            
        Con todos los nombres, emails, key codes y passwords en el diccionario."""

    if data == None:
        return []

    result: list[list[str]] = []

    for user in data:
        user_id = user.get("id")

        keycode = f"KEY_{user_id:06d}"

        result.append([
            user.get("name"),
            user.get("email"),
            keycode,
            user.get("passwordHash")
        ])

    return result


# Asignado: Miguel
def is_psk_and_username_valid(user:str, psk:str, data: list[list[str]]) -> bool:
    """Dado una lista de listas de la siguiente forma:
        [
            [NOMBRE1, EMAIL1, KEYCODE1, PASSWORD1],
            [NOMBRE2, EMAIL2, KEYCODE2, PASSWORD2],
            [NOMBRE3, EMAIL3, KEYCODE3, PASSWORD3]
        ]
        
        Verifique si user es igual a nombre, email, o key code.
        Si es igual a uno de estos, verifique si PASSWORD (el cuarto elemento)
        es igual a psk.
        
        Devuelva Verdadero si cumple el requisito, y Falso si no."""

    for persona in data:

        nombre = persona[0]
        email = persona[1]
        keycode = persona[2]
        password = persona[3]

        if user == nombre or user == email or user == keycode:

            if psk == password:
                return True

    return False


def convert_dict_to_list_of_list(user_data:dict):
    """[
            [NOMBRE1, EMAIL1, KEYCODE1, PASSWORD1],
            [NOMBRE2, EMAIL2, KEYCODE2, PASSWORD2],
            [NOMBRE3, EMAIL3, KEYCODE3, PASSWORD3]
        ]
        
        convierta json respoonse en esto"""
    pass

def find_user_id(users, identifier: str) -> int | None:
    """Resuelve nombre, email, KEY_XXXXXX o id numérico al id de usuario."""
    if not users or not identifier:
        return None

    identifier = identifier.strip()

    for user in users:
        user_id = user.get("id")
        keycode = f"KEY_{user_id:06d}"

        if identifier in (
            user.get("name"),
            user.get("email"),
            keycode,
            str(user_id),
        ):
            return user_id

    return None


def submit_review_local(
    users,
    tutor_id: int,
    student_id: int,
    rating: int,
    comment: str = "",
) -> bool:
    """Guarda una review en memoria cuando no hay servidor."""
    tutor = next((u for u in users if u.get("id") == tutor_id), None)
    student = next((u for u in users if u.get("id") == student_id), None)

    if not tutor or not student:
        return False

    if not tutor.get("tutorProfile"):
        return False

    written = student.setdefault("writtenReviews", [])
    received = tutor.setdefault("receivedReviews", [])

    for review in written:
        if review.get("tutor", {}).get("id") == tutor_id:
            return False

    new_review = {
        "id": len(written) + len(received) + 1,
        "tutor": {"id": tutor_id, "name": tutor.get("name")},
        "student": {"id": student_id, "name": student.get("name")},
        "rating": rating,
        "comment": comment or "",
    }

    written.append(new_review)
    received.append(new_review)

    ratings = [
        r["rating"]
        for r in received
        if r.get("rating") is not None
    ]

    if ratings:
        tutor["tutorProfile"]["rating"] = round(
            sum(ratings) / len(ratings),
            1,
        )

    return True


def extraer_tutores(data):
    tutores = []
    nombres = {}
    imagenes = {}

    for user in data:
        tutor_profile = user.get("tutorProfile")

        # Solo usuarios que sí son tutores
        if tutor_profile is not None:
            user_id = user["id"]

            tutores.append({
                "userId": user_id,
                "rating": tutor_profile["rating"]
            })

            nombres[user_id] = user["name"]
            imagenes[user_id] = user["pfp"]

    # Ordenar de mayor rating a menor
    tutores.sort(key=lambda x: x["rating"], reverse=True)

    return tutores, nombres, imagenes

# process_data.py

def process_stats(users) -> dict:
    """
    Recibe lista de users desde backend (Spring)
    y retorna un diccionario de stats listo para UI
    """

    total_users = len(users)

    active = len([u for u in users if u.get("state") == "active"])
    banned = len([u for u in users if u.get("state") == "banned"])
    becados = len([u for u in users if u.get("isBecado")])

    tutors = [u for u in users if u.get("tutorProfile")]
    total_tutors = len(tutors)

    avg_rating = (
        sum(t["tutorProfile"]["rating"] for t in tutors) / len(tutors)
        if tutors else 0
    )

    total_reviews = sum(len(u.get("writtenReviews", [])) for u in users)

    total_sessions = sum(len(u.get("sessions", [])) for u in users)

    pending_suggestions = sum(
        len([
            s for s in u.get("receivedSuggestions", [])
            if s.get("status") == "pending"
        ])
        for u in users
    )

    return {
        "total_users": total_users,
        "active": active,
        "banned": banned,
        "becados": becados,
        "tutors": total_tutors,
        "avg_rating": round(avg_rating, 2),
        "reviews": total_reviews,
        "sessions": total_sessions,
        "pending_suggestions": pending_suggestions
    }

def process_user_stats(users, identifier) -> dict:
    """
    users: lista completa de usuarios
    identifier: id, email o name
    """

    # ================= FIND USER =================
    user = next(
        (
            u for u in users
            if u.get("id") == identifier
            or u.get("email") == identifier
            or u.get("name") == identifier
        ),
        None
    )

    if not user:
        return {
            "error": "User not found"
        }

    # ================= PROCESS STATS =================
    return {
        "id": user.get("id"),
        "name": user.get("name", ""),
        "email": user.get("email", ""),
        "pfp": user.get("pfp", ""),
        "state": user.get("state", ""),

        "becado": "Becado" if user.get("isBecado") else "No becado",

        "rating": (
            user.get("tutorProfile", {}).get("rating", 0)
            if user.get("tutorProfile")
            else 0
        ),

        "sessions": len(user.get("sessions", [])),
        "reviews": len(user.get("writtenReviews", [])),
        "subjects": len(user.get("subjects", [])),

        "pending": sum(
            1 for s in user.get("receivedSuggestions", [])
            if s.get("status") == "pending"
        )
    }