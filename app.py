import os
import urllib.parse
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Cargar las variables del archivo .env
load_dotenv()

app = Flask(__name__)

# ==========================================
# 1. CONFIGURACIÓN DE LA BASE DE DATOS (.env)
# ==========================================
# Obtenemos las variables y usamos .replace() por si accidentalmente dejaste llaves en el .env
db_driver = os.getenv('DB_DRIVER', 'ODBC Driver 17 for SQL Server').replace('{', '').replace('}', '')
db_server = os.getenv('DB_SERVER', 'DESKTOP-KJ433A4')
db_database = os.getenv('DB_DATABASE', 'PW_BIBLIOTECA')
db_trusted = os.getenv('DB_TRUSTED_CONNECTION', 'yes')

# Armamos la cadena. Las tres llaves {{{ }}} son correctas en Python: 
# Las externas se convierten en una llave literal { } para SQL, y la interna inyecta la variable.
string_conexion = f"DRIVER={{{db_driver}}};SERVER={db_server};DATABASE={db_database};Trusted_Connection={db_trusted};"

# Imprimimos la cadena en la consola para depurar (luego puedes borrar esta línea)
print("\n--- INTENTANDO CONECTAR CON ---")
print(string_conexion)
print("-------------------------------\n")

params_conexion = urllib.parse.quote_plus(string_conexion)
CADENA_CONEXION = f"mssql+pyodbc:///?odbc_connect={params_conexion}"

app.config['SQLALCHEMY_DATABASE_URI'] = CADENA_CONEXION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializamos la base de datos
db = SQLAlchemy(app)


# ==========================================
# 2. MODELOS DE BASE DE DATOS (Tablas)
# ==========================================
class Categoria(db.Model):
    __tablename__ = 'Categorias_Libro'
    ID_Categoria = db.Column(db.Integer, primary_key=True)
    Nombre_Categoria = db.Column(db.String(100), nullable=False)
    libros = db.relationship('Libro', backref='categoria', lazy=True)

class Libro(db.Model):
    __tablename__ = 'Libros'
    ID_Libro = db.Column(db.Integer, primary_key=True)
    Titulo = db.Column(db.String(200), nullable=False)
    Autor = db.Column(db.String(150))
    ISBN = db.Column(db.String(20), unique=True)
    ID_Categoria = db.Column(db.Integer, db.ForeignKey('Categorias_Libro.ID_Categoria'))
    Anio_Edicion = db.Column(db.Integer)
    Sinopsis = db.Column(db.Text)
    Portada_URL = db.Column(db.String(255))
    Ubicacion_Fisica = db.Column(db.String(100))
    Copias_Totales = db.Column(db.Integer, default=0)
    Copias_Disponibles = db.Column(db.Integer, default=0)

class Publicacion(db.Model):
    __tablename__ = 'Publicaciones'
    ID_Publicacion = db.Column(db.Integer, primary_key=True)
    Titulo = db.Column(db.String(200), nullable=False)
    Tipo_Publicacion = db.Column(db.String(50), nullable=False) 
    Contenido = db.Column(db.Text, nullable=False)
    Imagen_Portada_URL = db.Column(db.String(255))
    Fecha_Publicacion = db.Column(db.DateTime, default=datetime.utcnow)

class Video(db.Model):
    __tablename__ = 'Videos'
    ID_Video = db.Column(db.Integer, primary_key=True)
    Titulo = db.Column(db.String(200), nullable=False)
    Categoria_Video = db.Column(db.String(100))
    URL_Video = db.Column(db.String(255), nullable=False)
    Miniatura_URL = db.Column(db.String(255))
    Duracion = db.Column(db.String(10))

# ==========================================
# 3. RUTAS DE LA APLICACIÓN
# ==========================================
@app.route("/")
def index():
    # 1. Obtener la publicación más reciente para el cuadro principal
    publicacion_principal = Publicacion.query.order_by(Publicacion.Fecha_Publicacion.desc()).first()

    # 2. Obtener las siguientes 3 publicaciones (saltamos la primera con offset(1))
    otras_publicaciones = []
    if publicacion_principal:
        otras_publicaciones = Publicacion.query.order_by(Publicacion.Fecha_Publicacion.desc()).offset(1).limit(3).all()

    return render_template("index.html", principal=publicacion_principal, noticias=otras_publicaciones)

@app.route("/catalogo.html")
def catalogo():
    return render_template("catalogo.html")

@app.route("/videoteca.html")
def videoteca():
    return render_template("videoteca.html")

@app.route("/nosotros.html")
def nosotros():
    return render_template("nosotros.html")

@app.route("/servicios.html")
def servicios():
    return render_template("servicios.html")

@app.route("/reglamento.html")
def reglamento():
    return render_template("reglamento.html")

@app.route("/admin-dashboard.html")
def admin_dashboard():
    return render_template("admin-dashboard.html")

@app.route("/admin-libros.html")
def admin_libros():
    return render_template("admin-libros.html")

@app.route("/admin-login.html")
def admin_login():
    return render_template("admin-login.html")

@app.route("/libro-detalle.html")
def libro_detalle():
    return render_template("libro-detalle.html")

if __name__ == "__main__":
    # Crea las tablas si no existen en la base de datos PW_BIBLIOTECA
    with app.app_context():
        db.create_all()
        
    app.run(debug=True, port=8000)