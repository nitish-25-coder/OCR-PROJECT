# OCR-Based Patient Assessment Form Data Extraction

## Project Overview
This project automates the extraction of data from scanned patient assessment forms using **Optical Character Recognition (OCR)** and stores the structured data in a **MySQL database**. The extracted information is formatted into **JSON** for easy processing and retrieval.

## Key Features
- Extract text from scanned **JPEG/PDF** patient forms using **Tesseract OCR**
- Preprocess images to improve OCR accuracy
- Parse and structure extracted text into **JSON format**
- Store structured data in a **MySQL database**
- Support both **printed and handwritten text recognition**
- Provide a **GitHub repository** with well-documented code for easy deployment

## Technologies Used
- **Python** (Main scripting language)
- **Tesseract OCR** (Text extraction)
- **OpenCV** (Image preprocessing)
- **Pillow (PIL)** (Image handling)
- **pdf2image** (PDF to image conversion)
- **MySQL** (Database for structured data storage)
- **VS Code** (Development environment)

## Installation & Setup
### 1. Clone the Repository
```sh
git clone <repository-url>
cd OCR-MySQL-Project
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. Configure MySQL Database
1. Open MySQL terminal and run the following commands:
```sql
CREATE DATABASE ocr_data;
USE ocr_data;
```
2. Create necessary tables:
```sql
CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    dob DATE
);

CREATE TABLE forms_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    form_json JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(id)
);
```

### 4. Run the OCR Script
```sh
python ocr_script.py
```

## Project Workflow
1. User provides a scanned **patient assessment form** (JPEG/PDF).
2. OCR extracts text from the document after **preprocessing**.
3. Extracted text is **parsed and structured** into a JSON format.
4. Data is **inserted into a MySQL database** for storage.
5. Stored data can be **retrieved for further processing or analysis**.

## Expected JSON Output
```json
{
  "patient_name": "John Doe",
  "dob": "01/05/1988",
  "date": "02/06/2025",
  "injection": "Yes",
  "exercise_therapy": "No",
  "difficulty_ratings": {
    "bending": 3,
    "putting_on_shoes": 1,
    "sleeping": 2
  },
  "pain_symptoms": {
    "pain": 2,
    "numbness": 5,
    "tingling": 6
  },
  "medical_assistant_data": {
    "blood_pressure": "120/80",
    "hr": 80,
    "weight": 67,
    "height": "5'7",
    "spo2": 98
  }
}
```

## Future Enhancements
- Improve OCR accuracy for **handwritten forms**
- Develop a **Flask/Django API** for web-based form uploads
- Deploy the project as a **cloud-based service**
- Enhance **database structure** for scalability

## License
This project is open-source and available under the **MIT License**.

---

This README provides complete guidance for setting up, running, and understanding the project. Let me know if you need modifications! 🚀

