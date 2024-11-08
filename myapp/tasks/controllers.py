#aqui van los codigos de las funciones que se van a crear y llamar
from flask import Blueprint

taskRoute = Blueprint('tasks', __name__, url_prefix='/tasks')

#Creacion de rutas en el modulo rutas
@taskRoute.route('/')
def index():
    return 'Index' #aqui tendremos toda la base de datos con los registro

@taskRoute.route('/<int:id>')
def show(id:int):
    return 'Show ' +str(id)

@taskRoute.route('/delete/<int:id>')
def delete(id:int):
    return 'delete ' +str(id)

@taskRoute.route('/create', methods=('GET','POST'))
def create():
    return 'Create '

@taskRoute.route('/update/<int:id>', methods=['GET','POST'])
def update(id:int):
    return 'update '+str(id)