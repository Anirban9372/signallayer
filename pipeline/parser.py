from pathlib import Path  # best pathway manager
# main class it allows to read documents
from docling.document_converter import DocumentConverter


class BSEparser:
    """
  Converts BSE corporate announcement PDFs into clean markdown.

  Uses docling for layout-preserving extraction — tables, headings,
  and structure are preserved. Critical because BSE announcements
  contain financial tables that must not be garbled.
  """

    def __init__(self):
        """
            Initialize the parser with one DocumentConverter instance.

            We create it here, not inside parse_pdf, because DocumentConverter
            loads ML models on creation — takes 2-3 seconds. Creating it once
            in __init__ means we pay that cost once, not for every PDF.
            """
        self.converter = DocumentConverter()

        def
