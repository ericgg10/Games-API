# GAMES API
Este es un ejemplo de una API de juegos construida con fastapi por Eric G.

## Instalación
 Uv es un gestor de paquetes extremadamente rápido para Python que nos servirá para limitar los paquetes que instalemos en nuestros proyectos. De este modo no tendremos que tener instalados todos los paquetes en los diferentes espacios de trabajo sino que tendremos instalados en cada espacio de trabajo los paquetes necesarios para poder trabajar.

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

`uvicorn src.main:app --reload`: Para lanzar el proyecto usaremos este comando.

## Descripción del proyecto
- `/` Devuelve el mensaje de Hello Eric cuando accedamos a la ruta y nos servirá para comprobar que funciona correctamente la conexión con el servidor.
- `/games/id/{id}` Devuelve los datos del juego con el ID que le hayamos pasado.
- `/games/name/{name}` Devuelve todos los datos del juego con el nombre que le hayamos pasado.
- `/games/genre/{genre}` Devuelve todos los juegos con el genero que le hayamos pasado.
- `/games/genres` Devuelve todos los generos distintos de los juegos como una lista.
- `/games/publisher` Devuelve todos los publisher distintos de los juegos como una lista.
- `/games/platform` Devuelve todas las plataformas distintas de los juegos como una lista.
- `/games/year` Devuelve todos los años distintos de los juegos como una lista.
- `/games/publisher/{publisher}` Devuelve los 100 primeros juegos del publisher que le hayamos pasado.
- `/games/platform/{platform}` Devuelve los 100 primeros juegos de la plataforma que le hayamos pasado.
- `/games/genre/{genre}` Devuelve los 100 primeros juegos del genero que le hayamos pasado.
- `/games/year/{year}` Devuelve los 100 primeros juegos del año que le hayamos pasado.
- `/games/year/{year_1}/{year_2}` Devuelve los 100 primeros juegos entre el año 1 y el año 2 que le hayamos pasado.
- `/games/eu_sales/{eu_sales_1}/{eu_sales_2}` Devuelve los 100 primeros juegos entre las eu_sales_1 y las eu_sales_2.
- `/games/na_sales/{na_sales_1}/{na_sales_2}` Devuelve los 100 primeros juegos entre las na_sales_1 y las na_sales_2.

## To do
-  Abstraer la lógica de las funciones de get games by
-  Abstraer la lógica de las funciones de get games between
-  Realizar pruebas y devolver el error conveniente. Nunca puede devolver un 500
-  Cuando abstraiga la lógica de las funciones hacer un test para ese grupo de endpoints en distintos archivos los grupos y para cada una de las funciones