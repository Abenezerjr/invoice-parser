from langchain.document_loaders import PyPDFLoader
from langchain.chains import LLMChain
import json
from langchain.prompts import PromptTemplate
from langchain.llms import Ollama  # Use Ollama for local LLM
from src.models.models_db import InvoiceData


def parse_invoice_pdf(file_path: str) -> InvoiceData:
    """
    Parse an invoice PDF using a local LLM (Ollama) and LangChain.
    """
    # Step 1: Load the PDF
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    text = "\n".join([page.page_content for page in pages])

    # Step 2: Use LangChain with Ollama to extract structured data
    llm = Ollama(model="mistral")  # Use a local LLM via Ollama

    prompt = PromptTemplate(
        input_variables=["text"],
        template="""
        Extract the following fields from the invoice text:
        - Invoice Number
        - Date
        - Total Amount
        - Items (Description, Quantity, Price)

        Invoice Text:
        {text}

        Return the result as a JSON object.
        """
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run(text)

    # Parse the JSON result into an InvoiceData object

    parsed_data = json.loads(result)
    return InvoiceData(**parsed_data)
