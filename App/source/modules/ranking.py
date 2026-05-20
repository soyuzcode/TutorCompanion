def get_featured_tutors(data):

    tutores = []

    if data is None:
        return

    for persona in data:

        # Verificar si es tutor
        if persona["tutorProfile"] != None:

            nombre = persona["name"]
            puntaje = persona["tutorProfile"]["rating"]

            tutor = {
                "name": nombre,
                "rating": puntaje
            }

            tutores.append(tutor)

    # Ordenar del mayor al menor puntaje
    tutores.sort(key=lambda x: x["rating"], reverse=True)

    tutores = tutores[:5]

    return tutores