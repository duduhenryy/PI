import cv2
import numpy as np
import matplotlib.pyplot as plt

cervos = cv2.imread("tarefa9/cervos.png", 0)

kernel = np.array([[0,1,0],
                    [1,1,1],
                    [0,1,0]], np.uint8)

#kernel = np.ones((2,2), np.uint8)

# teste com a estratégia de abertura - primeiro a erosao e depois a dilatação. Posteriormente, tentei fazer uma correção fazendo uma
# erosão nova

cervosErode = cv2.erode(cervos, kernel, iterations=3)
cervosDilate = cv2.dilate(cervosErode, kernel= np.ones((2,2), np.uint8), iterations=5)

cervosCorrecao = cv2.erode(cervosDilate, kernel=np.ones((2,2),np.uint8), iterations=5)

filtro_mediana = cv2.medianBlur(cervos, 5)

imagens = [cervosErode, cervosDilate, cervosCorrecao, filtro_mediana]
titulos = ["Erosão", "Dilatação", "Correção", "Teste com o filtro da mediana"]

plt.figure(figsize=(10, 8))
for i, (img, title) in enumerate(zip(imagens, titulos)):
    plt.subplot(2, 2, i + 1)
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.axis('off')
plt.tight_layout()
plt.show()