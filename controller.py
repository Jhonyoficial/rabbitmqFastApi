from time import sleep


from celery import Celery
from schemas import CertificateSchema

redis_url = "amqp://guest:guest@localhost:5672//"
app = Celery(__name__, broker=redis_url)

@app.task(name="certificado")
def enviar_certificado(schema: CertificateSchema):
    nome = schema.get('name')
    print(f'enviando certificado para {nome}')
    sleep(3)

@app.task(name="tasks.enviar_certificado")
def enviar_notificacao(schema: CertificateSchema):
    print('enviando notificacao')
    sleep(2)

@app.task(name="tasks.salvar_dados")
def salvar_dados(schema: CertificateSchema):
    print('salvando dados')
    sleep(3)