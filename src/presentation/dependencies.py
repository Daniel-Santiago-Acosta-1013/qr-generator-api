from infrastructure.repositories.file_qr_code_repository import FileQRCodeRepository
from infrastructure.services.qr_generator_service import QRGeneratorService

def get_qr_repository():
    return FileQRCodeRepository()

def get_qr_generator():
    return QRGeneratorService()
    