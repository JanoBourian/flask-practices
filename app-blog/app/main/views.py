from . import main 

@main.route("/", methods=['GET', 'POST'])
def index():
    return "<h1> Hola Pelona </h1>"