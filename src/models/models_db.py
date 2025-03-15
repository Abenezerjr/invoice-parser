from pydantic import BaseModel
from typing import List, Dict


class InvoiceData(BaseModel):
    invoice_number: str
    date: str
    total_amount: float
    items: List[Dict[str, str]]
