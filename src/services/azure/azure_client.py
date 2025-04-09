from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from src.models.schemas import InvoiceResponse
import json


class AzureInvoiceParser:
    def __init__(self, endpoint: str, key: str):
        self.client = DocumentAnalysisClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(key)
        )

    def analyze_invoice(self, file_bytes: bytes) -> dict:
        poller = self.client.begin_analyze_document(
            "prebuilt-invoice",
            file_bytes
        )
        result = poller.result()

        # Extract and structure data
        invoice_data = {
            "invoice": {
                "invoice_number": result.fields.get("InvoiceId").value,
                "date_of_issue": result.fields.get("InvoiceDate").value.strftime("%B %d, %Y"),
                "date_due": result.fields.get("DueDate").value.strftime("%B %d, %Y"),
                "total_amount": float(result.fields.get("InvoiceTotal").value),
                "currency": result.fields.get("InvoiceTotal").value.currency,
                "payment_status": "due"
            },
            "issuer": {
                "company_name": result.fields.get("VendorName").value,
                "address": self._parse_address(result.fields.get("VendorAddress")),
                "email": result.fields.get("VendorEmail") and result.fields.get("VendorEmail").value
            },
            "items": self._parse_items(result.fields.get("Items")),
            # Add other fields as needed
        }

        return invoice_data

    def _parse_address(self, address_field):
        if not address_field:
            return None
        return {
            "street": address_field.value.get("StreetAddress"),
            "city": address_field.value.get("City"),
            "state": address_field.value.get("State"),
            "postal_code": address_field.value.get("PostalCode"),
            "country": address_field.value.get("CountryRegion")
        }

    def _parse_items(self, items_field):
        if not items_field:
            return []
        return [{
            "description": item.value.get("Description").value,
            "quantity": float(item.value.get("Quantity").value),
            "unit_price": float(item.value.get("UnitPrice").value),
            "amount": float(item.value.get("Amount").value)
        } for item in items_field.value]