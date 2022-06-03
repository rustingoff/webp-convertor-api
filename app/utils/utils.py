from PIL import Image
from io import BytesIO


def webp_converter(file: bytes) -> Image:
    with BytesIO(file) as img:
        original_image = Image.open(img)
        original_image = original_image.convert('RGB')
        converted_image = BytesIO()
        original_image.save(converted_image, "webp")
        converted_image.seek(0)

        return converted_image
