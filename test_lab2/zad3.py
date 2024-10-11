from PIL import Image
import numpy as np

def rysuj_paski_pionowe(w, h, grub):
    obraz = np.ones((h, w), dtype=np.uint8)
    for j in range(0, w, 2 * grub):
        obraz[:, j:j+grub] = 0
    return Image.fromarray(obraz.astype(bool))

obraz_paski = rysuj_paski_pionowe(200, 100, 10)

bmp_path = 'obraz_paski.bmp'
obraz_paski.save(bmp_path)


jpeg_path = 'obraz_paski.jpg'
obraz_jpeg = Image.open(jpeg_path)

tryb_obrazu = obraz_jpeg.mode
wartosc_piksela = obraz_jpeg.getpixel((66, 13))  # Wartość piksela na pozycji (66, 13)
tablica = np.asarray(obraz_jpeg)
wartosc_elementu_tablicy = tablica[20, 97]  # Wartość elementu tablicy na pozycji (20, 97)

info = f"{tryb_obrazu}; {wartosc_piksela}; {wartosc_elementu_tablicy}"
print(info)
