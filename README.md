Juego de Preguntas 🎮

Una trivia rápida y entretenida en Python(usando libreria de Pygame)  + estadísticas + BDD relacional(SQLITE).

¿De qué se trata?

Este proyecto propone un juego de preguntas (tipo quiz/trivia) donde:

Las preguntas están definidas en un archivo JSON (preguntas_juego.json).

Se almacenan estadísticas de las preguntas hechas en tabla estadisticas.

Se guarda un ranking en tabla ranking.

Hay recursos gráficos en la carpeta Game_assets.


Contenido del repo

Game_assets/ → Imágenes, gráficos, lo visual para el juego.

JuegoPreguntados/ → Parte web o front‑end del juego (HTML, JS, CSS probablemente).

.gitignore → Archivos ignorados por Git.

preguntas_juego.json → Banco de preguntas + alternativas.

estadisticas_preguntas.csv → Registro de cuántas veces se hizo cada pregunta, aciertos, etc.

ranking.csv → Puntuaciones o posiciones de jugadores.

¿Cómo funciona la lógica básica?

El sistema carga las preguntas desde preguntas_juego.json.

Muestra al jugador una pregunta con alternativas, espera su elección.

Si es correcta → registra el acierto; si no → lo marca como error.

Actualiza estadísticas en estadisticas_preguntas.csv.

Si corresponde, actualiza ranking.csv con la puntuación del jugador.

Al finalizar, el jugador puede ver sus resultados, posición en el ranking, etc.

Para arrancar

Cloná el repo:

git clone https://github.com/LautaroMoro/Juego_de_preguntas.git  


Asegurate de que tenés Python 3.11 instalado.

Jugá y divertite. Cada vez que respondás, las estadísticas y el ranking se actualizan.

¿Por qué lo hice?

Porque me parecía divertido juntar: programación en Python,  manejo de base de datos relacional(SQLITE). Una buena práctica para programar + aprendizaje + diversión.

Ideas para mejorar

Añadir más preguntas / categorías / niveles de dificultad.

Crear tabla jugadores y preguntas

Mejores gráficos, animaciones.

Exportar ranking a un servidor o base de datos remota.

Licencia

Pueden usarlo libremente (open source friendly).
