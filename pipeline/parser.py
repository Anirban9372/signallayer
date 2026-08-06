from pathlib import Path

try:
    from docling.document_converter import DocumentConverter
except ImportError:
    class DocumentConverter:  # type: ignore[override]
        def __init__(self, *args, **kwargs):
            raise ImportError(
                "docling is required to use DocumentConverter. Install the 'docling' package."
            ) 