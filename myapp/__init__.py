from flask import Flask

from myapp.config import DevConfig
from myapp.tasks.controllers import taskRoute

app = Flask(__name__)
app.register_blueprint(taskRoute) #registra la ruta, definimos las rutas a donde el usuario quisiere entrar

#app.debug = True
app.config.from_object(DevConfig)


@app.route('/')#esta es la ruta más global de nuestro proyecto, la ruta raiz
def hello_world() -> str:
    return ' Hello world'
