from pydantic import BaseModel
from typing import List, Optional


class Address(BaseModel):
    street: Optional[str]
    city: Optional[str]
    state: Optional[str]
    postal_code: Optional[str]
    country: Optional[str]


class PaymentMethod(BaseModel):
    type: str
    details: Optional[dict]
    instructions: Optional[str]


class InvoiceItem(BaseModel):
    description: str
    quantity: float
    unit_price: float
    amount: float
    period: Optional[str]


class TaxDetail(BaseModel):
    name: str
    rate: str
    amount: float


class TaxSummary(BaseModel):
    subtotal: float
    total_excluding_tax: float
    taxes: List[TaxDetail]
    total: float


class InvoiceResponse(BaseModel):
    invoice: dict
    issuer: dict
    recipient: dict
    items: List[InvoiceItem]
    tax_summary: TaxSummary
    notes: List[str]
    pages: int
