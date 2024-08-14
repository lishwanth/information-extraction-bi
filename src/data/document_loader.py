import pytesseract
from pdf2image import convert_from_path
from PIL import Image

class DocumentLoader:
    def load_pdf(self, file_path):
        images = convert_from_path(file_path)
        texts = [pytesseract.image_to_string(image) for image in images]
        return "\n".join(texts)

    def load_image(self, file_path):
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        return text
