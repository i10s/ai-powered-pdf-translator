
# PDF to Word Translator

An AI-powered tool to translate PDF documents into Spanish (or other languages) and save them as Word files, preserving the original formatting. This project uses OpenAI's GPT-4 model for high-quality translations and supports incremental saving to avoid data loss.

---

## Features

- Extracts text from PDF files, preserving paragraphs.
- Translates text to Spanish using OpenAI's GPT-4.
- Exports translated text to a Word file with formatting intact.
- Handles large files with incremental saving to avoid data loss.
- Automatically pauses to respect OpenAI's requests per minute (TPM) limits.
- Resilient error handling for uninterrupted translation.

---

## Prerequisites

- Python 3.8 or higher
- OpenAI API key (you can obtain it from [OpenAI's website](https://platform.openai.com/))
- Libraries:
  - `openai`
  - `PyPDF2`
  - `python-docx`

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/pdf-to-word-translator.git
   cd pdf-to-word-translator
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/MacOS
   .\venv\Scripts\activate   # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

1. Set your OpenAI API key:
   Open the script `app.py` and replace the placeholder in the line below with your OpenAI API key:
   ```python
   openai.api_key = "your-api-key-here"
   ```

---

## Usage

1. Place the PDF file you want to translate in the project directory.

2. Run the script:
   ```bash
   python app.py
   ```

3. The script will:
   - Extract text from the PDF.
   - Translate the text paragraph by paragraph into Spanish.
   - Save the translated text incrementally to `output.docx`.

4. The translated Word document will be saved as `output.docx` in the project directory.

---

## Example Output

- **Input PDF**: A file with English text and clear paragraph breaks.
- **Output Word File**: A translated document in Spanish, preserving the original structure and formatting.

---

## Roadmap

- Add support for translating into multiple languages.
- Enable the processing of PDFs with images and tables.
- Provide a web-based interface for easier use.
- Add support for batch processing of multiple PDFs.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add a new feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or feedback, feel free to reach out:

- **Email**: [your-email@example.com](mailto:your-email@example.com)
- **GitHub Issues**: [Open an issue](https://github.com/<your-username>/pdf-to-word-translator/issues)
