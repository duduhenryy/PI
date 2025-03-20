import matplotlib.pyplot as plt
import cv2

img = cv2.imread("tarefa1/amor.jpeg")

alt, larg, canais = img.shape  # dimensões da imagem retornadas pelo img.shape
tamanho = img.size  # tamanho total da imagem em bytes - dimensões da imagem * canais
tipo_dado = img.dtype  # tipo de dados para armazenar valores dos pixels
# unit8 - significa unsigned 8-bit integer (inteiro sem sinal de 8 bits). esse tipo de dado pode representar valores de 0 a 255,
# o que é ideal para representar intensidades de cor.

print(f"Dimensões da imagem: {alt} x {larg}")
print(f"Número de canais: {canais}") #componentes de cor para cada pixel - BGR convertido pra R + G + B = 3
print(f"Tamanho da imagem em bytes: {tamanho}")
print(f"Tipo de dados dos pixels: {tipo_dado}")

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.axis('off')
plt.show()
