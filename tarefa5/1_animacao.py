import cv2
import numpy as np

# Carregar a imagem
img = cv2.imread('yn.png')
height, width, _ = img.shape

# Inicializar o vídeo
out = cv2.VideoWriter('animacao_simples.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

# Transição de preto para imagem normal
for alpha in np.linspace(0, 1, 60):  # 60 quadros para transição
    frame = cv2.addWeighted(img, alpha, np.zeros_like(img), 1 - alpha, 0)
    out.write(frame)

# Manter a imagem por alguns segundos
for _ in range(30):  # 1 segundo de imagem normal
    out.write(img)

# Transição de imagem para preto
for alpha in np.linspace(1, 0, 60):  # 60 quadros para transição
    frame = cv2.addWeighted(img, alpha, np.zeros_like(img), 1 - alpha, 0)
    out.write(frame)

out.release()
print("Vídeo criado com sucesso!")
