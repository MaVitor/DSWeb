import sys
from django.conf import settings
from django.urls import path
from django.http import HttpResponse

# Configuração das definições do Django
settings.configure(
    DEBUG=True,
    SECRET_KEY='segredo',
    ROOT_URLCONF=__name__,
)

# Função que retorna "Hello, World!"
def index(request):
    return HttpResponse('<h1>Hello, World!</h1>')

# Função que retorna "Olá Mundo"
def hello(request):
    return HttpResponse('<h1>Olá Mundo</h1>')

# Função para gerar a tabuada e exibir como tabela HTML
def tabuada(request, numero=5):
    numero = int(numero)
    html = '<h1>Tabuada do {}</h1>'.format(numero)
    html += '<table border="1">'
    for i in range(1, 11):
        html += '<tr>'
        html += '<td>{} x {} = {}</td>'.format(numero, i, numero * i)
        html += '</tr>'
    html += '</table>'
    return HttpResponse(html)

# Definição das rotas
urlpatterns = [
    path('', index),
    path('ola', hello),
    path('tabuada/<int:numero>/', tabuada),
]

# Executa o servidor Django
if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
