from time import sleep

from schemas import CertificateSchema

def enviar_certificado(schema: CertificateSchema):
    print('enviando certificado')
    sleep(3)

def enviar_notificacao(schema: CertificateSchema):
    print('enviando notificacao')
    sleep(2)

def salvar_dados(schema: CertificateSchema):
    print('salvando dados')
    sleep(3)