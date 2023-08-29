import pytesseract
from PIL import Image


def ocr_image_to_text(image_path):
    try:
        # Abre a imagem usando a biblioteca Pillow (PIL)
        image = Image.open(image_path)

        # Usa o Tesseract para realizar a OCR na imagem e converter em texto
        text = pytesseract.image_to_string(image)

        return text
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    # Caminho da imagem que deseja fazer a OCR
    image_path = "./exame.png"

    # Chama a função de OCR e obtém o texto da imagem
    ocr_text = ocr_image_to_text(image_path)

    if ocr_text:
        print("Texto extraído da imagem:")
        print(ocr_text)
    else:
        print("Não foi possível extrair texto da imagem.")
