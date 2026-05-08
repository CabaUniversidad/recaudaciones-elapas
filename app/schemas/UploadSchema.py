from pydantic import BaseModel
from uuid import UUID

class UploadSignRequest(BaseModel):
    entity_type: str  # "lectura" o "corte"
    extension: str    # "jpg" o "png"

class UploadSignResponse(BaseModel):
    bucket: str
    object_path: str
    signed_upload_url: str
    public_url: str

class PhotoPathUpdate(BaseModel):
    foto_url: str