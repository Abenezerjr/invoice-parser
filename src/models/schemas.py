#
# from pydantic import BaseModel
# from typing import List, Dict, Optional
#
#
# # class InvoiceData(BaseModel):
#     invoice_number: str
#     date: str
#     total_amount: float
#     items: List[Dict[str, str]]
#
#
# class SourceDocumentResponse(BaseModel):
#     id: int
#     title: str
#     doc_hash: str
#     size: int
#     total_pages: Optional[int] = None
#     status: Optional[str] = None
#     embedded: Optional[bool] = None
#
#     class Config:
#         orm_mode = True  # Enable ORM mode for SQLAlchemy compatibility
