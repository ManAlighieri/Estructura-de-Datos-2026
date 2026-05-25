from flask import Flask, render_template
import os
import subprocess
import sys

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def obtener_practicas():
    practicas = {}

    for carpeta in os.listdir(BASE_DIR):
        ruta = os.path.join(BASE_DIR, carpeta)

        if os.path.isdir(ruta) and carpeta.startswith("Practica_"):
            archivos = []

            for archivo in os.listdir(ruta):
                if archivo.endswith(".py"):
                    archivos.append(archivo)

            practicas[carpeta] = archivos

    return practicas


def leer_codigo(practica, archivo):
    ruta = os.path.join(BASE_DIR, practica, archivo)

    with open(ruta, "r", encoding="utf-8") as f:
        return f.read()


def ejecutar_codigo(practica, archivo):
    ruta = os.path.join(BASE_DIR, practica, archivo)

    try:
        resultado = subprocess.run(
            [sys.executable, ruta],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )

        return resultado.stdout if resultado.stdout else resultado.stderr

    except Exception as e:
        return str(e)


@app.route("/")
def inicio():
    practicas = obtener_practicas()
    return render_template("index.html", practicas=practicas)


@app.route("/practica/<practica>")
def ver_practica(practica):
    practicas = obtener_practicas()

    if practica not in practicas:
        return "Práctica no encontrada"

    return render_template(
        "practica.html",
        practica=practica,
        archivos=practicas[practica]
    )


@app.route("/codigo/<practica>/<archivo>")
def ver_codigo(practica, archivo):
    codigo = leer_codigo(practica, archivo)
    salida = ejecutar_codigo(practica, archivo)

    return render_template(
        "codigo.html",
        practica=practica,
        archivo=archivo,
        codigo=codigo,
        salida=salida
    )


if __name__ == "__main__":
    app.run(debug=True)