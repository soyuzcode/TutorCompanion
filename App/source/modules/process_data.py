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