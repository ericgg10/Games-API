# GAMES API
This is an example of a games api build in fastapi by Eric G.

## Installation
Uv is an extremely fast package manager for Python that will help us limit the packages we install in our projects. This way, we won't have to install all the packages in different workspaces, but instead, we'll install the necessary packages for each workspace to be able to work.

### Installation Instructions:: 
 - Open the terminal or CMD in Python, and to install it, use the following command:

    - Windows: powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    
    - Mac o Linux: curl -LsSf https://astral.sh/uv/install.sh | sh

### Commands:
`uv sync`: This will synchronize the project's dependencies with the environment.

`uv add`: Add a dependency to the project.

`uv remove`: Remove a dependency from the project.

`uv tree`: View the project's dependency tree.



### Activate the virtual environment:
`.venv/bin/activate`: This command will activate the virtual environment where the packages and Python executions will be installed.


## Execution

`uvicorn src.main:app --reload`: To launch the project, we will use this command.

## Descripción del proyecto
- `/` Returns the message "Hello Eric" when we access the route and will help verify that the connection with the server is working correctly.
- `/games/id/{id}` Returns the data of the game with the ID we provide.
- `/games/name/{name}` Returns all the data of the game with the name we provide.
- `/games/genre/{genre}` Returns all games with the genre we provide.
- `/games/genres` Returns all distinct genres of games as a list.
- `/games/publisher` Returns all distinct publishers of games as a list.
- `/games/platform` Returns all distinct platforms of games as a list.
- `/games/year` Returns all distinct years of games as a list.
- `/games/publisher/{publisher}` Returns the first 100 games from the publisher we provide.
- `/games/platform/{platform}` Returns the first 100 games from the platform we provide.
- `/games/genre/{genre}` Returns the first 100 games from the genre we provide.
- `/games/year/{year}` Returns the first 100 games from the year we provide.
- `/games/year/{year_1}/{year_2}` Returns the first 100 games between the two years we provide.
- `/games/eu_sales/{eu_sales_1}/{eu_sales_2}` Returns the first 100 games between the EU sales range we provide.
- `/games/na_sales/{na_sales_1}/{na_sales_2}` Returns the first 100 games between the NA sales range we provide.

## To do

