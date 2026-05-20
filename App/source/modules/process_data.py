"""Here we're gonna process every data when we need on ui"""

def validar_correo(texto):
    if texto.endswith("@keyinstitute.edu.sv"):
        if " " not in texto:
            return True
    return False


# Asignado: Michelle
# Asignado: Michelle
def obtener_todas_las_tutorias(data: list | dict | None) -> list[list[str]]:
    """
    Recorre usuarios, extrae tutorías de 'subjects' y sugerencias de 'sentSuggestions',
    formateando la fecha correctamente.
    """
    if data is None:
        return []

    resultado = []
    ids_visitados = set()

    for user in data:
        # 1. Procesar subjects (lo que ya tenías)
        subjects = user.get("subjects", [])
        for sub in subjects:
            sub_id = str(sub.get("id"))
            if sub_id not in ids_visitados:
                ids_visitados.add(sub_id)
                
                lista_tutoria = [
                    sub_id,
                    sub.get("name", "Materia sin nombre"),
                    sub.get("topic", "General"),
                    "Sin fecha", # Los subjects no traen fecha en tu JSON
                    "4:00 PM"
                ]
                resultado.append(lista_tutoria)

        # 2. Procesar sentSuggestions (¡Aquí está la fecha real!)
        suggestions = user.get("sentSuggestions", [])
        for sug in suggestions:
            # Usamos el ID de la sugerencia para no duplicar
            sug_id = str(sug.get("id"))
            if sug_id not in ids_visitados:
                ids_visitados.add(sug_id)
                
                # Extraemos fecha y hora de "createdAt": "2026-01-05T15:00:00"
                full_date = sug.get("createdAt", "T--")
                fecha, hora = full_date.split("T") if "T" in full_date else (full_date, "12:00 PM")
                
                lista_tutoria = [
                    sug_id,
                    sug.get("subject", {}).get("name", "Materia sin nombre"),
                    sug.get("topic", "General"),
                    fecha, # Ejemplo: 2026-01-05
                    hora   # Ejemplo: 15:00:00
                ]
                resultado.append(lista_tutoria)
                
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