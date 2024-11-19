import os
import re
from unittest.mock import patch
from app import extract_text_from_pdf, clean_text, translate_text_with_openai, save_paragraph_to_word
from docx import Document


def test_clean_text():
    """
    Test cleaning invalid characters from text.
    """
    raw_text = "Hello\x00World\x1F!"
    cleaned_text = clean_text(raw_text)
    assert cleaned_text == "HelloWorld!", "Invalid characters were not removed"


def test_extract_text_from_pdf(tmp_path):
    """
    Test extracting text from a PDF file.
    """
    from fpdf import FPDF

    # Create a sample PDF file
    pdf_path = tmp_path / "sample.pdf"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, "This is a test.\n\nHere is another paragraph.")
    pdf.output(str(pdf_path))

    # Test the extraction
    paragraphs = extract_text_from_pdf(str(pdf_path))
    assert paragraphs == ["This is a test.", "Here is another paragraph."], "Text extraction failed"


@patch("app.client.chat.completions.create")
def test_translate_text_with_openai(mock_openai):
    """
    Test translation functionality with OpenAI using a mock.
    """
    mock_openai.return_value = {
        "choices": [
            {"message": {"content": "Hola Mundo"}}
        ]
    }
    translated_text = translate_text_with_openai("Hello World")
    assert translated_text == "Hola Mundo", "Translation failed"


def test_save_paragraph_to_word(tmp_path):
    """
    Test saving paragraphs incrementally to a Word document.
    """
    word_path = tmp_path / "output.docx"

    # Save paragraphs to Word
    save_paragraph_to_word("First paragraph.", str(word_path))
    save_paragraph_to_word("Second paragraph.", str(word_path))

    # Verify the content
    doc = Document(word_path)
    paragraphs = [p.text for p in doc.paragraphs]
    assert paragraphs == ["First paragraph.", "Second paragraph."], "Word saving failed"
