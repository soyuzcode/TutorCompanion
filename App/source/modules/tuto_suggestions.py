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