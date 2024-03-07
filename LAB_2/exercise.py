import matplotlib.pyplot as plt
import cv2
import random
import numpy as np
import scipy as scp


def load_image(path):
    image = cv2.imread(path)
    #cv2.imshow('image.png', image)
    #cv2.waitKey(0)  # Dodaj to aby okno z obrazem zostało pokazane
    return image

def save_image(image):
    cv2.imwrite("image.png", image)

def zad_1(path = "pictures/image.png"):
    """
    Zad. 1 Korzystając z jednej z dostępnych bibliotek (np. OpenCV) przygotuj kod w języku Python,
    który załaduje a następnie zapisze wybrany obraz z/na dysku.
    """
    image = load_image(path)
    save_image(image)

def zad_2(path="pictures/image.png"):
    """
    Zad. 2 Przygotuj w języku Python kod, który wygeneruje histogram dla załadowanego obrazu
    z zadania 1.
    """
    image = load_image(path)
    n = 256
    plt.hist(image.ravel(), n, [0, n])
    # make hist into plot histogram
    plt.show()

def zad_3(path="pictures/image.png", number_of_pixels = 350000):
    """
    Zad. 3 Przygotuj w języku Python kod,
    który wygeneruje i zwizualizuje szum „sól i pieprz”
    """
    # Wczytanie obrazu
    image = load_image(path)

    # Zbieranie wymiarów zdjęcia
    row, col, z = image.shape

    for i in range(number_of_pixels):
        # Wybranie koordynatów
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        # Pokolorowanie piksela na biało
        image[y_coord][x_coord] = 255

    for i in range(number_of_pixels):

        # Wybranie koordynatów
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)

        # Pokolorowanie piksela na czarno
        image[y_coord][x_coord] = 0
    save_image(image)

def zad_4(path="pictures/image.png"):
    """
    Zad. 4 Przygotuj w języku Python kod, który obróci załadowany w zadaniu 1 obraz o 90
    stopni
    """
    image = load_image(path)
    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    save_image(image)

def zad_5(path="pictures/image.png"):
    """
    Zad. 5 Przygotuj w języku Python kod, który wygeneruje szum Riciana, Poissona i Rayleigha.
    Dla każdego z tych szumów przygotuj histogram. W tym celu wykorzystaj odpowiednie
    biblioteki w języku Python.
    """
    image = load_image(path)

    fig, ax = plt.subplots(4)
    ax[0].hist(image.ravel(), 256, (0, 256))
    ax[0].set_title('Oryginalny obraz')

    # Riciana
    mean = 0
    sigma = 0.1
    noise = scp.stats.rice.rvs(mean, sigma, image.shape)
    image_c = image + noise
    ax[1].hist(image_c.ravel(), 256, (0, 256))
    ax[1].set_title('Szum Riciana')

    # Poissona
    noise = scp.stats.poisson.rvs(2, size=image.shape)
    image_c = image + noise
    ax[2].hist(image_c.ravel(), 256, (0, 256))
    ax[2].set_title('Szum Poissona')

    # Rayleigha
    noise = scp.stats.rayleigh.rvs(2, size=image.shape)
    image_c = image + noise
    ax[3].hist(image_c.ravel(), 256, (0, 256))
    ax[3].set_title('Szum Rayleigha')

    plt.tight_layout()
    plt.show()


    print("Zadanie 5 wykonane")


if __name__ == "__main__":
    zad_3()