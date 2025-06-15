from flask import Blueprint, render_template, request, redirect, url_for
from .models import Persona
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    personas = Persona.query.all()
    return render_template('index.html', personas=personas)

@main.route('/crear', methods=['POST'])
def crear():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    dni = request.form['dni']

    nueva_persona = Persona(nombre=nombre, apellido=apellido, dni=dni)
    db.session.add(nueva_persona)
    db.session.commit()

    return redirect(url_for('main.index') + "?agregado=ok")

    #return redirect(url_for('main.index'))


@main.route('/eliminar/<int:id>')
def eliminar(id):
    persona = Persona.query.get_or_404(id)
    db.session.delete(persona)
    db.session.commit()

    return redirect(url_for('main.index') + "?eliminado=ok")
    #return redirect(url_for('main.index'))


# Rutas disponibles
# / → Lista todas las personas y muestra el formulario
# /crear → Guarda una nueva persona (POST)
# /eliminar/<id> → Elimina una persona por ID