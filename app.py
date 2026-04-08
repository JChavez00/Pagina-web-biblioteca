import os
import urllib.parse
import pandas as pd  # <--- NUEVA IMPORTACIÓN
import uuid  # <--- AGREGA ESTO
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect # <--- AGREGAR request y redirect
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
#print("\n--- INTENTANDO CONECTAR CON ---")
#print(string_conexion)
#print("-------------------------------\n")

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
    Titulo = db.Column(db.Text, nullable=False)
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
    Tipo_Publicacion = db.Column(db.String(50), nullable=False) # Ej: 'Noticia', 'Evento', 'Aviso'
    Contenido = db.Column(db.Text, nullable=False)
    Imagen_Portada_URL = db.Column(db.String(255))
    Fecha_Publicacion = db.Column(db.DateTime, default=datetime.utcnow)
    Fecha_Evento = db.Column(db.DateTime, nullable=True) # <-- NUEVO CAMPO AÑADIDO

class Video(db.Model):
    __tablename__ = 'Videos'
    ID_Video = db.Column(db.Integer, primary_key=True)
    Titulo = db.Column(db.String(200), nullable=False)
    Categoria_Video = db.Column(db.String(100))
    URL_Video = db.Column(db.String(255), nullable=False)
    Miniatura_URL = db.Column(db.String(255))
    Duracion = db.Column(db.String(10))


# --- NUEVAS RUTAS PARA LIBROS ---

@app.route("/admin/libros/editar/<int:id>", methods=['POST'])
def editar_libro(id):
    libro = Libro.query.get_or_404(id)
    libro.Titulo = request.form.get('titulo')
    libro.Autor = request.form.get('autor')
    libro.Ubicacion_Fisica = request.form.get('ubicacion')
    libro.Sinopsis = request.form.get('sinopsis')
    
    db.session.commit()
    return redirect('/admin-libros.html')

@app.route("/admin/libros/eliminar/<int:id>", methods=['POST'])
def eliminar_libro(id):
    libro = Libro.query.get_or_404(id)
    db.session.delete(libro)
    db.session.commit()
    return redirect('/admin-libros.html')

# ==========================================
# 3. RUTAS DE LA APLICACIÓN
# ==========================================
@app.route("/")
def index():
    # 1. Obtener la publicación más reciente para el cuadro principal
    publicacion_principal = Publicacion.query.order_by(Publicacion.Fecha_Publicacion.desc()).first()

    # 2. Obtener las siguientes 3 publicaciones
    otras_publicaciones = []
    if publicacion_principal:
        otras_publicaciones = Publicacion.query.order_by(Publicacion.Fecha_Publicacion.desc()).offset(1).limit(3).all()

    # 3. NUEVO: Obtener los últimos 4 libros agregados al catálogo
    ultimos_libros = Libro.query.order_by(Libro.ID_Libro.desc()).limit(4).all()

    # Pasamos también los libros a la plantilla
    return render_template("index.html", 
                           principal=publicacion_principal, 
                           noticias=otras_publicaciones,
                           libros=ultimos_libros)

@app.route("/catalogo.html")
def catalogo():
    # Obtenemos todos los libros de la base de datos
    libros = Libro.query.all()
    # Se los pasamos a la plantilla
    return render_template("catalogo.html", libros=libros)

# Modificamos la ruta para que acepte un ID numérico
@app.route("/libro-detalle/<int:id_libro>")
def libro_detalle(id_libro):
    # Buscamos el libro por su ID, si no existe devuelve un error 404
    libro = Libro.query.get_or_404(id_libro)
    return render_template("libro-detalle.html", libro=libro)

@app.route("/admin-libros.html")
def admin_libros():
    # Para la tabla del administrador también necesitamos los libros
    libros = Libro.query.all()
    return render_template("admin-libros.html", libros=libros)

@app.route("/admin/importar-libros", methods=['POST'])
def importar_libros():
    # 1. Verificar que se haya enviado un archivo
    if 'archivo_csv' not in request.files:
        return "No se envió ningún archivo", 400
    
    file = request.files['archivo_csv']
    if file.filename == '':
        return "No se seleccionó ningún archivo", 400

    if file and file.filename.endswith('.csv'):
        # 2. Leer el archivo CSV
        stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
        csv_reader = csv.DictReader(stream)
        
        for row in csv_reader:
            # 3. Extraer los datos según las columnas de tu Excel real
            titulo = row.get('NOMBRE', '').strip()
            autor = row.get('AUTOR', '').strip()
            materia = row.get('MATERIA', '').strip()
            tema = row.get('TEMA', '').strip()
            
            if not titulo:
                continue # Si no hay título, saltamos esa fila

            # 4. Buscar o crear la categoría (MATERIA) dinámicamente
            id_categoria = None
            if materia:
                categoria = Categoria.query.filter_by(Nombre_Categoria=materia).first()
                if not categoria:
                    categoria = Categoria(Nombre_Categoria=materia)
                    db.session.add(categoria)
                    db.session.commit() # Guardamos para obtener su ID
                id_categoria = categoria.ID_Categoria

            # 5. Crear el registro del libro
            nuevo_libro = Libro(
                Titulo=titulo,
                Autor=autor,
                ID_Categoria=id_categoria,
                Sinopsis=tema,
                Copias_Totales=1,       # Asignamos 1 por defecto al importarlo
                Copias_Disponibles=1    # Asignamos 1 por defecto al importarlo
            )
            db.session.add(nuevo_libro)
        
        # 6. Guardar todos los libros nuevos en la base de datos
        db.session.commit()
        
        # Redirigir de vuelta al panel de libros
        return redirect('/admin-libros.html')
    else:
        return "Por favor sube un archivo con extensión .csv", 400
    
