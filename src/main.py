from fastapi import FastAPI
from src.presentation.api.routers.qr import router as qr_router

app = FastAPI()
app.include_router(qr_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)