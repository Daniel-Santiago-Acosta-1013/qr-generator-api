# QR Generator API - Modo de Ejecución  
  
## Requisitos  
- Python 3.8+  
  
## Instalación  
1. Clona el repositorio.  
2. Crea y activa el entorno virtual:  
```bash  
python -m venv venv  
# Windows:  
venv\Scripts\activate  
# Unix/macOS:  
source venv/bin/activate  
```  
3. Instala dependencias:  
```bash  
pip install -r requirements.txt  
```  
  
## Ejecutar el Servidor  
```bash  
uvicorn src.main:app --reload  
```  
  
## Uso  
- **Generar QR**:  
  ```bash  
  curl -X POST "http://localhost:8000/api/generate-qr" -H "Content-Type: application/json" -d '{"data":"<TU_TEXTO_O_URL>"}'  
  ```  
  **Respuesta**: `{"qr_url": "http://localhost:8000/api/qr/<qr_id>"}`  
 
- **Ver QR**:  
  Abre en el navegador la URL devuelta (ej: `http://localhost:8000/api/qr/<qr_id>`).  
 
## Nota  
- Los QR se guardan en `media/qr_codes/`.  
- Para desactivar el entorno virtual, ejecuta:  
```bash  
deactivate  
```  # qr-generator-api
