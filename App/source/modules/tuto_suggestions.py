def sugerir_tutorias(materia, fecha, rating_minimo=0, becado=None, horas_minimas=0):
    """
    Función que genera un diccionario con filtros para sugerencias de tutorías.
    """
    sugerencia = {
        "materia": materia,
        "fecha": fecha,
        "ratingMinimo": rating_minimo,
        "becado": becado,
        "horasMinimas": horas_minimas
    }
    return sugerencia

def get_key_hours_by_identifier(identifier, users):
    user = None

    if isinstance(identifier, int):
        user = next((u for u in users if u["id"] == identifier), None)

    elif isinstance(identifier, str):
        identifier_clean = identifier.strip().lower()

        if "@" in identifier_clean:
            user = next((u for u in users if u["email"].lower() == identifier_clean), None)
        else:
            user = next((u for u in users if u["name"].lower() == identifier_clean), None)

    if user is None:
        return None

    if not user.get("isBecado") or not user.get("tutorProfile"):
        print("JAJA DEBUGGING AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADNIASJCNKVDJSNCD VM  BJRFHBEDJSKCNVF BJRHBGEKDSNCMNVF BRJHNEKDCDN VFRJHGE")
        return None

    approved_hours = int(user["tutorProfile"].get("approvedHours"))
    required_hours = 70  # Horas key necesarias

    return (approved_hours, required_hours)  # Tupla


def get_name(identifier, users):
    user = None

    if isinstance(identifier, int):
        user = next((u for u in users if u["id"] == identifier), None)

    elif isinstance(identifier, str):
        identifier_clean = identifier.strip().lower()

        if "@" in identifier_clean:
            user = next((u for u in users if u["email"].lower() == identifier_clean), None)
        else:
            user = next((u for u in users if u["name"].lower() == identifier_clean), None)

    if user is None:
        return None

    if not user.get("isBecado") or not user.get("tutorProfile"):
        return None

    return user["name"]




def get_name_by_identifier(identifier, users):
    user = None

    if isinstance(identifier, int):
        user = next((u for u in users if u["id"] == identifier), None)

    elif isinstance(identifier, str):
        identifier_clean = identifier.strip().lower()

        if "@" in identifier_clean:
            user = next((u for u in users if u["email"].lower() == identifier_clean), None)
        else:
            user = next((u for u in users if u["name"].lower() == identifier_clean), None)

    if user is None:
        return None

    if not user.get("isBecado") or not user.get("tutorProfile"):
        return None

    return user["name"]


def get_mentorias_by_identifier(identifier, users):
    user = None

    if isinstance(identifier, int):
        user = next((u for u in users if u["id"] == identifier), None)

    elif isinstance(identifier, str):
        identifier_clean = identifier.strip().lower()

        if "@" in identifier_clean:
            user = next((u for u in users if u["email"].lower() == identifier_clean), None)
        else:
            user = next((u for u in users if u["name"].lower() == identifier_clean), None)

    if user is None:
        return None

    activas = []
    no_activas = []
    completadas = []

    # --- Como tutor ---
    for session in user.get("sessions", []):
        entry = {"sesion": session, "rol": "tutor"}

        if session.get("attended") == True:
            completadas.append(entry)
        elif session.get("tutorStatus") == "ACCEPTED":
            activas.append(entry)
        else:
            no_activas.append(entry)

    # --- Como estudiante ---
    for session in user.get("enrolledSessions", []):
        entry = {"sesion": session, "rol": "estudiante"}

        if session.get("attended") == True:
            completadas.append(entry)
        elif session.get("studentStatus") == "ACCEPTED":
            activas.append(entry)
        else:
            no_activas.append(entry)

    return {"activas": activas, "no_activas": no_activas, "completadas": completadas}

