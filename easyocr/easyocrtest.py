import easyocr

# Purely using easyocr
print("Loading EasyOCR model...")
reader = easyocr.Reader(['en','en'])  # Only need 'en' once

print("Processing image...")
result = reader.readtext('pulchra_base1.png')

print("Results:")
for (bbox, text, confidence) in result:
    print(f"Text: {text} (Confidence: {confidence:.2f})")