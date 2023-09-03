import pytesseract
from PIL import Image
import PyPDF2  # Biblioteca para lidar com PDFs
from docx import Document


def ocr_image_to_text(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return str(e)


def ocr_pdf_to_text(pdf_path):
    try:
        text = ""
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        return str(e)


def ocr_docx_to_text(docx_path):
    try:
        doc = Document(docx_path)
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    file_path = "imagem_examePNG.png"

    if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        ocr_text = ocr_image_to_text(file_path)
    elif file_path.lower().endswith('.pdf'):
        ocr_text = ocr_pdf_to_text(file_path)
    elif file_path.lower().endswith('.docx'):
        ocr_text = ocr_docx_to_text(file_path)
    else:
        ocr_text = "Tipo de arquivo não suportado para OCR."

    if ocr_text:
        print("Texto extraído:")
        print(ocr_text)
    else:
        print("Não foi possível extrair texto do arquivo.")