from flask import Flask, render_template, jsonify
import os
import subprocess
import sys

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def obtener_practicas():
    practicas = {}
    for carpeta in sorted(os.listdir(BASE_DIR)):
        ruta = os.path.join(BASE_DIR, carpeta)
        if os.path.isdir(ruta) and carpeta.startswith("Practica"):
            archivos = sorted([f for f in os.listdir(ruta) if f.endswith(".py")])
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
            encoding="utf-8",
            timeout=10,
            cwd=os.path.join(BASE_DIR, practica)
        )
        return {
            "stdout": resultado.stdout,
            "stderr": resultado.stderr,
            "returncode": resultado.returncode
        }
    except subprocess.TimeoutExpired:
        return {"stdout": "", "stderr": "Tiempo límite excedido (30s)", "returncode": 1}
    except Exception as e:
        return {"stdout": "", "stderr": str(e), "returncode": 1}

@app.route("/")
def inicio():
    practicas = obtener_practicas()
    return render_template("index.html", practicas=practicas)

@app.route("/practica/<practica>")
def ver_practica(practica):
    ruta = os.path.join(BASE_DIR, practica)
    if not os.path.exists(ruta):
        return "Práctica no encontrada", 404
    archivos = sorted([f for f in os.listdir(ruta) if f.endswith(".py")])
    return render_template("practica.html", nombre=practica, archivos=archivos)

@app.route("/practica/<practica>/<archivo>")
def ver_archivo(practica, archivo):
    codigo = leer_codigo(practica, archivo)
    resultado = ejecutar_codigo(practica, archivo)
    salida = resultado["stdout"]
    errores = resultado["stderr"]
    return render_template("archivo.html",
        practica=practica,
        archivo=archivo,
        codigo=codigo,
        salida=salida,
        errores=errores
    )

@app.route("/api/ejecutar/<practica>/<archivo>")
def api_ejecutar(practica, archivo):
    resultado = ejecutar_codigo(practica, archivo)
    return jsonify(resultado)

if __name__ == "__main__":
    app.run(debug=True)
