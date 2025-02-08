from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import FileResponse
from src.application.use_cases.generate_qr import GenerateQRUseCase
from src.domain.repositories.qr_code_repository import QRCodeRepository
from src.domain.services.qr_generator import QRGenerator
from src.presentation.api.models import QRGenerateRequest, QRUrlResponse
from src.presentation.dependencies import get_qr_repository, get_qr_generator

router = APIRouter()

@router.post("/generate-qr", response_model=QRUrlResponse)
async def generate_qr(
    request: Request,
    data: QRGenerateRequest,
    qr_repository: QRCodeRepository = Depends(get_qr_repository),
    qr_generator: QRGenerator = Depends(get_qr_generator),
):
    use_case = GenerateQRUseCase(qr_generator, qr_repository)
    qr_id = use_case.execute(data.data)
    return {"qr_url": f"{request.base_url}api/qr/{qr_id}"}

@router.get("/qr/{qr_id}")
async def get_qr(
    qr_id: str,
    qr_repository: QRCodeRepository = Depends(get_qr_repository),
):
    try:
        file_path = qr_repository.get_path(qr_id)
        return FileResponse(file_path, media_type="image/png")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="QR no encontrado")