import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

# filtro passa baixa
def filtro_passa_baixa(image, kernel_size=5):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigmaX=0)

# filtro passa alta
def filtro_passa_alta(image):
    laplacian = cv2.Laplacian(image, 3)
    laplacian = cv2.convertScaleAbs(laplacian)
    return laplacian

# combinação dos filtros
def aprimora_imagem(image, kernel_size_baixa=5):
    baixa = filtro_passa_baixa(image, kernel_size_baixa)
    alta = filtro_passa_alta(image)
    return cv2.addWeighted(baixa, 0.5, alta, 0.5, 0)

def mostrar_imagens(image):
    
    kernel_size_baixa = 5
    baixa = filtro_passa_baixa(image, kernel_size_baixa)
    alta = filtro_passa_alta(image)
    aprimorada = aprimora_imagem(image, kernel_size_baixa)

    titles = ["Original", "Passa-Baixa", "Passa-Alta (Laplaciano)", "Aprimorada"]
    images = [image, baixa, alta, aprimorada]

    plt.figure(figsize=(10, 8))
    for i, (img, title) in enumerate(zip(images, titles)):
        plt.subplot(2, 2, i + 1)
        plt.imshow(img, cmap='gray')
        plt.title(title)
        plt.axis('off')
    plt.tight_layout()
    plt.show()


    # cria uma interface gráfica com um botão para carregar imagens. usa filedialog.askopenfilename para abrir um seletor de arquivos e
    # após carregar a imagem, chama a função mostrar_imagens
def interface_grafica():
    def carregar_imagem():
        file_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.jpg *.png *.bmp *.jpeg")])
        if file_path:
            img = cv2.imread(file_path, 0)
            mostrar_imagens(img)

    root = Tk()
    root.title("Aprimoramento de Imagens")

    btn_carregar = filedialog.Button(root, text="Carregar Imagem", command=carregar_imagem)
    btn_carregar.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    interface_grafica()
