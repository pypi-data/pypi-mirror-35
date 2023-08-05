Supergato
=========

.. image:: https://github.com/categulario/supercat/blob/master/supercat/assets/game.png
   :alt: El juego de gato a otro nivel

Reglas
------

El juego del supergato se juega así:

* Gana el que gana el gato grande.
* Se gana el gato grande ganando los gatos chiquitos en alguna forma que represente un juego ganador en el tradicional gato.
* El primer jugador decide qué gato y casilla jugar.
* Cada jugador jugará el gato análogo en el gato grande a la casilla que jugó el jugador previo en su gato pequeño.
* Si a un jugador le corresponde jugar un gato que ya está terminado (ganado o empate) puede elegir qué gato jugar.

API para jugadores
------------------

Debes crear un módulo en python con una clase `Player` que herede de `supercat.utils.BasePlayer` y que tenga una función `play(world, game, move_num, last_move)`, dónde:

* `world` es el estado actual del juego (ver `definitinos/world.py`).
* `game` son las coordenadas (como tupla) del juego que el jugador debe jugar
  o `None` si es juego libre. Ejemplo: `(1, 2)`.
* `move_num` el número de jugada, comenzando con 1.
* `last_move` es la última jugada `juego, casilla` del oponente, si es la primera jugada del juego esto es `None, None`.

El valor de retorno de la función debe ser una 2-tupla de 2-tuplas que represente la jugada que va a jugar o `None, None` en caso de rendición, ejemplo: `(0, 0), (1, 1)`.

Adicionalmente la clase debe definir un atributo `name` con el nombre del jugador.

Se puede saber qué tipo de ficha (`X`, u `O`) se está jugando accediendo a la propiedad `self.identity` de la clase.

Puedes revisar (y usar) las cosas en `supercat.utils`, hay funciones ya definidas para varias cosas.

Cómo usar el referi
-------------------

Habiendo instalado pygame (ver [Cómo instalar pygame](https://www.youtube.com/watch?v=ZJ2XvYMr6tY)) usar al referi es muy sencillo. Abre una consola y navega hasta el repositorio, luego:

```bash
$ python referi --help # Un poco de ayuda
$ python referi lucky ordered -f 3 # Corre el referi, lucky contra depressed a 3 cuadros por segundo
```

El referi puede jugar con jugadores presentes en la carpeta `players`, se pueden repetir jugadores también, los nombres de los jugadores son el nombre del archivo sin la extensión, de modo que si tengo un jugador llamado `kysxd.py` en la carpeta players puedo jugarlo con:

```bash
$ python referi lucky kysxd
```

Por defecto los juegos son a 1 cuadro por segundo

Opciones de línea de comandos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


```
usage: referi [-h] [-f NUM] [-c] [-s] [-n] [-w SECONDS]
              PLAYER1 PLAYER2 PLAYER1 PLAYER2

Supercat referi

positional arguments:
  PLAYER1 PLAYER2       players to play

optional arguments:
  -h, --help            show this help message and exit
  -f NUM, --fps NUM     fps at with the game should play
  -c, --coin            should the referi flip a coin?
  -s, --capture-screen  take a screenshot of the final game
  -n, --no-render       Do not render the pygame GUI, just compute the game
  -w SECONDS, --wait SECONDS
                        wait before game disapears

lets play!
```

Changelog
---------

v1.2
~~~~

* Nuevos jugadores! `murder` le gana a ordered siempre, `meta` le gana a `murder`, `randomdrepressed` se cambió el nombre a `drunk`. `murder` y `meta` son contribuciones de @KYSXD.
* El tablero estaba traspuesto con respecto a las coordenadas que recibían los jugadores, ya no más.

v1.1
~~~~

* Se crean dos funciones `csv` y `err` en `supercat.utils` para separar `stdin` y `stderr` (esto puede ser útil para replay games).
* Se añadè `human` a los jugadores, ahora los humanos pueden jugar (kind of)...
* Se añade el jugador `randomdepressed` a los posibles jugadores.
* Corrección de bugs, refactorización, muerte, destrucción y cumbia.

v1.0
~~~~

* Ahora los jugadores son objetos en vez de sólo funciones, revisar `players/lucky.py` para más información
* Correcciones menores de bugs

v0.3
~~~~

* Se añade el módulo `supercat.utils` que todos los jugadores pueden usar, con funciones útiles como `boxes`, `random_boxes` y tests sobre el estado del juego
* Correcciones a `ordered`

v0.2
~~~~

* Se pueden guardar capturas de pantalla del final del juego usando la opción `-s` de la interfaz de línea de comandos
* El primer jugador siempre juega cuadros
* Para que el referi tire una moneda y decida quién tira primero se usa la opción `-c` (aun así el primer jugador juega cuadros)
* Ya se reconocen los empates (locales y general) y se marcan en el mundo con `"R"`
* El código de `lucky` y `ordered` está más limpio gracias a una función mágica

v0.1
~~~~

* Primera versión del referi, puede poner a competir dos IA y mostrar la partida
* permite regular los frames por segundo
