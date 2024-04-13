from flask import Flask, jsonify # type: ignore

telefono = "+524442975031"
mensaje = "HOLA TQM"
hora = "10"
minutos = "44"

app = Flask(__name__)
tasks = [
    {'telefono':telefono, 'mensaje':mensaje, 'hora': hora, 'minutos':minutos}

]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)
