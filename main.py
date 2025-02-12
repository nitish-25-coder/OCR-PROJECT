import cv2
from pytesseract import image_to_string, pytesseract
import json
import psycopg2
import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Preprocess the image to enhance text extraction
def preprocess_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
    
    image = cv2.imread(image_path)
    
    if image is None:
        raise ValueError("Failed to load image. Ensure the file path and format are correct.")
    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
    return threshold_image

# Extract text from the processed image using Tesseract
def extract_text(image_path):
    processed_image = preprocess_image(image_path)
    text = image_to_string(processed_image)
    print("Extracted Text:\n", text)
    return text

# Parse the extracted text into a structured JSON format
def parse_to_json(text):
    lines = text.strip().split("\n")
    data = {
        "patient_name": None,
        "dob": None,
        "treatment_date": None,
        "injection": None,
        "exercise_therapy": None,
        "difficulty_ratings": {},
        "pain_symptoms": {}
    }

    for line in lines:
        line_lower = line.lower()
        if "patient name" in line_lower:
            data["patient_name"] = line.split(":")[-1].strip()
        if "dob" in line_lower:
            data["dob"] = line.split(":")[-1].strip()
        if "injection" in line_lower:
            data["injection"] = "Yes" if "yes" in line_lower else "No"
        if "exercise therapy" in line_lower:
            data["exercise_therapy"] = "Yes" if "yes" in line_lower else "No"
        if "bending" in line_lower:
            data["difficulty_ratings"]["bending"] = int(line[-1]) if line[-1].isdigit() else None
        if "pain" in line_lower and "numbness" not in line_lower:
            data["pain_symptoms"]["pain"] = int(line.split(":")[-1].strip()) if line.split(":")[-1].strip().isdigit() else None
    
    return data

# Save the structured data into a JSON file
def save_json(data, filename="output.json"):
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data saved to {filename}")

# Store data in the PostgreSQL database
def store_data_in_db(data):
    try:
        conn = psycopg2.connect(
            dbname="ocr_database",
            user="postgres",
            password="Nitish@2003",  # Replace with your actual PostgreSQL password
            host="localhost"
        )
        cursor = conn.cursor()

        # Insert patient data
        cursor.execute("INSERT INTO patients (name, dob) VALUES (%s, %s) RETURNING id",
                        (data["patient_name"], data["dob"]))
        patient_id = cursor.fetchone()[0]

        # Insert form JSON data
        cursor.execute("INSERT INTO forms_data (patient_id, form_json) VALUES (%s, %s)",
                        (patient_id, json.dumps(data)))

        conn.commit()
        cursor.close()
        conn.close()
        print("Data stored in the database successfully!")
    except Exception as e:
        print("Error storing data in the database:", e)

# Main function to run the process
def main():
    image_path = "sample_images/patient_form.png"  # Update to your image file
    text = extract_text(image_path)
    data = parse_to_json(text)
    save_json(data)
    store_data_in_db(data)
    print("Process completed successfully!")

if __name__ == "__main__":
    main()
