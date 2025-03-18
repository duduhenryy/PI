import cv2
import numpy as np
import matplotlib.pyplot as plt

# eq. de histograma: melhora o contraste de uma imagem ajustando a distribuição dos seus pixels, de forma uniforme ao longo de todo
# espectro de níveis de cinza. A equalização utiliza a função de distribuição acumulada (Cumulative Distribution Function - CDF) 
# para redistribuir os valores de intensidade. A CDF mapeia os valores de intensidade originais para novos valores proporcionais à 
# sua posição acumulada no histograma. A teoria matemática por trás baseia-se em transformar a distribuição dos níveis de intensidade 
# dos pixels de uma imagem de forma que a densidade probabilística do histograma seja redistribuída de maneira mais uniforme

def plotar_histograma(image, title, color):
    plt.hist(image.ravel(), bins=256, range=[0, 256], color=color)
    
    # ravel: transforma a matriz bidimensional da imagem em um vetor 1D com H x W elementos. Isso permite que o plt.hist() conte a
    # frequência de cada nível de intensidade (de 0 a 255).
    
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("Contagem de Pixels")
    plt.grid()

img = cv2.imread("pi/pi/tarefa6/exWiki.jpg", 0)
img_equalizada = cv2.equalizeHist(img)

# cria uma única figura 
plt.figure(figsize=(12, 6))

# imagem original
plt.subplot(2, 2, 1) # cria um subplot 2x2 e seleciona o primeiro espaço
plt.imshow(img, cmap='gray')
plt.title("Imagem Original")
plt.axis("off")

# histograma da imagem original
plt.subplot(2, 2, 2)
plotar_histograma(img, "Histograma Original", "blue")

# imagem equalizada
plt.subplot(2, 2, 3)
plt.imshow(img_equalizada, cmap='gray')
plt.title("Imagem Equalizada")
plt.axis("off")

# histograma da imagem equalizada
plt.subplot(2, 2, 4)
plotar_histograma(img_equalizada, "Histograma Equalizado", "green")
plt.tight_layout()
plt.show()

cv2.imwrite("imagem_equalizada.jpg", img_equalizada)
