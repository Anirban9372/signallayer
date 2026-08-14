from pathlib import Path  # best pathway manager
import sys
import os

try:
    # main class it allows to read documents
    from docling.document_converter import DocumentConverter
except ImportError:
    # If docling is not in the current environment, try to load it from the venv
    # We assume the venv is located at ../venv relative to this file
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    venv_site_packages = os.path.join(
        base_path, 'venv', 'lib', f'python{sys.version_info.major}.{sys.version_info.minor}', 'site-packages')
    if os.path.exists(venv_site_packages):
        sys.path.insert(0, venv_site_packages)
        from docling.document_converter import DocumentConverter
    else:
        # If we still can't find it, re-raise the exception to alert the user
        raise


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

    def parse_pdf(self, pdf_path: str) -> str:
        """
        Parse a BSE PDF and return clean markdown text.

        Args:
            pdf_path: Path to the PDF file.

        Returns:
            Markdown string with tables and headings preserved.

        Raises:
            FileNotFoundError: If the PDF does not exist.
            ValueError: If the file is not a PDF.
        """
        path = Path(pdf_path)

        if not path.exists():
            raise FileNotFoundError(f"PDF not found: {pdf_path}")

        if path.suffix.lower() != ".pdf":
            raise ValueError(f"Expected .pdf file, got: {path.suffix}")

        result = self.converter.convert(str(path))
        return result.document.export_to_markdown()


def extract_tables(self, pdf_path: str) -> list[str]:
    """
    Extract only the tables from a BSE PDF.

    BSE announcements contain key financial data in tables:
    quarterly results, shareholding patterns, dividend details.
    This method isolates just those tables for targeted analysis.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        List of tables as markdown strings. Empty list if no tables.
    """
    path = Path(pdf_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    result = self.converter.convert(str(path))

    tables = []
    for table in result.document.tables:
        tables.append(table.export_to_dataframe().to_markdown())

    return tables
