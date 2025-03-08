# GAMES API
This is an example of a games api build in fastapi by Eric G.

## To do
- Actualizar el readme
    - Sección de instalación (uv sync, activate) [Explicar como instalarlo]
    - Sección de lanzar el proyecto [Comando de Uvicorn]
    - Sección de descripción del proyecto [Listar los endpoints y una frase explicativa (ponerlo como sale abajo en endpoints a implementar)] 

- Endpoints a implementar
    - `/games/genres` -> Devuelve todos los generos distintos como una lista
    - `/games/publisher` -> Devuelve todos los publisher distintos como una lista
    - `/games/platform` -> Devuelve todos las plataformas distintas como una lista
    - `/games/year` -> Devuelve todos los años distintos como una lista
    - `/games/publisher/{publisher}` -> Devuelve los 100 primeros juegos de ese publisher
    - `/games/platform/{platform}` -> Devuelve los 100 primeros juegos de ese platform
    - `/games/genres/{genres}` -> Devuelve los 100 primeros juegos de ese genres
    - `/games/year/{year}` -> Devuelve los 100 primeros juegos de ese year
    - `/games/year/{year_1}/{year_2}`-> Devuelve los 100 primeros juegos entre el año 1 y año 2
    - `/games/eusales/{eusales_1}/{eusales_2}`-> Devuelve los 100 primeros juegos entre el eusales_1 y eusales_2
    `/games/eusales/{nasales_1}/{nasales_2}`-> Devuelve los 100 primeros juegos entre el nasales_1 y nasales_2
