from flask import Flask, render_template

app = Flask(__name__)

# SECTION: Modelos Interactivos
interactives = [
    {
        'id': 'gears_v4',
        'title': 'Rueda Calendárica (V4)',
        'description': 'Versión 4 del sistema planetario de engranajes.',
        'filename': 'interactive_gears_v4.html',
        'type': 'interactive'
    },
    {
        'id': 'gears_v5',
        'title': 'Rueda Calendárica (V5)',
        'description': 'Versión 5 interactiva con mejoras de visualización.',
        'filename': 'interactive_gears_v5.html',
        'type': 'interactive'
    }
]

# SECTION 1: Representaciones del Tonalpohualli Básico
representaciones_basico = [
    {
        'id': 'toro_cuadricula_2d',
        'title': 'Plano Cuadrícula 2D (Estándar)',
        'description': 'Plano cartesiano con origen en la esquina inferior izquierda. Muestra la trayectoria de los 260 días y los hitos.',
        'filename': 'toro_cuadricula_interactiva.html',
        'type': 'representacion'
    },
    {
        'id': 'toro_cuadricula_2d_invertida',
        'title': 'Plano Cuadrícula 2D (Invertida)',
        'description': 'Plano matricial con lectura clásica (origen en esquina superior izquierda).',
        'filename': 'toro_cuadricula_interactiva_invertida.html',
        'type': 'representacion'
    },
    {
        'id': 'toro_animacion_2d',
        'title': 'Animación Cuadrícula 2D',
        'description': 'Evolución animada paso a paso del generador (1,1) sobre el plano cartesiano.',
        'filename': 'toro_animacion_2d.html',
        'type': 'representacion'
    },
    {
        'id': 'toro_animacion_3d',
        'title': 'Animación Toro 3D',
        'description': 'Evolución animada paso a paso del generador sobre la superficie del toro.',
        'filename': 'toro_animacion_3d.html',
        'type': 'representacion'
    }
]

# SECTION 2: Representaciones Visuales del Modelo de Meza
modelo_meza = [
    {
        'id': 'mapeo_2',
        'title': 'Mapeo 2 - Solenoide',
        'description': 'Visualización del mapeo interactivo 2.',
        'filename': 'mapeo_2_interactivo.html',
        'type': 'interactive'
    },
    {
        'id': 'mapeo_2_mod20',
        'title': 'Mapeo 2 - Módulo 20',
        'description': 'Visualización coloreada interactiva del solenoide módulo 20.',
        'filename': 'mapeo_2_solenoide_mod20_interactivo.html',
        'type': 'interactive'
    },
    {
        'id': 'solenoide_puentes',
        'title': 'Solenoide - Puentes Rojos',
        'description': 'Interactivo detallado resaltando conexiones críticas.',
        'filename': 'solenoide_circular_puentes_rojos_interactivo.html',
        'type': 'interactive'
    },
    {
        'id': 'anim_solenoide_coloreado',
        'title': 'Animación Solenoide Coloreado',
        'description': 'Video de la formación del solenoide.',
        'filename': 'animacion_2_solenoide_coloreado.mp4',
        'type': 'video'
    },
    {
        'id': 'anim_puentes_rojos',
        'title': 'Animación Puentes Rojos',
        'description': 'Video resaltando los puentes rojos en la estructura.',
        'filename': 'solenoide_circular_puentes_rojos.mp4',
        'type': 'video'
    },
    {
        'id': 'img_solenoide_coloreado',
        'title': 'Mapeo Solenoide Coloreado',
        'description': 'Imagen estática del mapeo coloreado.',
        'filename': 'mapeo_2_solenoide_coloreado.png',
        'type': 'image'
    },
    {
        'id': 'toro_cuadricula',
        'title': 'Toro Cuadrícula (18980 días)',
        'description': 'Mapeo del plano / toro desenrollado original.',
        'filename': 'toro_interactivo.html',
        'type': 'representacion'
    },
    {
        'id': 'toro_solenoide_puentes',
        'title': 'Toro Solenoide Continuo',
        'description': 'Topología ininterrumpida de solenoide con puentes envueltos en el toro.',
        'filename': 'toro_solenoide_puentes_interactivo.html',
        'type': 'representacion'
    },
    {
        'id': 'toro_rueda',
        'title': 'Toro Rueda Calendárica',
        'description': 'Modelo 3D interactivo con los 52 anillos.',
        'filename': 'toro_rueda_interactivo.html',
        'type': 'representacion'
    },
    {
        'id': 'img_solenoide_circular',
        'title': 'Solenoide Circular',
        'description': 'Imagen estática del solenoide circular.',
        'filename': 'solenoide_circular.png',
        'type': 'image'
    },
    {
        'id': 'toro_solenoide_mu3_3anios',
        'title': 'Toro Solenoide μ<sub>3</sub> (3 Años)',
        'description': 'Interactivo web demostrando los nemontemi del modelo μ<sub>3</sub>.',
        'filename': 'toro_solenoide_mu3_3anios.html',
        'type': 'representacion'
    },
    {
        'id': 'toro_solenoide_mu3_completo',
        'title': 'Toro Solenoide μ<sub>3</sub> Completo',
        'description': 'Video de la evolución entera de los 18,980 días con el modelo μ<sub>3</sub>.',
        'filename': 'toro_solenoide_mu3_completo.mp4',
        'type': 'video'
    }
]

