"""Here we're gonna process every data when we need on ui"""
def validar_correo(texto):

    if texto.endswith("@keyinstitute.edu.sv"):

        if " " not in texto:
            return True

    return False

correo = input("Ingresa tu correo: ")
print(validar_correo(correo))


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
data = []
id = int(input("Ingrese id: "))
name = input("Ingrese nombre: ")
topic = input("Ingrese tema: ")
date = input("Ingrese fecha: ")
hour = input("Ingrese hora: ")
nuevo = {
    "id": id,
    "name": name,
    "topic": topic,
    "date": date,
    "hour": hour
}
data.append(nuevo)
print(convertir_lista(data))

def is_psk_and_username_valid(user:str, psk:str) -> bool:

    datos = [
        ["Miguel", "miguel@keyinstitute.edu.sv", "KEY123", "1234"],
        ["Carlos", "carlos@keyinstitute.edu.sv", "KEY456", "abcd"],
        ["Ana", "ana@keyinstitute.edu.sv", "KEY789", "4321"]
    ]

    for persona in datos:

        nombre = persona[0]
        email = persona[1]
        keycode = persona[2]
        password = persona[3]

        if user == nombre or user == email or user == keycode:

            if psk == password:
                return True

    return False


usuario = input("Ingresa nombre, correo o keycode: ")
clave = input("Ingresa password: ")

resultado = is_psk_and_username_valid(usuario, clave)

print(resultado)