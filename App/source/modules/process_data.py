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