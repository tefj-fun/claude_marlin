from fastapi import APIRouter, File, UploadFile
from ..services.ml_detection import detect_objects
from ..models.detection import DetectionResponse

router = APIRouter()

@router.post('', response_model=DetectionResponse)
async def detect(image: UploadFile = File(...)):
    data = await image.read()
    detections = detect_objects(data)
    return {'filename': image.filename, 'detections': detections}
