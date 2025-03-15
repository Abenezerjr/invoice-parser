from fastapi import FastAPI, File, UploadFile, HTTPException
from src.parsers.pdf_parser import parse_invoice_pdf
from src.models.models_db import InvoiceData
import os

app = FastAPI()


@app.post("/parse-invoice/", response_model=InvoiceData)
async def parse_invoice(file: UploadFile = File(...)):

    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    # Parse the invoice
    parsed_data = parse_invoice_pdf(file_path)

    # Clean up the temporary file
    os.remove(file_path)

    # Return the parsed data in JSON format
    return parsed_data
