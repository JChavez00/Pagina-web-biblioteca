from pathlib import Path

files = {
    "templates/nosotros.html": """{% extends \"base.html\" %}

{% block title %}Nosotros | Sistema de Bibliotecas UNDAC{% endblock %}

{% block content %}
<section class=\"page-header\" style=\"background: linear-gradient(to right, #0F172A, #1E3A8A);\">
    <div class=\"container\" data-aos=\"fade-up\">
        <h1>Sobre Nosotros</h1>
        <p>Dirección de la Unidad de Sistemas de Biblioteca \"Gerardo Patiño López\"</p>
    </div>
</section>

<section class=\"container\" style=\"padding: 4rem 1.5rem;\">
    <div class=\"section-header\" data-aos=\"fade-up\">
        <h2>Nuestra Biblioteca</h2>
        <div class=\"title-line\"></div>
        <p>Conoce los pilares que rigen nuestro sistema de bibliotecas.</p>
    </div>

    <div class=\"grid-2\" style=\"gap: 3rem;\">
        <div class=\"service-card\" data-aos=\"fade-right\" style=\"padding: 2rem; display: block;\">
            <div class=\"icon-wrapper\" style=\"margin-bottom: 1rem; width: 60px; height: 60px;\"><i class=\"fas fa-bullseye\" style=\"font-size: 1.5rem;\"></i></div>
            <h3 style=\"margin-bottom: 1rem; color: var(--primary);\">Misión</h3>
            <p style=\"color: var(--gray-500); text-align: justify;\">Brindar y ofrecer servicios de información y proporcionar acceso a distintas fuentes bibliográficas para satisfacer las necesidades y demandas de profesores, investigadores, alumnos y demás miembros de la comunidad universitaria, contribuyendo de esta manera al proceso de enseñanza, aprendizaje, investigación, extensión y formación profesional.</p>
        </div>

        <div class=\"service-card\" data-aos=\"fade-left\" style=\"padding: 2rem; display: block;\">
            <div class=\"icon-wrapper\" style=\"margin-bottom: 1rem; width: 60px; height: 60px;\"><i class=\"fas fa-eye\" style=\"font-size: 1.5rem;\"></i></div>
            <h3 style=\"margin-bottom: 1rem; color: var(--primary);\">Visión</h3>
            <p style=\"color: var(--gray-500); text-align: justify;\">Alcanzar la excelencia en la prestación del servicio de información conforme a los estándares de calidad, orientados a la generación del pensamiento científico humanístico y técnico, para constituirnos en un referente nacional en el ámbito de las bibliotecas universitarias.</p>
        </div>
    </div>

    <div style=\"margin-top: 3rem; background: var(--light); padding: 3rem; border-radius: var(--radius-md);\" data-aos=\"fade-up\">
        <h3 style=\"text-align: center; margin-bottom: 2rem; color: var(--primary);\">Nuestros Valores</h3>
        <ul style=\"display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; color: var(--gray-500);\">
            <li><i class=\"fas fa-check-circle\" style=\"color: var(--secondary); margin-right: 0.5rem;\"></i> Garantía del derecho a la información.</li>
            <li><i class=\"fas fa-check-circle\" style=\"color: var(--secondary); margin-right: 0.5rem;\"></i> Innovación tecnológica de recursos.</li>
            <li><i class=\"fas fa-check-circle\" style=\"color: var(--secondary); margin-right: 0.5rem;\"></i> Formación continua del personal bajo un marco ético.</li>
            <li><i class=\"fas fa-check-circle\" style=\"color: var(--secondary); margin-right: 0.5rem;\"></i> Compromiso en proyectos de innovación y cultura.</li>
        </ul>
    </div>
</section>

<section class=\"bg-light\" style=\"padding: 4rem 0;\">
    <div class=\"container\">
        <div class=\"section-header\" data-aos=\"fade-up\">
            <h2>Identidad UNDAC</h2>
            <div class=\"title-line\"></div>
            <p>Alineados con los principios de nuestra Alma Máter</p>
        </div>

        <div class=\"grid-2\" style=\"gap: 3rem; align-items: center;\">
            <div data-aos=\"fade-right\">
                <img src=\"../static/assets/img/logo-undac.png\" alt=\"Logo UNDAC\" style=\"max-width: 300px; margin: 0 auto; display: block;\">
            </div>
            <div data-aos=\"fade-left\">
                <h3 style=\"color: var(--primary); margin-bottom: 0.5rem;\">Misión Institucional</h3>
                <p style=\"color: var(--gray-500); margin-bottom: 1.5rem; text-align: justify;\">Formar profesionales competitivos, innovadores, con capacidad científica, tecnológica, humanista y multilingüe, integrando Universidad-Empresa-Sociedad, con valores éticos y morales para una mejor calidad de vida de la Región y el país.</p>
                <h3 style=\"color: var(--primary); margin-bottom: 0.5rem;\">Visión Institucional</h3>
                <p style=\"color: var(--gray-500); text-align: justify;\">Ser universidad líder en la formación profesional, con alto nivel de responsabilidad social, que permita el desarrollo sustentable y el mejoramiento de la calidad de vida en la región, el país y el mundo.</p>
            </div>
        </div>
    </div>
</section>
{% endblock %}
""",
    "templates/reglamento.html": """{% extends \"base.html\" %}

{% block title %}Reglamento | Sistema de Bibliotecas UNDAC{% endblock %}

{% block content %}
<style>
    .reglamento-card { background: white; padding: 2rem; border-radius: var(--radius-md); box-shadow: var(--shadow-sm); margin-bottom: 2rem; }
    .reglamento-card h3 { color: var(--primary); border-bottom: 2px solid var(--secondary); display: inline-block; margin-bottom: 1.5rem; padding-bottom: 0.3rem; }
    .table-reglamento { width: 100%; border-collapse: collapse; margin-top: 1rem; }
    .table-reglamento th, .table-reglamento td { padding: 1rem; border: 1px solid var(--gray-200); text-align: left; }
    .table-reglamento th { background: var(--gray-100); color: var(--primary); }
    .alert-danger { background: #fee2e2; color: #991b1b; padding: 1rem; border-radius: var(--radius-sm); border-left: 4px solid #ef4444; margin-top: 1rem; }
</style>

<section class=\"page-header\" style=\"background: linear-gradient(to right, #1E293B, #0F172A);\">
    <div class=\"container\" data-aos=\"fade-up\">
        <h1>Reglamento del Sistema de Bibliotecas</h1>
        <p>Normas de uso, derechos, deberes y transparencia en los procesos administrativos.</p>
    </div>
</section>

<main class=\"container\" style=\"padding: 4rem 1.5rem;\">
    <div class=\"reglamento-card\" data-aos=\"fade-up\">
        <h3>Capítulo I: De los Usuarios</h3>
        <div class=\"grid-2\" style=\"gap: 2rem; margin-top: 1rem;\">
            <div>
                <h4 style=\"margin-bottom: 0.5rem;\"><i class=\"fas fa-user-graduate\"></i> Usuarios Internos</h4>
                <p style=\"color: var(--gray-500);\">Docentes, investigadores, estudiantes de Pregrado y Postgrado con matrícula vigente, y personal administrativo[cite: 41, 42, 43].</p>
            </div>
            <div>
                <h4 style=\"margin-bottom: 0.5rem;\"><i class=\"fas fa-user-friends\"></i> Usuarios Externos</h4>
                <p style=\"color: var(--gray-500);\">Ex alumnos, estudiantes del Centro Pre y personas ajenas a la comunidad universitaria con identificación vigente[cite: 46, 47, 48].</p>
            </div>
        </div>
    </div>

    <div class=\"reglamento-card\" data-aos=\"fade-up\">
        <h3>Deberes y Prohibiciones</h3>
        <ul class=\"service-list\" style=\"columns: 2;\">
            <li><i class=\"fas fa-exclamation-triangle\"></i> Guardar silencio absoluto en las salas[cite: 60].</li>
            <li><i class=\"fas fa-exclamation-triangle\"></i> No ingresar alimentos ni bebidas[cite: 62].</li>
            <li><i class=\"fas fa-exclamation-triangle\"></i> No colocar mochilas sobre las mesas de lectura[cite: 64].</li>
            <li><i class=\"fas fa-exclamation-triangle\"></i> Prohibido el ingreso con vestimenta hospitalaria (mandiles, scrubs)[cite: 63].</li>
            <li><i class=\"fas fa-exclamation-triangle\"></i> Respetar las fechas de devolución de materiales[cite: 57].</li>
        </ul>
    </div>

    <div class=\"reglamento-card\" data-aos=\"fade-up\">
        <h3>Anexo 2: Tarifas y Multas</h3>
        <p style=\"color: var(--gray-500); margin-bottom: 1rem;\">Los pagos se depositan directamente a la cuenta de tesorería UNDAC[cite: 201].</p>
        <table class=\"table-reglamento\">
            <thead>
                <tr>
                    <th>Concepto</th>
                    <th>Monto</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Retraso en devolución (por día)</td>
                    <td>S/. 5.00</td>
                </tr>
                <tr>
                    <td>Carné de Lector (vigencia anual)</td>
                    <td>S/. 6.00</td>
                </tr>
                <tr>
                    <td>Constancia de NO ADEUDAR</td>
                    <td>S/. 5.00</td>
                </tr>
                <tr>
                    <td>Procesamiento de libros</td>
                    <td>S/. 25.00</td>
                </tr>
            </tbody>
        </table>
        <div class=\"alert-danger\">
            <strong>Nota sobre libros de Alta Demanda:</strong> El retraso en estos ejemplares genera una multa acumulable por cada hora transcurrida[cite: 94].
        </div>
    </div>

    <div class=\"reglamento-card\" data-aos=\"fade-up\" style=\"border-left: 5px solid #ef4444;\">
        <h3 style=\"color: #991b1b; border-bottom-color: #ef4444;\">Faltas Graves y Sanciones</h3>
        <p style=\"margin-bottom: 1rem;\">Las faltas graves causan la suspensión temporal de todos los servicios durante un semestre académico[cite: 151]:</p>
        <ul class=\"service-list\">
            <li><i class=\"fas fa-times-circle\" style=\"color: #ef4444;\"></i> Sustracción, mutilación o deterioro del material bibliográfico[cite: 153].</li>
            <li><i class=\"fas fa-times-circle\" style=\"color: #ef4444;\"></i> Uso de documento de identidad de otra persona[cite: 152].</li>
            <li><i class=\"fas fa-times-circle\" style=\"color: #ef4444;\"></i> Pérdida de material (requiere reposición de libro nuevo más suspensión)[cite: 155, 156].</li>
        </ul>
    </div>
</main>
{% endblock %}
""",
    "templates/servicios.html": """{% extends \"base.html\" %}

{% block title %}Servicios | Sistema de Bibliotecas UNDAC{% endblock %}

{% block content %}
<style>
    .service-detail-card {
        background: white;
        border-radius: var(--radius-md);
        box-shadow: var(--shadow-sm);
        padding: 2rem;
        transition: var(--transition);
        border-top: 4px solid transparent;
        height: 100%;
    }
    .service-detail-card:hover {
        box-shadow: var(--shadow-md);
        border-top-color: var(--primary);
        transform: translateY(-5px);
    }
    .service-icon-large {
        font-size: 2.5rem;
        color: var(--primary);
        margin-bottom: 1.5rem;
    }
    .service-list {
        margin-top: 1rem;
        color: var(--gray-500);
        font-size: 0.95rem;
    }
    .service-list li {
        margin-bottom: 0.5rem;
        display: flex;
        gap: 0.5rem;
    }
    .service-list i {
        color: var(--secondary);
        margin-top: 0.25rem;
    }
</style>

<section class=\"page-header\" style=\"background: linear-gradient(to right, #0F172A, #3B82F6);\">
    <div class=\"container\" data-aos=\"fade-up\">
        <h1>Servicios de la Biblioteca</h1>
        <p>Conoce todo lo que la DIUNSIBI tiene para apoyar tu desarrollo académico e investigativo.</p>
    </div>
</section>

<section class=\"container\" style=\"padding: 4rem 1.5rem;\">
    <div class=\"grid-3\" style=\"gap: 2rem;\">
        <div class=\"service-detail-card\" data-aos=\"fade-up\" data-aos-delay=\"100\">
            <i class=\"fas fa-book-reader service-icon-large\"></i>
            <h3>Préstamo de Libros</h3>
            <p style=\"color: var(--gray-500); margin-top: 0.5rem;\">Accede a nuestra amplia colección bibliográfica física.</p>
            <ul class=\"service-list\">
                <li><i class=\"fas fa-check\"></i> <strong>En Sala:</strong> Hasta 5 libros a la vez.</li>
                <li><i class=\"fas fa-check\"></i> <strong>A Domicilio (Alumnos/Docentes):</strong> Hasta 2 ejemplares por 3 días calendario.</li>
                <li><i class=\"fas fa-check\"></i> <strong>Alta Demanda:</strong> Préstamo a partir de las 9:00 p.m. Devolución al día siguiente (8:00 - 8:10 a.m.)</li>
            </ul>
        </div>
        <div class=\"service-detail-card\" data-aos=\"fade-up\" data-aos-delay=\"200\">
            <i class=\"fas fa-users service-icon-large\"></i>
            <h3>Salas Polivalentes</h3>
            <p style=\"color: var(--gray-500); margin-top: 0.5rem;\">Espacios diseñados para el estudio y trabajo grupal.</p>
            <ul class=\"service-list\">
                <li><i class=\"fas fa-check\"></i> Tiempo máximo de uso: 2 horas (extensibles si no hay reservas).</li>
                <li><i class=\"fas fa-check\"></i> Requiere dejar el carné de lector DIUNSIBI.</li>
                <li><i class=\"fas fa-check\"></i> Docentes pueden reservar con 24h de anticipación para sustentaciones o entrevistas.</li>
            </ul>
        </div>
        <div class=\"service-detail-card\" data-aos=\"fade-up\" data-aos-delay=\"300\">
            <i class=\"fas fa-print service-icon-large\"></i>
            <h3>Servicio de Reprografía</h3>
            <p style=\"color: var(--gray-500); margin-top: 0.5rem;\">Fotocopiado con fines estrictamente académicos (Ley 822).</p>
            <ul class=\"service-list\">
                <li><i class=\"fas fa-check\"></i> <strong>Libros:</strong> Máximo hasta 2 capítulos.</li>
                <li><i class=\"fas fa-check\"></i> <strong>Revistas:</strong> Hasta 3 artículos por fascículo.</li>
                <li><i class=\"fas fa-check\"></i> <strong>Tesis (Restringido):</strong> Solo resumen, introducción, conclusiones, bibliografía y anexos.</li>
            </ul>
        </div>
        <div class=\"service-detail-card\" data-aos=\"fade-up\" data-aos-delay=\"400\">
            <i class=\"fas fa-desktop service-icon-large\"></i>
            <h3>Equipos y Base de Datos</h3>
            <p style=\"color: var(--gray-500); margin-top: 0.5rem;\">Acceso a internet y catálogos virtuales.</p>
            <ul class=\"service-list\">
                <li><i class=\"fas fa-check\"></i> Tiempo máximo de uso en sala: 1 hora.</li>
                <li><i class=\"fas fa-check\"></i> Acceso al repositorio institucional y revistas científicas.</li>
                <li><i class=\"fas fa-check\"></i> Acceso a Biblioteca Virtual (eLibro).</li>
            </ul>
        </div>
        <div class=\"service-detail-card\" data-aos=\"fade-up\" data-aos-delay=\"500\">
            <i class=\"fas fa-chalkboard-teacher service-icon-large\"></i>
            <h3>Formación de Usuarios</h3>
            <p style=\"color: var(--gray-500); margin-top: 0.5rem;\">Programa de Alfabetización Informacional (ALFIN).</p>
            <ul class=\"service-list\">
                <li><i class=\"fas fa-check\"></i> Aprende a buscar y recuperar información científica.</li>
                <li><i class=\"fas fa-check\"></i> Sesiones de 2 horas programadas todo el año.</li>
                <li><i class=\"fas fa-check\"></i> Inscripciones vía sistema KOHA o presencial.</li>
            </ul>
        </div>
        <div class=\"service-detail-card\" data-aos=\"fade-up\" data-aos-delay=\"600\">
            <i class=\"fas fa-laptop-house service-icon-large\"></i>
            <h3>Préstamo Digital</h3>
            <p style=\"color: var(--gray-500); margin-top: 0.5rem;\">Si estás fuera de tu sede, te acercamos la información.</p>
            <ul class=\"service-list\">
                <li><i class=\"fas fa-check\"></i> Solicita capítulos específicos de libros físicos vía correo electrónico.</li>
                <li><i class=\"fas fa-check\"></i> Se remiten en formato digital respetando los derechos de autor.</li>
            </ul>
        </div>
    </div>
</section>
{% endblock %}
""",
    "templates/videoteca.html": """{% extends \"base.html\" %}

{% block title %}Videoteca | Sistema de Bibliotecas UNDAC{% endblock %}

{% block body_class %} class=\"videoteca-body\"{% endblock %}

{% block content %}
<section class=\"videoteca-hero\">
    <div class=\"videoteca-hero-content\" data-aos=\"fade-up\">
        <span style=\"color: var(--secondary); font-weight: 700; text-transform: uppercase; letter-spacing: 2px;\">Ciclo de Conferencias 2026</span>
        <h1>El futuro de la Inteligencia Artificial en la Academia</h1>
        <p style=\"font-size: 1.1rem; margin-bottom: 2rem; color: #e2e8f0;\">Descubre cómo las nuevas tecnologías están transformando los procesos de investigación y redacción científica en la universidad moderna.</p>
        <button class=\"play-btn-large\">
            <i class=\"fas fa-play\"></i> Reproducir Video Principal
        </button>
    </div>
</section>

<main class=\"container video-section\">
    <div style=\"display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; flex-wrap: wrap; gap: 1rem;\" data-aos=\"fade-up\">
        <div class=\"search-admin\" style=\"background: #1e293b; max-width: 400px; width: 100%;\">
            <input type=\"text\" placeholder=\"Buscar video, autor o serie...\" style=\"color: white;\">
            <button class=\"btn\" style=\"background: transparent; color: white;\"><i class=\"fas fa-search\"></i></button>
        </div>
        <select style=\"padding: 0.75rem 1rem; border-radius: 8px; background: #1e293b; color: white; border: 1px solid #334155;\">
            <option value=\"todas\">Todas las categorías</option>
            <option value=\"tutoriales\">Tutoriales Base de Datos</option>
            <option value=\"entrevistas\">Entrevistas e Investigación</option>
            <option value=\"jueves-cultural\">Jueves Culturales UNDAC</option>
        </select>
    </div>

    <h2 data-aos=\"fade-right\">Tutoriales: Bases de Datos Académicas</h2>
    <div class=\"video-grid\" style=\"margin-bottom: 4rem;\">
        <div class=\"video-card\" data-aos=\"fade-up\" data-aos-delay=\"100\">
            <div class=\"video-thumb\">
                <img src=\"https://images.unsplash.com/photo-1555066931-4365d14bab8c?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80\" alt=\"Scopus Tutorial\">
                <span class=\"video-duration\">14:20</span>
                <div class=\"video-play-icon\"><i class=\"fas fa-play\"></i></div>
            </div>
            <div class=\"video-info\">
                <h3>Cómo realizar búsquedas avanzadas en Scopus</h3>
                <p>Módulo 1 - Alfabetización Informacional</p>
            </div>
        </div>
        <div class=\"video-card\" data-aos=\"fade-up\" data-aos-delay=\"200\">
            <div class=\"video-thumb\">
                <img src=\"https://images.unsplash.com/photo-1456324504439-367cee3b3c32?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80\" alt=\"E-Libro Tutorial\">
                <span class=\"video-duration\">08:45</span>
                <div class=\"video-play-icon\"><i class=\"fas fa-play\"></i></div>
            </div>
            <div class=\"video-info\">
                <h3>Navegación y descarga de libros en eLibro</h3>
                <p>Módulo 1 - Alfabetización Informacional</p>
            </div>
        </div>
        <div class=\"video-card\" data-aos=\"fade-up\" data-aos-delay=\"300\">
            <div class=\"video-thumb\">
                <img src=\"https://images.unsplash.com/photo-1542621334-a2542d773431?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80\" alt=\"Turnitin Tutorial\">
                <span class=\"video-duration\">22:10</span>
                <div class=\"video-play-icon\"><i class=\"fas fa-play\"></i></div>
            </div>
            <div class=\"video-info\">
                <h3>Interpretación de reportes de similitud en Turnitin</h3>
                <p>Herramientas para Docentes</p>
            </div>
        </div>
        <div class=\"video-card\" data-aos=\"fade-up\" data-aos-delay=\"400\">
            <div class=\"video-thumb\">
                <img src=\"https://images.unsplash.com/photo-1606326608606-aa0b62935f2b?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80\" alt=\"Mendeley Tutorial\">
                <span class=\"video-duration\">18:30</span>
                <div class=\"video-play-icon\"><i class=\"fas fa-play\"></i></div>
            </div>
            <div class=\"video-info\">
                <h3>Gestión de referencias con Mendeley Reference Manager</h3>
                <p>Taller de Redacción Científica</p>
            </div>
        </div>
    </div>

    <h2 data-aos=\"fade-right\">Jueves Culturales UNDAC</h2>
    <div class=\"video-grid\" style=\"margin-bottom: 2rem;\">
        <div class=\"video-card\" data-aos=\"fade-up\" data-aos-delay=\"100\">
            <div class=\"video-thumb\">
                <img src=\"https://images.unsplash.com/photo-1478147424044-4874c7717466?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80\" alt=\"Literatura\">
                <span class=\"video-duration\">55:00</span>
                <div class=\"video-play-icon\"><i class=\"fas fa-play\"></i></div>
            </div>
            <div class=\"video-info\">
                <h3>Análisis de la obra de César Vallejo</h3>
                <p>Facultad de Ciencias de la Educación</p>
            </div>
        </div>
        <div class=\"video-card\" data-aos=\"fade-up\" data-aos-delay=\"200\">
            <div class=\"video-thumb\">
                <img src=\"https://images.unsplash.com/photo-1460518451285-b82b3dcb7831?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80\" alt=\"Psicologia\">
                <span class=\"video-duration\">42:15</span>
                <div class=\"video-play-icon\"><i class=\"fas fa-play\"></i></div>
            </div>
            <div class=\"video-info\">
                <h3>Salud Mental de los Estudiantes en la Era Digital</h3>
                <p>Psicología y Bienestar Universitario</p>
            </div>
        </div>
        <div class=\"video-card\" data-aos=\"fade-up\" data-aos-delay=\"300\">
            <div class=\"video-thumb\">
                <img src=\"https://images.unsplash.com/photo-1540317580384-e5d43616b9aa?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80\" alt=\"Ingenieria\">
                <span class=\"video-duration\">1:18:20</span>
                <div class=\"video-play-icon\"><i class=\"fas fa-play\"></i></div>
            </div>
            <div class=\"video-info\">
                <h3>Innovaciones en la Ingeniería de Minas en Cerro de Pasco</h3>
                <p>Semana de la Ingeniería UNDAC</p>
            </div>
        </div>
    </div>
</main>
{% endblock %}
""",
    "templates/libro-detalle.html": """{% extends \"base.html\" %}

{% block title %}Estructuras de Datos y Algoritmos en Python | Biblioteca UNDAC{% endblock %}

{% block content %}
<div class=\"breadcrumb\">
    <div class=\"container\">
        <a href=\"/\">Inicio</a> <i class=\"fas fa-chevron-right\"></i>
        <a href=\"/catalogo.html\">Catálogo</a> <i class=\"fas fa-chevron-right\"></i>
        <span>Ingeniería</span> <i class=\"fas fa-chevron-right\"></i>
        <span class=\"current\">Estructuras de Datos y Algoritmos en Python</span>
    </div>
</div>

<section class=\"book-detail-section\">
    <div class=\"container\">
        <div class=\"grid-2 book-detail-grid\">
            <div class=\"book-sticky-sidebar\">
                <div class=\"book-cover-panel\">
                    <img src=\"https://images.unsplash.com/photo-1544947950-fa07a98d237f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80\" alt=\"Estructuras de Datos\">
                    <span class=\"book-status\"><i class=\"fas fa-check-circle\"></i> 3 Copias Disponibles</span>
                    <div style=\"display: flex; flex-direction: column; gap: 1rem;\">
                        <button class=\"btn btn-primary w-full\"><i class=\"fas fa-bookmark\"></i> Reservar este libro</button>
                        <button class=\"btn btn-outline w-full\"><i class=\"fas fa-share-alt\"></i> Compartir</button>
                    </div>
                </div>
            </div>
            <div>
                <span class=\"book-info-category\">Ingeniería de Sistemas</span>
                <h1 class=\"book-info-title\">Estructuras de Datos y Algoritmos en Python</h1>
                <p class=\"book-info-author\">Por <strong>Michael T. Goodrich</strong>, <strong>Roberto Tamassia</strong>, <strong>Michael H. Goldwasser</strong></p>
                <div class=\"book-info-panel\">
                    <h3>Sinopsis</h3>
                    <p>Basado en el éxito comercial de \"Data Structures and Algorithms in Java\", este nuevo título ofrece una introducción completa e integral a las estructuras de datos y algoritmos, esta vez diseñados explícitamente y de manera nativa para el lenguaje de programación Python.<br><br>El libro proporciona un enfoque moderno orientado a objetos para el uso de estructuras de datos estándar y algoritmos asociados, con descripciones detalladas de su implementación práctica eficiente mediante el lenguaje Python.</p>
                </div>
                <div class=\"book-info-panel\">
                    <h3>Detalles del Libro</h3>
                    <div class=\"book-details-grid\">
                        <div class=\"book-details-label\">ISBN:</div>
                        <div>978-8441539241</div>
                        <div class=\"book-details-label\">Editorial:</div>
                        <div>Anaya Multimedia</div>
                        <div class=\"book-details-label\">Año de Edición:</div>
                        <div>2017</div>
                        <div class=\"book-details-label\">Nº Páginas:</div>
                        <div>784</div>
                        <div class=\"book-details-label\">Idioma:</div>
                        <div>Español</div>
                        <div class=\"book-details-label\">Ubicación:</div>
                        <div>Piso 2 - Estante B - Fila 4</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
{% endblock %}
"""
}

root = Path(__file__).resolve().parent
for relative_path, content in files.items():
    file_path = root / relative_path
    file_path.write_text(content, encoding="utf-8")
    print(f"Wrote {file_path}")
