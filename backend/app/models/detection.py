from typing import List
from pydantic import BaseModel

class Detection(BaseModel):
    label: str
    confidence: float

class DetectionResponse(BaseModel):
    filename: str
    detections: List[Detection]
