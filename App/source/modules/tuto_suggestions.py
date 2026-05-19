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
