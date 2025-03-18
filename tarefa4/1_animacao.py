import cv2
import numpy as np

img = cv2.imread('tarefa4/yn.png')
height, width, _ = img.shape

# inicializar o vídeo com 30 fps e as mesmas dimensoes da imagem
out = cv2.VideoWriter('video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

# transição de preto para imagem normal
for alpha in np.linspace(0, 1, 60):  # cria 60 quadros para transição com valores de 0 a 1
    frame = cv2.addWeighted(img, alpha, np.zeros_like(img), 1 - alpha, 0) # mescla a imagem com uma tela preta e ajusta o brilho com o alpha
    out.write(frame)

for _ in range(30):  # repete a imagem por 30 quadros, mantendo-a normal
    out.write(img)

# Transição de imagem para preto
for alpha in np.linspace(1, 0, 60):  # cria 60 quadros para transição com valores de 1 pra 0, e conforme alpha diminui a imagem vai ficando preta
    frame = cv2.addWeighted(img, alpha, np.zeros_like(img), 1 - alpha, 0)
    out.write(frame)

out.release()
print("Vídeo criado com sucesso!")
