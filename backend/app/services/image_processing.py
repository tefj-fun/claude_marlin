from PIL import Image
from io import BytesIO

def load_image(data: bytes) -> Image.Image:
    return Image.open(BytesIO(data))
