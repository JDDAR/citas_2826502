from . import app, db
from .models import Medico, Paciente, Consultorio, Cita 
from flask import render_template, request

@app.route('/medicos')
def get_all_medicos():
    medicos = Medico.query.all()
    return render_template('medicos.html', medicos = medicos) 

@app.route('/pacientes')
def get_all_pacientes():
    pacientes = Paciente.query.all()
    return render_template('pacientes.html', pacientes = pacientes)

@app.route('/consultorios')
def get_all_consultorios():
    consultorios = Consultorio.query.all()
    return render_template('consultorios.html', consultorios = consultorios )

@app.route('/citas')
def get_all_citas():
    citas = Cita.query.all()
    return render_template("citas.html", citas = citas)


############# rutas para selecionar detalles 

@app.route('/medicos/<int:id>')
def get_medico_by_id(id):
    ##return 'id del medico: ' + str(id)
    #traer el medico por id utilizando la entidad medico 
    medico = Medico.query.get(id)
    return render_template('medico.html', medicoId = medico)

@app.route('/pacientes/<int:id>')
def get_paciente_by_id(id):
    paciente = Paciente.query.get(id)
    return render_template('paciente.html', pacienteId = paciente)

@app.route('/consultorios/<int:id>')
def get_consultorio_by_id(id):
    consultorio = Consultorio.query.get(id)
    return render_template('consultorio.html', consultorioId = consultorio)

@app.route('/citas/<int:id>')
def get_citas_by_id(id):
    citas = Cita.query.get(id)
    return render_template('cita.html', citaId = citas)


################ Creando rutas pra nuevo medico 
@app.route('/medicos/create' , methods = [ 'GET' , 'POST'])
def create_medico():
    ##Mostrar el formulario: metodo GET  
    if( request.method == 'GET' ):
        especialidades = [
            'Cardiologia',
            'Pediatria',
            'Psicologia'
        ]
        return render_template('medico_form.html', especialidades = especialidades)
    ##cuando el usuario preiona el boton de guardar 
    ##los datos del formulario viajan al servidor utilisando el metodo POST
    elif( request.method == 'POST'):
        #cuando se presiona 'crear'
        ##return request.form['especialidad']
        new_medico = Medico(nombres = request.form['nombres'],
                            apellidos = request.form['apellidos'],
                            tipo_identificacion = request.form['tipoID'],
                            numero_identificacion = request.form['numeroID'],
                            registro_medico = request.form['registroMedico'],
                            especialidad = request.form['especialidad']
                            )
        ##añadirlo a sqlalchemy 
        db.session.add(new_medico)
        db.session.commit()
        return "Medico registrado" 

############### Creando rutas para nuevo paciente 
@app.route('/pacientes/create', methods = ['GET' , 'POST'])
def create_paciente():
    if(request.method == 'GET'):
        return render_template('paciente_form.html')
    elif(request.method == 'POST'):
        new_paciente = Paciente(nombres = request.form['nombres'],
                                apellidos = request.form['apellidos'],
                                tipo_identificacion = request.form['tipoID'],
                                numero_identificacion = request.form['numeroID'],
                                altura = request.form['altura'],
                                tipo_sangre = request.form['tipoSangre']
                                )
        db.session.add(new_paciente)
        db.session.commit()
        return "Paciente Registrado "

############## Creando Nuevos consultorios 

@app.route('/consultorios/create', methods = ['GET', 'POST'])
def create_consultorio():
    if(request.method == 'GET'):
        return render_template('consultorio_form.html')
    elif(request.method == 'POST'):
        new_consultorio = Consultorio( numero = request.form['numero'] )
    db.session.add(new_consultorio)
    db.session.commit()
    return 'consultorio creado '

############## Creando nuevas citas  

@app.route('/citas/create', methods = ['GET', 'POST'])
def create_cita():
    if(request.method == 'GET'):
        return render_template('cita_form.html') 
    
        
        





