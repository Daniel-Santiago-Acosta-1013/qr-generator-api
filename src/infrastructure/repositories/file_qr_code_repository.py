import os
import uuid
from domain.repositories.qr_code_repository import QRCodeRepository

class FileQRCodeRepository(QRCodeRepository):
    def __init__(self, storage_path: str = "media/qr_codes"):
        self.storage_path = storage_path
        os.makedirs(self.storage_path, exist_ok=True)
    
    def save(self, data: bytes) -> str:
        qr_id = str(uuid.uuid4())
        file_path = os.path.join(self.storage_path, f"{qr_id}.png")
        with open(file_path, "wb") as f:
            f.write(data)
        return qr_id
    
    def get_path(self, qr_id: str) -> str:
        file_path = os.path.join(self.storage_path, f"{qr_id}.png")
        if not os.path.exists(file_path):
            raise FileNotFoundError
        return file_path