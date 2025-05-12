from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/ejercicio1", methods=["GET", "POST"])
def ej1():
    promedio = None
    estado = None

    if request.method == "POST":
        try:
            nota1 = float(request.form.get("nota1", 0))
            nota2 = float(request.form.get("nota2", 0))
            nota3 = float(request.form.get("nota3", 0))
            asistencia = float(request.form.get("asistencia", 0))

            if not (10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70 and 0 <= asistencia <= 100):
                return "Error: Los valores deben estar dentro del rango permitido.", 400

            promedio = (nota1 + nota2 + nota3) / 3
            estado = "Aprobado ✅" if promedio >= 40 and asistencia >= 75 else "Reprobado ❌"
        except ValueError:
            estado = "Error: Datos inválidos."

    return render_template("Ejercicio_1.html", promedio=promedio, estado=estado)


@app.route('/ejercicio2', methods=["GET", "POST"])
def ej2():
    nombre_largo = None
    largo = None
    if request.method == "POST":
        try:
            nombre1 = request.form.get("nombre1", "")
            nombre2 = request.form.get("nombre2", "")
            nombre3 = request.form.get("nombre3", "")

            nombres = [nombre1, nombre2, nombre3]
            nombre_largo = max(nombres, key=len)
            largo = len(nombre_largo)

        except Exception as e:
            nombre_largo = "Error al procesar los datos."
            largo = None

    return render_template('Ejercicio_2.html', nombre_largo=nombre_largo, largo=largo)


if __name__ == '__main__':
    app.run()
