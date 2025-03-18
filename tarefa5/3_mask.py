import cv2
import numpy as np

# Carregar a imagem
img = cv2.imread('yn.png')

# Converter para o espaço de cor HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Definir o intervalo de cor para a pele em HSV
# Esses valores podem ser ajustados conforme necessário
lower_skin = np.array([0, 20, 70], dtype=np.uint8)
upper_skin = np.array([20, 255, 255], dtype=np.uint8)

# Criar uma máscara onde os pixels dentro do intervalo de cor da pele são brancos, e o restante é preto
mask = cv2.inRange(hsv, lower_skin, upper_skin)

# Aplicar a máscara para obter a imagem com apenas a pele visível
result = cv2.bitwise_and(img, img, mask=mask)

# Exibir a imagem original, a máscara e o resultado final
cv2.imshow("Original Image", img)
cv2.imshow("Mask", mask)
cv2.imshow("Output", result)

# Aguardar até que uma tecla seja pressionada e fechar as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
