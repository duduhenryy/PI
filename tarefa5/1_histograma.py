import cv2
import numpy as np
import matplotlib.pyplot as plt

imgPB = cv2.imread("tarefa6/yn.png", 0)
img = cv2.imread("tarefa6/yn.png")

cv2.imshow("Imagem Original", img)
cv2.imshow("Imagem em Preto e Branco", imgPB)

histogramaYN= cv2.calcHist([imgPB], [0], None, [256], [0, 256])

# primeiro parametro: lista de imagens de entrada

# segundo parametro: numero de canais de cores para o qual o histograma é calculado. no caso de imagens em tons de cinza, o valor é 0 pq só tem um canal

# terceiro parametro: máscara. definido como None pq não há mascara a ser utilizada

# quarto parametro: numero de bins. um bin é um intervalo de valores de intensidade e cada bin conta o número de pixels na imagem, tendo valores de 
# intensidade nesse intervalo. aqui, é passado 256 e indica que será criado um histograma com 256 bins, variando o valor de intensidade de cada bin de 0 a 255

# quinto parametro: representa o intervalo dos valores de intensidade. como foi passado 0,256 o histograma é calculado para todo o conjunto de cores

plt.figure()
plt.title("Histograma Your Name")
plt.xlabel("Bins")
plt.ylabel(" Contagem de pixels")
plt.plot(histogramaYN)
plt.xlim([0, 256])
plt.show()
