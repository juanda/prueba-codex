# prueba-codex

Esta es una aplicación sencilla de gestión de tareas escrita con Flask.

## Requisitos

- Python 3.8 o superior
- Las dependencias listadas en `requirements.txt`

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

Ejecuta la aplicación con:

```bash
python app.py
```

La API estará disponible en `http://localhost:5000` con los siguientes endpoints:

- `GET /tasks` – lista todas las tareas.
- `POST /tasks` – crea una nueva tarea (JSON: `{ "title": "Nombre" }`).
- `PUT /tasks/<id>` – actualiza una tarea.
- `DELETE /tasks/<id>` – elimina una tarea.


## Docker

Puedes construir y ejecutar la aplicación dentro de un contenedor con Docker:

```bash
docker build -t prueba-codex .
docker run -p 5000:5000 prueba-codex
```

O bien, utilizando `docker-compose`:

```bash
docker compose up --build
```


