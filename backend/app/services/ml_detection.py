import random
from typing import List
from ..models.detection import Detection

LABELS = ["helmet", "goggles", "vest", "gloves", "boots"]


def detect_objects(_: bytes) -> List[Detection]:
    results: List[Detection] = []
    for label in LABELS:
        if random.random() > 0.5:
            results.append(
                Detection(label=label, confidence=round(random.uniform(0.5, 1.0), 2))
            )
    return results
