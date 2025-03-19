from pydantic import BaseModel

class CertificateSchema(BaseModel):
    name: str
    email: str
    course: str