@app.route("/admin/importar-excel", methods=['POST'])
def importar_excel():
    if 'archivo_excel' not in request.files:
        return "No se envió ningún archivo", 400
    
    file = request.files['archivo_excel']
    if file.filename == '':
        return "No se seleccionó ningún archivo", 400

    if file and (file.filename.endswith('.xlsx') or file.filename.endswith('.xls')):
        try:
            df = pd.read_excel(file)
            
            for index, row in df.iterrows():
                titulo = str(row.get('NOMBRE', '')).strip()
                autor = str(row.get('AUTOR', '')).strip()
                materia = str(row.get('MATERIA', '')).strip()
                tema = str(row.get('TEMA', '')).strip()
                local = str(row.get('LOCAL', '')).strip()
                
                if titulo == 'nan' or not titulo:
                    continue 
                
                if autor == 'nan': autor = 'Desconocido'
                if tema == 'nan': tema = ''
                if local == 'nan': local = ''

                id_categoria = None
                if materia and materia != 'nan':
                    categoria = Categoria.query.filter_by(Nombre_Categoria=materia).first()
                    if not categoria:
                        categoria = Categoria(Nombre_Categoria=materia)
                        db.session.add(categoria)
                        db.session.commit()
                    id_categoria = categoria.ID_Categoria

                # --- SOLUCIÓN: Generar un código único para evitar el error del ISBN ---
                codigo_unico = f"UNDAC-{uuid.uuid4().hex[:8].upper()}"

                nuevo_libro = Libro(
                    Titulo=titulo,
                    Autor=autor,
                    ISBN=codigo_unico,  # <--- Insertamos el código único aquí
                    ID_Categoria=id_categoria,
                    Sinopsis=tema,
                    Ubicacion_Fisica=local,
                    Copias_Totales=1,       
                    Copias_Disponibles=1    
                )
                db.session.add(nuevo_libro)
            
            db.session.commit()
            return redirect('/admin-libros.html')
            
        except Exception as e:
            # Si hay un error, deshacemos los cambios a medias para evitar corromper la BD
            db.session.rollback() 
            return f"Ocurrió un error al leer el Excel: {str(e)}", 500
    else:
        return "Por favor sube un archivo con extensión .xlsx o .xls", 400

@app.route("/videoteca.html")
def videoteca():
    return render_template("videoteca.html")

@app.route("/nosotros.html")
def nosotros():
    return render_template("nosotros.html")

@app.route("/noticias.html")
def noticias_publicas():
    # Obtenemos TODAS las publicaciones ordenadas de la más reciente a la más antigua
    publicaciones = Publicacion.query.order_by(Publicacion.Fecha_Publicacion.desc()).all()
    return render_template("noticias.html", publicaciones=publicaciones)

@app.route("/servicios.html")
def servicios():
    return render_template("servicios.html")

@app.route("/reglamento.html")
def reglamento():
    return render_template("reglamento.html")

@app.route("/admin-dashboard.html")
def admin_dashboard():
    return render_template("admin-dashboard.html")

@app.route("/admin-login.html")
def admin_login():
    return render_template("admin-login.html")

@app.route("/admin-noticias.html")
def admin_noticias():
    # Obtenemos todas las publicaciones ordenadas de la más reciente a la más antigua
    publicaciones = Publicacion.query.order_by(Publicacion.Fecha_Publicacion.desc()).all()
    return render_template("admin-noticias.html", publicaciones=publicaciones)

@app.route("/admin/noticias/crear", methods=['POST'])
def crear_noticia():
    titulo = request.form.get('titulo')
    tipo = request.form.get('tipo')
    contenido = request.form.get('contenido')
    imagen_url = request.form.get('imagen_url')
    fecha_evento_str = request.form.get('fecha_evento')

    # Convertir el string de fecha a objeto datetime si existe
    fecha_evento = None
    if fecha_evento_str:
        fecha_evento = datetime.strptime(fecha_evento_str, '%Y-%m-%d')

    nueva_publicacion = Publicacion(
        Titulo=titulo,
        Tipo_Publicacion=tipo,
        Contenido=contenido,
        Imagen_Portada_URL=imagen_url,
        Fecha_Evento=fecha_evento
    )
    
    db.session.add(nueva_publicacion)
    db.session.commit()
    
    return redirect('/admin-noticias.html')

@app.route("/admin/noticias/editar/<int:id>", methods=['POST'])
def editar_noticia(id):
    publicacion = Publicacion.query.get_or_404(id)
    
    publicacion.Titulo = request.form.get('titulo')
    publicacion.Tipo_Publicacion = request.form.get('tipo')
    publicacion.Contenido = request.form.get('contenido')
    publicacion.Imagen_Portada_URL = request.form.get('imagen_url')

    fecha_evento_str = request.form.get('fecha_evento')
    if fecha_evento_str:
        publicacion.Fecha_Evento = datetime.strptime(fecha_evento_str, '%Y-%m-%d')
    else:
        publicacion.Fecha_Evento = None

    db.session.commit()
    return redirect('/admin-noticias.html')

@app.route("/admin/noticias/eliminar/<int:id>", methods=['POST'])
def eliminar_noticia(id):
    publicacion = Publicacion.query.get_or_404(id)
    db.session.delete(publicacion)
    db.session.commit()
    return redirect('/admin-noticias.html')

if __name__ == "__main__":
    # Crea las tablas si no existen en la base de datos PW_BIBLIOTECA
    with app.app_context():
        db.create_all()
        
    app.run(debug=True, port=8000)