import sqlite3
import os
from typing import Dict, List, Tuple, Any

RUTA_DB = os.path.join(os.path.dirname(__file__), "juego_preguntados.db")

def crear_tablas():
    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS estadisticas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pregunta TEXT NOT NULL,
    veces_preguntada INTEGER DEFAULT 0,
    aciertos INTEGER DEFAULT 0,
    errores INTEGER DEFAULT 0,
    porcentaje_aciertos REAL DEFAULT 0
    )
    """)
    

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ranking(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    puntuacion INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    duracion TEXT)
    """)
    
    conexion.commit()
    conexion.close()

def guardar_ranking_bdd(nombre: str, puntuacion: int, fecha: str = None, duracion_partida:str = None):
    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()
    """Inserta una fila en la tabla ranking """
    if fecha is None:
        fecha = datetime.datetime.now().strftime('%Y-%m-d %H:%M:%S')
    cursor.execute("""
    INSERT INTO ranking (nombre, puntuacion, fecha, duracion)
    VALUES(?, ?, ?, ?)
    """, (nombre, puntuacion, fecha, duracion_partida))
    conexion.commit()
    conexion.close()

def obtener_top10_bdd() -> List[Tuple[str, int, str, str]]:
    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()
    """Devuelve el top 10 del ranking ordenado por puntaje desc."""
    cursor.execute("""
    SELECT nombre, puntuacion, fecha, duracion
    FROM ranking
    ORDER BY puntuacion DESC
    """)
    filas = cursor.fetchall()
    conexion.commit()
    conexion.close()
    return filas



#-------------------------------------------FUNCIONES  DE ESTADISTICAS----------------------------------------------------------------
def insertar_o_actualizar_estadisticas(pregunta:str, veces_preguntada:int, aciertos:int, errores:int, porcentaje_aciertos: float):
    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()
    """Inserta una nueva fila de estadisticas para las preguntas"""
    cursor.execute("""
    DELETE FROM estadisticas WHERE pregunta = ?
    """, (pregunta,))

    cursor.execute("""
    INSERT INTO estadisticas(pregunta, veces_preguntada, aciertos, errores, porcentaje_aciertos)
    VALUES(?, ?, ?, ?, ?)
    """, (pregunta, veces_preguntada, aciertos, errores, porcentaje_aciertos))
    conexion.commit()
    conexion.close()

def guardar_estadisticas_preguntas_bdd(estadisticas_preguntas):
    for pregunta, estadisticas in estadisticas_preguntas.items():
            if estadisticas["total_preguntas"] > 0:
                porcentaje_aciertos = (estadisticas["respuestas_correctas"] / estadisticas["total_preguntas"]) * 100
            else:
                porcentaje_aciertos = 0.0
            insertar_o_actualizar_estadisticas(
                pregunta,
                estadisticas["total_preguntas"],
                estadisticas["respuestas_correctas"],
                estadisticas["respuestas_incorrectas"],
                porcentaje_aciertos
            )








