from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from controller import enviar_certificado, enviar_notificacao, salvar_dados
from schemas import CertificateSchema

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/chamando-rabbit")
def read_root(schema: CertificateSchema):

    enviar_certificado(schema)
    enviar_notificacao(schema)
    salvar_dados(schema)

    data_retorno = {
        "status": "true",
        "message": "Certificado gerado com sucesso!",
        "data": schema.model_dump()
    },

    return JSONResponse(content=data_retorno, status_code= status.HTTP_201_CREATED)