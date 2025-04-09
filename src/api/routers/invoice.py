import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from src.parsers.extract_text import extract_text_from_pdf, extract_text_from_docx

router = APIRouter(prefix="/invoice", tags=["invoice"])


@router.post("/invoice/upload")
async def upload_invoice(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    try:
        if file.content_type == "application/pdf":
            text = extract_text_from_pdf(file_path)
        elif file.content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            text = extract_text_from_docx(file_path)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")
        os.remove(file_path)
        print(text)
        return {"text": text}
    except Exception as e:
        os.remove(file_path)
        raise HTTPException(status_code=500, detail=str(e))
