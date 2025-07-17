from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

# Conexión a la base de datos
conn = psycopg2.connect(
    dbname="Basededatos",
    user="postgres",
    password="1234567",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    nombre = request.form['nombre']
    correo = request.form['correo']
    cur.execute("INSERT INTO usuarios (nombre, correo) VALUES (%s, %s)", (nombre, correo))
    conn.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
