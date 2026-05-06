from flask import Flask, render_template

app = Flask(__name__)

# List of interactive models (HTML)
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
    },
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
    }
]

# List of simulations (videos and images)
simulations = [
    {
        'id': 'anim_solenoide_coloreado',
        'title': 'Animación Solenoide Coloreado',
        'description': 'Video de la formación del solenoide.',
        'filename': 'animacion_2_solenoide_coloreado.mp4',
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
        'id': 'anim_puentes_rojos',
        'title': 'Animación Puentes Rojos',
        'description': 'Video resaltando los puentes rojos en la estructura.',
        'filename': 'solenoide_circular_puentes_rojos.mp4',
        'type': 'video'
    },
    {
        'id': 'img_solenoide_circular',
        'title': 'Solenoide Circular',
        'description': 'Imagen estática del solenoide circular.',
        'filename': 'solenoide_circular.png',
        'type': 'image'
    }
]

# Combine both lists to easily look up by ID for the viewer
all_items = interactives + simulations
item_dict = {item['id']: item for item in all_items}

@app.route('/')
def index():
    return render_template('index.html', interactives=interactives, simulations=simulations)

@app.route('/view/<item_id>')
def view_item(item_id):
    item = item_dict.get(item_id)
    if not item:
        return "Not found", 404
    return render_template('viewer.html', item=item)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
