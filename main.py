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

    enviar_certificado.delay(schema.model_dump())
    enviar_notificacao.delay(schema.model_dump())
    salvar_dados.delay(schema.model_dump())

    data_retorno = {
        "status": "true",
        "message": "Certificado gerado com sucesso!",
        "data": schema.model_dump()
    },

    return JSONResponse(content=data_retorno, status_code= status.HTTP_201_CREATED)