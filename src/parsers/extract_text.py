import os, re

from PyPDF2 import PdfReader
from docx import Document


def extract_text_from_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""

    # Extract text from each page
    for page in reader.pages:
        page_text = page.extract_text() or ""
        text += page_text

    # Clean the text
    text = text.replace("\u0000", "")  # Remove null characters
    # Remove single spaces between characters within words
    text = re.sub(r'(?<=\S)\s(?=\S)', '', text)  # Remove space between non-space characters
    # Normalize remaining spaces (e.g., multiple spaces to one)
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def extract_text_from_docx(file_path: str) -> str:
    doc = Document(file_path)
    text = ""

    # Extract text from paragraphs with proper newlines
    for para in doc.paragraphs:
        text += para.text + "\n"

    # Clean the text
    text = text.replace("\u0000", "")  # Remove null characters
    # Remove single spaces between characters within words
    text = re.sub(r'(?<=\S)\s(?=\S)', '', text)  # Remove space between non-space characters
    # Normalize remaining spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text
