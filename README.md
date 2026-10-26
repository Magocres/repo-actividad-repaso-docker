# repaso fundamentos

Aplicación en Python que se conecta a una base de datos PostgreSQL, crea una tabla `characters` con personajes de Rick y Morty, inserta datos y comprueba el resultado. Todo se levanta con Docker Compose.

## Integrantes y reparto del trabajo

| Integrante        | Trabajo realizado                                              |
|-------------------|----------------------------------------------------------------|
| Mario González    | `compose.yaml`, `Dockerfile` y `.env`                          |
| Manolo Tortajada  | Queries de inserción (`INSERT`) y de recuento (`COUNT`)        |
| Pablo Cunat       | Queries de creación de la tabla (`CREATE TABLE`) y del `SELECT` |
| Ignacio Pinazo    | `main.py`                                                      |

## Estructura

```
proyecto/
├── main.py            # conexión a la BD, creación, inserción y comprobación
├── tabla.sql          # CREATE TABLE de la tabla characters
├── insertarDatos.sql  # INSERT de los 10 personajes
├── Dockerfile         # imagen de la aplicación (python:3.12-slim)
├── compose.yaml       # servicios: db (postgres:17-alpine) y app
├── .env               # variables de entorno (usuario, contraseña, BD, DATABASE_URL)
└── requirements.txt   # psycopg[binary]
```

## Pasos de ejecución

1. Clonar el repositorio y entrar en la carpeta del proyecto:

   ```bash
   git clone https://github.com/Magocres/repo-actividad-repaso-docker.git
   cd repo-actividad-repaso-docker/proyecto
   ```

2. Construir las imágenes y levantar los contenedores:

   ```bash
   docker compose up --build
   ```

   Esto arranca el contenedor `db` (PostgreSQL) y el contenedor `app`, que ejecuta `main.py` y termina al acabar.

3. Para parar y borrar los contenedores:

   ```bash
   docker compose down
   ```

   Si además se quiere borrar los datos guardados (volumen `postgresDB`), por ejemplo tras cambiar las variables `POSTGRES_*` del `.env`:

   ```bash
   docker compose down -v
   ```

## Qué hace `main.py`

1. Se conecta a PostgreSQL usando `DATABASE_URL` y muestra la versión del servidor.
2. Crea la tabla `characters` si no existe (`CREATE TABLE IF NOT EXISTS`).
3. Inserta 10 personajes (`ON CONFLICT (id) DO NOTHING`, así se puede ejecutar varias veces) y muestra cuáles se han insertado.
4. Hace un `SELECT` de `id`, `name` y `species` de los 10 primeros personajes ordenados por `id`, y los muestra.
5. Muestra el número total de personajes guardados.

## Resultado por pantalla

En la primera ejecución, con la tabla vacía, `app` muestra:

```
¡Conexión establecida con éxito a PostgreSQL!
Versión del servidor: PostgreSQL 17.x on ...
Inserciones realizadas: 10
  - id=1, name=Rick Sanchez
  - id=2, name=Morty Smith
  - id=3, name=Summer Smith
  - id=4, name=Beth Smith
  - id=5, name=Jerry Smith
  - id=6, name=Abadango Cluster Princess
  - id=7, name=Abradolf Lincler
  - id=8, name=Adjudicator Rick
  - id=9, name=Agency Director
  - id=10, name=Alan Rails
Primeros 10 personajes:
  - id=1, name=Rick Sanchez, species=Human
  - id=2, name=Morty Smith, species=Human
  - id=3, name=Summer Smith, species=Human
  - id=4, name=Beth Smith, species=Human
  - id=5, name=Jerry Smith, species=Human
  - id=6, name=Abadango Cluster Princess, species=Alien
  - id=7, name=Abradolf Lincler, species=Human
  - id=8, name=Adjudicator Rick, species=Human
  - id=9, name=Agency Director, species=Human
  - id=10, name=Alan Rails, species=Human
Total de personajes guardados: 10
```

Si se vuelve a ejecutar sin borrar el volumen, los personajes ya existen y se omiten: aparece `Inserciones realizadas: 0`, pero el `SELECT` y el total siguen mostrando los 10 personajes.
