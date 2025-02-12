CREATE DATABASE ocr_database;

\c ocr_database

CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob DATE
);

CREATE TABLE forms_data (
    id SERIAL PRIMARY KEY,
    patient_id INT REFERENCES patients(id),
    form_json JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);
