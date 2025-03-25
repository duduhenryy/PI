import cv2
import numpy as np
import matplotlib.pyplot as plt

imagem = cv2.imread("tarefa8/sources/exemplo.jpg", 0)

# criação de uma matriz 2x2 composta por "uns", que será o kernel (operador morfológico) a ser passado na imagem para
kernel = np.ones((2,2), np.uint8)

# o gradiemte morfológico é a diferença entre a dilatação (contorno da imagem fica mais grosso) e a erosão (contorno da imagem fica
# mais fino) da imagem, dessa forma sendo útil para realçar contornos da imagem
gradiente = cv2.morphologyEx(imagem, cv2.MORPH_GRADIENT, kernel)

imagens = [imagem, gradiente]
titulos = ["Original", "Bordas"]

plt.figure(figsize=(10, 8))
for i, (img, title) in enumerate(zip(imagens, titulos)):
    plt.subplot(2, 2, i + 1)
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.axis('off')
plt.tight_layout()
plt.show()
