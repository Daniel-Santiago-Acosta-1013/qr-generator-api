from abc import ABC, abstractmethod

class QRCodeRepository(ABC):
    @abstractmethod
    def save(self, data: bytes) -> str:
        pass
    
    @abstractmethod
    def get_path(self, qr_id: str) -> str:
        pass