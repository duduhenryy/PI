import cv2
import numpy as np

img = cv2.imread('tarefa4/yn.png')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define o intervalo de cor para a pele em HSV
lower_skin = np.array([0, 20, 70])
upper_skin = np.array([20, 255, 255])

# cria uma máscara onde os pixels dentro do intervalo de cor da pele são brancos, e o restante é preto
mask = cv2.inRange(hsv, lower_skin, upper_skin)

# aplica a máscara para obter a imagem com apenas a pele visível
result = cv2.bitwise_and(img, img, mask=mask)

# exibe a imagem original, a máscara e o resultado final
cv2.imshow("Original Image", img)
cv2.imshow("Mask", mask)
cv2.imshow("Output", result)

# Aguardar até que uma tecla seja pressionada e fechar as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
