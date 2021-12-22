import pytesseract
import slither_api
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
def read(image):
    text  = pytesseract.image_to_string(image)
    return text

