"""Here we're gonna process every data when we need on ui"""
def validar_correo(texto):

    if texto.endswith("@keyinstitute.edu.sv"):

        if " " not in texto:
            return True

    return False

def convertir_lista(diccionarios):
    resultado = []
    for elemento in diccionarios:
        lista = []
        lista.append(elemento["id"])
        lista.append(elemento["name"])
        lista.append(elemento["topic"])
        lista.append(elemento["date"])
        lista.append(elemento["hour"])
        resultado.append(lista)
    return resultado

# Asignado: Cristina
def process_data_from_user_dict(data:dict):
    """Dado un diccionario (llamado data) de la forma escrita en Data/return_example.json
        Retorne una lista de listas asi:
            [
                [NOMBRE1, EMAIL1, KEYCODE1, PASSWORD1],
                [NOMBRE2, EMAIL2, KEYCODE2, PASSWORD2],
                [NOMBRE3, EMAIL3, KEYCODE3, PASSWORD3]
            ]
            
        Con todos los nombres, emails, key codes y passwords en el diccionario."""

    result: list[list[str]] = []

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