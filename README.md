# Sistema web de gestión de tareas

Proyecto académico SENA para practicar el desarrollo de aplicaciones web con Django y la persistencia de información en una base de datos relacional.

## Funcionalidades verificadas en el código
- Listado de tareas.
- Creación de tareas mediante formularios.
- Eliminación de tareas.

## Tecnologías
Python, Django y SQLite.

## Estructura
- `manage.py`: administración del proyecto.
- `tareas/`: configuración principal.
- `todo/`: modelos, formularios, vistas, rutas y plantillas.
- `todo/migrations/`: migraciones de base de datos.

## Instalación local (Windows, Git Bash)
```bash
git clone https://github.com/AstharoXs/ProyectoDjango2.git
cd ProyectoDjango2
python -m venv .venv
source .venv/Scripts/activate
python -m pip install Django
python manage.py migrate
python manage.py runserver
```

Abre http://127.0.0.1:8000. Usa una copia local con datos ficticios. La versión exacta de Django queda pendiente de fijar en un archivo de dependencias.

## Estado
Proyecto académico. La edición de tareas no está implementada en las vistas revisadas. La instalación y las pruebas quedan pendientes de validación en un entorno limpio.
