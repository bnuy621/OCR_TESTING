import easyocr
import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

def preprocess_image(image_path):
    # Load image
    img = cv2.imread(image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply noise reduction
    denoised = cv2.medianBlur(gray, 3)
    
    # Apply sharpening
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpened = cv2.filter2D(denoised, -1, kernel)
    
    # Apply threshold to get binary image
    _, thresh = cv2.threshold(sharpened, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    return thresh

print("Loading EasyOCR model...")
reader = easyocr.Reader(['en','en'])

print("Preprocessing image...")
processed_img = preprocess_image('../pulchra3.png')

print("Processing image...")
result = reader.readtext(processed_img)

print("Results:")
for (bbox, text, confidence) in result:
    print(f"Text: {text} (Confidence: {confidence:.2f})")