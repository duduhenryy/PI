import cv2
import numpy as np

image = cv2.imread('tarefa2/sources/amor.jpeg')

p1 = (930, 390)
p2 = (860, 560)
p3 = (999, 540)

# cria uma lista com os pontos
triangle_cnt = np.array([p1, p2, p3])

# desenha um contorno e pinta de preto (0,0,0); o -1 indica que ele será preenchido com essa cor
cv2.drawContours(image, [triangle_cnt], 0, (0, 0, 0), -1)

# Salvar a imagem resultante
output_path = 'tarefa2/sources/imgTriangulo.jpeg'
cv2.imwrite(output_path, image)

print(f"Imagem salva em: {output_path}")
