from PIL import Image
import numpy as np


# 1.
def rysuj_ramke_w_obrazie(obraz, grub):

    tab_obraz = np.asarray(obraz).astype(np.uint8)

    h, w = tab_obraz.shape

    tab_obraz[:grub, :] = 0
    tab_obraz[-grub:, :] = 0

    tab_obraz[:, :grub] = 0
    tab_obraz[:, -grub:] = 0

    tab = tab_obraz.astype(bool)
    return Image.fromarray(tab)


# 2.1
def rysuj_ramki(w, h, grub):
    obraz = np.ones((h, w), dtype=np.uint8)
    current_color = 0
    for i in range(0, min(h, w) // 2, grub):
        obraz[i:h - i, i:w - i] = current_color
        current_color = 1 - current_color

    return Image.fromarray(obraz.astype(bool))


# 2.2
def rysuj_pasy_pionowe(w, h, grub):
    obraz = np.ones((h, w), dtype=np.uint8)
    for j in range(0, w, 2 * grub):
        obraz[:, j:j + grub] = 0

    return Image.fromarray(obraz.astype(bool))

def rysuj_wlasne(w, h, grub):
    obraz = np.ones((h, w), dtype=np.uint8)

    #rysowanie szachownicy o kwadratowych polach o szerokości 'grub'
    for i in range(0, h, 2 * grub):
        for j in range(0, w, 2 * grub):
            obraz[i:i + grub, j:j + grub] = 0
            if j + 2 * grub < w:
                obraz[i + grub:i + 2 * grub, j + grub:j + 2 * grub] = 0

    return Image.fromarray(obraz.astype(bool))


# 1. Dodanie ramki do obrazu
image = Image.new('1', (100, 50), color=1)  # Tworzenie pustego białego obrazu
ramka_image = rysuj_ramke_w_obrazie(image, 5)
ramka_image.show()

# 2. Tworzenie obrazu z naprzemiennymi ramkami
ramki_image = rysuj_ramki(100, 50, 5)
ramki_image.show()

# 3. Tworzenie obrazu z pionowymi pasami
pasy_image = rysuj_pasy_pionowe(100, 50, 10)
pasy_image.show()

#Tworzenie obrazu według własnych założeń (szachownica)
wlasny_image = rysuj_wlasne(100, 50, 10)
wlasny_image.show()
