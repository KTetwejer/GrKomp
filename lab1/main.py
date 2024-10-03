from PIL import Image
import numpy as np

image1 = Image.open("inicjaly.bmp")
print("Informacje o obrazie:")
print("tryb:", image1.mode)
print("format:", image1.format)
print("rozmiar:", image1.size)

image1.show()