# SECTION 3: Modelo Integrado de Meza
modelo_integrado = [
    {
        'id': 'toro_fractal_interactivo',
        'title': 'Toro Fractal',
        'description': 'Versión interactiva del toro de toros.',
        'filename': 'toro_fractal_interactivo.html',
        'type': 'representacion'
    },
    {
        'id': 'toro_fractal_estricto',
        'title': 'Toro Fractal (Estricto)',
        'description': 'Modelo interactivo con saltos matemáticos explícitos.',
        'filename': 'toro_fractal_estricto.html',
        'type': 'representacion'
    },
    {
        'id': 'toro_fractal_suave',
        'title': 'Toro Fractal (Suave)',
        'description': 'Modelo interactivo con interpolación topológica continua.',
        'filename': 'toro_fractal_suave.html',
        'type': 'representacion'
    },
    {
        'id': 'toro_fractal_mp4',
        'title': 'Video Fractal',
        'description': 'Primera versión del video completo.',
        'filename': 'toro_fractal_completo.mp4',
        'type': 'video'
    },
    {
        'id': 'toro_fractal_estricto_mp4',
        'title': 'Video Fractal Estricto',
        'description': 'Animación MP4 completa (18,980 días) con saltos.',
        'filename': 'toro_fractal_estricto_completo.mp4',
        'type': 'video'
    },
    {
        'id': 'toro_fractal_suave_mp4',
        'title': 'Video Fractal Suave',
        'description': 'Animación MP4 completa (18,980 días) suavizada.',
        'filename': 'toro_fractal_suave_completo.mp4',
        'type': 'video'
    }
]

# Combine both lists to easily look up by ID for the viewer
all_items = interactives + representaciones_basico + modelo_meza + modelo_integrado
item_dict = {item['id']: item for item in all_items}

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/gallery/<category>')
def gallery(category):
    subtitle = "Explora las simulaciones matemáticas y modelos interactivos."
    if category == 'interactives':
        items = interactives
        title = "Ruedas calendáricas"
    elif category == 'representaciones':
        items = representaciones_basico
        title = "Representaciones del Tonalpohualli Básico"
    elif category == 'modelo_meza':
        items = modelo_meza
        title = "Representaciones Visuales del Modelo de Meza"
    elif category == 'integrado':
        items = modelo_integrado
        title = "Modelo Integrado de Meza"
        subtitle = "Tloque Nahuaque"
    else:
        return "Category not found", 404
        
    return render_template('gallery.html', items=items, title=title, subtitle=subtitle)

@app.route('/view/<item_id>')
def view_item(item_id):
    item = item_dict.get(item_id)
    if not item:
        return "Not found", 404
    return render_template('viewer.html', item=item)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
