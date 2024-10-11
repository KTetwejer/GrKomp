import numpy as np
from PIL import Image

tablica = np.loadtxt('tablica.txt', dtype=np.uint8)
obraz = Image.fromarray(tablica * 255).convert('1')

def rysuj_ramke_w_obrazie(obraz, grub):
    tab_obraz = np.asarray(obraz).astype(np.uint8)
    h, w = tab_obraz.shape
    tab_obraz[:grub, :] = 0
    tab_obraz[-grub:, :] = 0
    tab_obraz[:, :grub] = 0
    tab_obraz[:, -grub:] = 0
    tab = tab_obraz.astype(bool)
    return Image.fromarray(tab)

obraz_z_ramka = rysuj_ramke_w_obrazie(obraz, 5)
'''
zakładam, że chodzi o plik tablica.txt z pierwszych ćwiczeń, utworzony na podstawie pliku z inicjałami
jako że tamten plik ma wielkość 100x50, ramka de facto sprawia, że cały obraz jest czarny
pozwoliłem więc sobie zmodyfikować grubość z 50 na 5 (kod działa w obu wersjach)
'''

obraz_z_ramka.show()
