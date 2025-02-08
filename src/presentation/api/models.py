from pydantic import BaseModel

class QRGenerateRequest(BaseModel):
    data: str

class QRUrlResponse(BaseModel):
    qr_url: str