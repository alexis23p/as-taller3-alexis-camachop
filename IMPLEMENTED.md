Estado: Scaffold implementado

Se implementó un scaffold mínimo para acelerar el desarrollo del proyecto. Cambios principales:

- `api/`:
  - `main.py`: instancia FastAPI y endpoints básicos (`/health`, `/users/register`, `/products`, `/cart/{user_id}/add`).
  - `database.py`: configuración de SQLAlchemy (lee `DATABASE_URL`).
  - `models.py`, `schemas.py`, `crud.py`: modelos, esquemas Pydantic y operaciones CRUD básicas.

- `webapp/`:
  - `app.py`: pequeña app Flask que consulta `API_URL` y muestra productos.
  - `templates/index.html`, `static/style.css`.

- `proxy/nginx.conf`: configuración mínima para enrutar a `api` y `webapp`.
- `database/init.sql`: placeholder de inicialización.

Instrucciones rápidas para pruebas locales (sin Docker):

1. Crear y activar un virtualenv en la carpeta `api` e instalar `api/requirements.txt`.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r api/requirements.txt
uvicorn api.main:app --reload
```

2. En otra terminal, crear/activar virtualenv en `webapp` e instalar `webapp/requirements.txt`.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r webapp/requirements.txt
python webapp/app.py
```

3. Abrir `http://localhost:5000` para ver el frontend (consumirá la API en `http://localhost:8000`).

Notas:
- Este cambio resuelve muchos de los `TODO` documentales creando un scaffold funcional; quedan pendientes mejoras de seguridad, autenticación completa, manejo de sesiones y despliegue con base de datos en contenedor.
