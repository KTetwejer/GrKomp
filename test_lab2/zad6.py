import numpy as np
from PIL import Image

def rysuj_wlasne(w, h, grub):
    obraz = np.ones((h, w), dtype=np.uint8)
    for i in range(0, h, grub):
        for j in range(0, w, grub):
            if (i // grub) % 2 == (j // grub) % 2:
                obraz[i:i+grub, j:j+grub] = 0
    return Image.fromarray(obraz.astype(bool))

obraz_wlasny = rysuj_wlasne(200, 200, 20)
obraz_wlasny.show()

'''
Wymagania:

    Parametry wejściowe:
        w: szerokość obrazu.
        h: wysokość obrazu.
        grub: rozmiar pojedynczego kwadratu w szachownicy.
    Wzór:
        Obraz powinien mieć naprzemienne czarne i białe kwadraty o szerokości i wysokości równej grub.
    Typ obrazu:
        Obraz powinien być zapisany w formacie czarno-białym (1).
'''