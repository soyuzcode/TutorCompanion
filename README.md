# TutorCompanion

Plataforma de tutorías para el Key Institute: estudiantes solicitan sesiones, tutores las gestionan y el sistema muestra rankings, horas de impacto y calificaciones.

## Arquitectura

| Capa | Tecnología | Ubicación |
|------|------------|-----------|
| Cliente | Python 3 + Kivy / KivyMD | `App/` |
| API | Spring Boot 4 + JPA | `Server/TutorCompanion/` |
| Config / respaldo | JSON local | `App/Data/` |

## Requisitos

- Python 3.10+
- Java 25
- Maven (incluido `mvnw` en el servidor)

## Configuración

1. Edita la URL base en `App/Data/settings.json`:

```json
{
  "BASE_URL": "https://tutorcompanionv1.onrender.com/"
}
```

2. Instala dependencias del cliente:

```bash
cd App
pip install -r requirements.txt
```

3. (Opcional) Arranca el servidor en local:

```bash
cd Server/TutorCompanion
./mvnw spring-boot:run
```

## Ejecutar la app

```bash
cd App/source
python main.py
```

Si la API no responde, la app usa `App/Data/return_example.json` como respaldo.

## Endpoints de la API

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/user` | Usuarios con perfiles, reviews y sesiones |
| GET | `/suggestions` | Solicitudes de tutoría |
| POST | `/suggestions` | Crear solicitud |
| GET | `/reviews?tutorId={id}` | Reviews de un tutor |
| POST | `/reviews` | Calificar a un tutor |

### Ejemplo: crear review

```json
POST /reviews
{
  "tutorId": 10,
  "studentId": 1,
  "rating": 5,
  "comment": "Excelente sesión"
}
```

## Funcionalidades

- Login con nombre, correo `@keyinstitute.edu.sv` o código `KEY_XXXXXX`
- Dashboard: ranking de tutores, horas aprobadas, tutorías y solicitudes
- Sugerir tutoría (materia + tutor)
- **Rating Tutor**: calificar tutores con estrellas y comentario

## Credenciales de prueba

Usuarios de ejemplo en `Server/TutorCompanion/src/main/resources/data.sql`. La contraseña de demo coincide con el hash almacenado (`ab0ec5a139100e2f51ac08360c79a452`).

Ejemplos:

- `einstein@keyinstitute.edu.sv`
- `KEY_000001` (Karl Marx)

## Estructura del repositorio

```
TutorCompanion/
├── App/
│   ├── Data/           # settings.json, return_example.json
│   ├── requirements.txt
│   └── source/
│       ├── main.py
│       ├── ui.py
│       ├── ui/         # pantallas .kv
│       └── modules/    # API, procesamiento de datos
└── Server/
    └── TutorCompanion/   # Spring Boot
```

## Estado del proyecto

Versión alpha. Algunas acciones del dashboard (búsqueda de tutorías, historial) siguen en desarrollo.
