from flask import Flask, render_template

app = Flask(__name__)

# List of interactive models with their details
interactives = [
    {
        'id': 'gears_v5',
        'title': 'Rueda Calendárica (Engranajes)',
        'description': 'Simulación interactiva de la correlación de los calendarios mesoamericanos mediante un sistema planetario de engranajes (Versión 5).',
        'filename': 'interactive_gears_v5.html',
        'category': 'Tonamalat'
    },
    {
        'id': 'mapeo_1',
        'title': 'Mapeo 1 - Cuadrícula 2D',
        'description': 'Visualización del mapeo inicial en una cuadrícula plana interactiva.',
        'filename': 'mapeo_1_interactivo.html',
        'category': 'Solenoide'
    },
    {
        'id': 'mapeo_2',
        'title': 'Mapeo 2 - Solenoide Básico',
        'description': 'Estructura en 3D del solenoide proyectando las trayectorias matemáticas.',
        'filename': 'mapeo_2_interactivo.html',
        'category': 'Solenoide'
    },
    {
        'id': 'mapeo_2_mod20',
        'title': 'Mapeo 2 - Módulo 20',
        'description': 'Visualización coloreada interactiva del solenoide agrupando los datos en ciclos de módulo 20.',
        'filename': 'mapeo_2_solenoide_mod20_interactivo.html',
        'category': 'Solenoide'
    },
    {
        'id': 'solenoide_circular',
        'title': 'Solenoide Circular',
        'description': 'Representación de las trayectorias proyectadas sobre la superficie de un toro continuo.',
        'filename': 'solenoide_circular.html',
        'category': 'Solenoide'
    },
    {
        'id': 'solenoide_puentes',
        'title': 'Solenoide con Puentes Rojos',
        'description': 'Interactivo detallado resaltando conexiones críticas (puentes) en la estructura circular.',
        'filename': 'solenoide_circular_puentes_rojos_interactivo.html',
        'category': 'Solenoide'
    }
]

# Create a dictionary for quick lookup by id
interactive_dict = {item['id']: item for item in interactives}

@app.route('/')
def index():
    return render_template('index.html', interactives=interactives)

@app.route('/view/<item_id>')
def view_item(item_id):
    item = interactive_dict.get(item_id)
    if not item:
        return "Not found", 404
    return render_template('viewer.html', item=item)

if __name__ == '__main__':
    app.run(debug=True, port=5001) # Use port 5001 to avoid conflicting with the translator on 5000
