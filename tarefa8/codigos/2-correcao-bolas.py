import cv2
import numpy as np
import matplotlib.pyplot as plt

bolas = cv2.imread("tarefa8/sources/bolas.png", 0)

kernel = np.array([[0,1,0],
                    [1,1,1],
                    [0,1,0]], np.uint8)

bolasErode = cv2.erode(bolas, kernel, iterations=3)
bolasDilate = cv2.dilate(bolasErode, kernel, iterations=5)
filtro_mediana = cv2.medianBlur(bolas, 5)

imagens = [bolas, bolasErode, bolasDilate, filtro_mediana]
titulos = ["Original", "Erosão", "Dilatação", "Teste com o filtro da mediana"]

plt.figure(figsize=(10, 8))
for i, (img, title) in enumerate(zip(imagens, titulos)):
    plt.subplot(2, 2, i + 1)
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.axis('off')
plt.tight_layout()
plt.show()
