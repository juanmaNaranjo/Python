import barcode
from barcode import generate
from barcode.writer import ImageWriter
from barcode import get_barcode_class
from PIL import Image
import cv2
import numpy as np

# Generar un código de barras
def generar_codigo_de_barras(data, formato='code128'):
    code_class = get_barcode_class(formato)
    codigo = code_class(data, writer=ImageWriter(), add_checksum=False)
    codigo.save('codigo_de_barras')

# Leer un código de barras desde una imagen
def leer_codigo_de_barras(imagen):
    imagen = cv2.imread(imagen)
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    detector = cv2.QRCodeDetector()
    valor, puntos, qr_code = detector.detectAndDecodeMulti(gray)
    if valor:
        return valor
    else:
        return "Código de barras no encontrado."

# Generar un código de barras
data = "123456789"  # Cambia esto por el valor que desees codificar
generar_codigo_de_barras(data)

# Leer el código de barras generado
codigo_leido = leer_codigo_de_barras('codigo_de_barras.png')

if codigo_leido:
    print("Código de barras leído:", codigo_leido)
else:
    print("No se pudo leer el código de barras.")
