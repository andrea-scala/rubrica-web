from flask import Flask, render_template, request, redirect, url_for, session
from dotenv import load_dotenv
import os
import rubrica
from models import Persona

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

def get_db_config():
    return session.get('db_config', None)

@app.route('/')
def index():
    return redirect(url_for('lista'))

@app.route('/lista')
def lista():
    contatti = rubrica.get_all(get_db_config())
    return render_template('lista.html', contatti=contatti)

@app.route('/editor')
def editor():
    id = request.args.get('id')
    persona = rubrica.get_by_id(id, get_db_config()) if id else Persona()
    return render_template('editor.html', persona=persona)

@app.route('/salva', methods=['POST'])
def salva():
    id = request.form.get('id')
    persona = Persona(
        id       = int(id) if id else None,
        nome     = request.form.get('nome'),
        cognome  = request.form.get('cognome'),
        indirizzo= request.form.get('indirizzo'),
        telefono = request.form.get('telefono'),
        eta      = int(request.form.get('eta') or 0)
    )
    if persona.id:
        rubrica.update(persona, get_db_config())
    else:
        rubrica.insert(persona, get_db_config())
    return redirect(url_for('lista'))

@app.route('/elimina/<int:id>')
def elimina(id):
    rubrica.delete(id, get_db_config())
    return redirect(url_for('lista'))

if __name__ == '__main__':
    app.run(debug=True)
