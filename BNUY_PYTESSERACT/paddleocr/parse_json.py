import json

def parse_ocr_json(json_file_path):
    """Parse OCR JSON output and extract only the text."""
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Extract text from rec_texts field
        rec_texts = data.get('rec_texts', [])
        rec_scores = data.get('rec_scores', [])
        
        # Filter out empty text and low confidence results
        extracted_text = []
        for i, text in enumerate(rec_texts):
            if text.strip() and rec_scores[i] > 0.5:  # Only include text with confidence > 0.5
                extracted_text.append(text.strip())
        
        return extracted_text
    
    except FileNotFoundError:
        print(f"Error: File '{json_file_path}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{json_file_path}'.")
        return []
    except Exception as e:
        print(f"Error: {str(e)}")
        return []

def main(file_paths):
    # Parse the JSON file
    json_file = file_paths
    texts = parse_ocr_json(json_file)
    
    if texts:
        print("Extracted text:")
        print("-" * 40)
        for text in texts:
            print(text)
        print("-" * 40)
        print(f"Total lines: {len(texts)}")
        
        # Join all text into a single string
        full_text = " ".join(texts)
        print(f"\nFull text: {full_text}")
    else:
        print("No text found or error occurred.")
main("output/pulchra_base1_res.json")