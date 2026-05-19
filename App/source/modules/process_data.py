"""Here we're gonna process every data when we need on ui"""

def validar_correo(texto):
    if texto.endswith("@keyinstitute.edu.sv"):
        if " " not in texto:
            return True
    return False


# Asignado: Michelle
def obtener_todas_las_tutorias(data: list | dict | None) -> list[list[str]]:
    """
    Dado el diccionario o lista de datos de Data/return_example.json,
    recorre los usuarios, extrae TODAS las tutorías existentes en sus 'subjects'
    e información disponible, evitando duplicarlas.
    
    Retorna una lista de listas lista para la UI:
        [
            [ID, MATERIA, TEMA, FECHA, HORA],
            ...
        ]
    """
    if data is None:
        return []

    resultado = []
    ids_visitados = set()

    for user in data:
        subjects = user.get("subjects", [])
        for sub in subjects:
            sub_id = str(sub.get("id"))
            
            # Si la tutoría no la hemos procesado ya, la agregamos
            if sub_id not in ids_visitados:
                ids_visitados.add(sub_id)
                
                # Extraemos los datos básicos. Si falta alguno, ponemos un valor por defecto
                lista_tutoria = [
                    sub_id,                                # ID
                    sub.get("name", "Materia sin nombre"), # Nombre de la materia
                    sub.get("topic", "General"),           # Tema / Tópico
                    sub.get("date", "XX/XX/2026"),         # Fecha
                    sub.get("hour", "4:00 PM")             # Hora
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