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

