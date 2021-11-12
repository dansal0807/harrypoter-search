from app import app
from app.models import User, Busca

@app.shell_context_processor
def make_shell_context():
    return {'User': User}

@app.shell_context_processor_busca
def make_shell_context_busca():
    return {'Busca': Busca}