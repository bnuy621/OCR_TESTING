from PIL import Image
import pytesseract
#This struggles with basic images. For example, text in a comic like format is ignored.
print(pytesseract.image_to_string(Image.open('pulchra3.png')))
