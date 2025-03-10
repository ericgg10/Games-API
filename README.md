# GAMES API
This is an example of a games api build in fastapi by Eric G.

## Instalación
 Uv es un gestor de paquetes extremadamente rápido para Python que nos servirá para limitar los paquetes que instalemos en nuestros proyectos. De este modo no tendremos que tener instalados todos los paquetes en los diferentes espacios de trabajo sino que tendremos instalados en cada espacio de trabajo los paquetes necesarios para poder trabajar

### Instrucciones de instalación: 
 - Ejecutamos el terminal el CMD en Python y para instalarlo usaremos el comando:

    - Windows: powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    
    - Mac o Linux: curl -LsSf https://astral.sh/uv/install.sh | sh

### Comandos:
`uv sync`: Nos servirá para sincronizar las dependencias del proyecto con el entorno.

`uv add`: Agregamos una dependencia al proyecto.

`uv remove`: Eliminamos una dependencia del proyecto.

`uv tree`: Ver el arbol de dependencias del proyecto.



### Activar el entorno virtual:
`.venv/bin/activate`: Con este comando activaremos el entorno virtual donde se instalaran los paquetes y ejecuciones de Python.


## Ejecucción

`uvicorn src.main:app --reload`: Para lanzar el proyecto usaremos este comando

## Descripción del proyecto
- `/` Devuelve el mensaje de Hello Eric cuando accedamos a la ruta y nos servirá para comprobar que funciona correctamente la conexión con el servidor
- `/games/id/{id}` Devuelve los datos del juego con el ID que le hayamos pasado
- `/games/name/{name}` Devuelve todos los datos del juego con el nombre que le hayamos pasado
- `/games/genre/{genre}` Devuelve todos los juegos con el genero que le hayamos pasado








## To do
- Actualizar el readme
    - ~~Sección de instalación (uv sync, activate) [Explicar como instalarlo]~~
    - ~~Sección de lanzar el proyecto [Comando de Uvicorn]~~
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
