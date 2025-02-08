from pydantic import BaseModel

class QRCode(BaseModel):
    id: str
    data: str