from fastapi import APIRouter, Depends, HTTPException
from app.api import deps
from app.core.supabase import supabase_client
from app.core.config import settings
from app.schemas.UploadSchema import UploadSignRequest, UploadSignResponse
from datetime import datetime
import uuid

router = APIRouter()

@router.post("/sign", response_model=UploadSignResponse)
async def get_signed_url(
    data: UploadSignRequest,
    current_user = Depends(deps.get_current_empleado) # Seguridad integrada 
):
    if data.entity_type not in ["lectura", "corte"]:
        raise HTTPException(status_code=400, detail="Entidad no soportada")

    now = datetime.now()
    filename = f"{uuid.uuid4()}.{data.extension}"
    object_path = f"{data.entity_type}s/{now.year}/{now.month:02d}/{filename}"

    try:
        # Generar URL temporal de subida válida por 15 minutos [cite: 137, 138]
        res = supabase_client.storage.from_(settings.SUPABASE_BUCKET).create_signed_upload_url(object_path)
        
        return {
            "bucket": settings.SUPABASE_BUCKET,
            "object_path": object_path,
            "signed_upload_url": res['signed_url'],
            "public_url": f"{settings.SUPABASE_URL}/storage/v1/object/public/{settings.SUPABASE_BUCKET}/{object_path}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))