from flask import Flask, render_template, request
import mysql.connector

"""# Establecer la conexión con la base de datos
cnx = mysql.connector.connect(user='usuario', password='contraseña' , host='http://localhost/phpmyadmin/', database='nombre_de_la_base_de_datos')

# Crear un objeto cursor para ejecutar las consultas
cursor = cnx.cursor()

# Ejecutar una consulta SELECT
query = ("SELECT columna1, columna2, columna3, columna4, columna5 FROM tabla")
cursor.execute(query)

# Recorrer los resultados de la consulta
for (columna1, columna2, columna3, columna4, columna5) in cursor:
    print("{} {} {} {} {}".format(columna1, columna2, columna3, columna4, columna5))

# Cerrar el cursor y la conexión
cursor.close()
cnx.close()"""


app = Flask(__name__)

def validarLogin(user, passw):
    usuario = 'adm'
    password = '12345'

    if(user == usuario and passw == password):
        return True
    else:
        return False

@app.route('/')
def index():
    return render_template('home.html')
    

@app.route('/ingresar', methods=['post'])
def productosingresar():
    
    nombre = request.form['nombre']
    print(nombre)

    cantidad = request.form['cantidad']
    print(cantidad)
    
    procedencia = request.form['procedencia']
    print(procedencia)
    
    codigo = request.form['codigo']
    print(codigo)
    
    lote = request.form['lote']
    print(lote)

    return render_template('listaInventario.html')


@app.route('/consulta', methods=['post'])
def consulta():

    
    return request.form['cantidad']


@app.route('/login', methods=['post'])
def home():
    
    usuario = request.form['usuario']
    
    contrasena = request.form['contrasena']
    
    logueado = validarLogin(usuario, contrasena)
    
    if(logueado ==True):
        print('si')
        return render_template('listaInventario.html')
    else:
        print('no')
        return render_template('home.html')

    
if __name__ == '__main__':
    app.run(debug=True)
    
    

    
