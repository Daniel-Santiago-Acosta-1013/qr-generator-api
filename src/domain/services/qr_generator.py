from abc import ABC, abstractmethod

class QRGenerator(ABC):
    @abstractmethod
    def generate(self, data: str) -> bytes:
        pass