import cv2
import matplotlib.pyplot as plt

img = cv2.imread("tarefa5/sources/yn.png")
cv2.imshow("Imagem",img)

cores = ('b', 'g', 'r') # representa cada canal
for i, cor in enumerate(cores): # for que repete para cada canal o calculo do histograma
    histograma = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histograma, color = cor) # plota o histograma ja com a cor correta
    plt.xlim([0, 256])

plt.title("Histograma Colorido")
plt.xlabel("Bins")
plt.ylabel("Contagem de Pixels")
plt.show()
