import easyocr

print("Loading EasyOCR model...")
reader = easyocr.Reader(['en'])

print("Processing image...")
result = reader.readtext(
    'pulchra3.png',
    detail=1,           # Return bounding box coordinates
    width_ths=0.7,      # Text width threshold
    height_ths=0.7,     # Text height threshold
    paragraph=False,    # Don't combine text into paragraphs
    min_size=10,        # Minimum text size
    text_threshold=0.7, # Text confidence threshold
    low_text=0.4,       # Low text threshold
    link_threshold=0.4, # Link threshold
    canvas_size=2560,   # Canvas size for processing
    mag_ratio=1.5       # Magnification ratio
)

print("Results:")
for (bbox, text, confidence) in result:
    if confidence > 0.5:  # Filter low confidence results
        print(f"Text: {text} (Confidence: {confidence:.2f})")