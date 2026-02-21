from paddleocr import PaddleOCR

ocr = PaddleOCR(
    lang="en", # Specify English recognition model with the lang parameter
    use_doc_orientation_classify=False, # Disable document orientation classification model
    use_doc_unwarping=False, # Disable text image unwarping model
    use_textline_orientation=False, # Disable text line orientation classification model
)
result = ocr.predict("pulchra_base1.png")
for res in result:
    res.print()
    res.save_to_img("output")
    res.save_to_json("output")