import numpy as np
import cv2

altura = 300
largura = 600
imagem = np.zeros((altura, largura, 3), dtype=np.uint8)  # cria uma imagem vazia (300 linhas, 600 colunas, 3 canais), com valor 0 em todos os canais

imagem[:, 0:200, 2] = 255  # preenche a primeira coluna (de 0 a 200) com o valor 255 no vermelho - indice 2 por causa do bgR

imagem[:, 200:400, 1] = 255  # preenche a segunda coluna (de 200 a 400) com o valor 255 no verde - indice 1 por causa do bGr

imagem[:, 400:600, 0] = 255  # preenche a terceira coluna de 400 a 600) com o valor 255 no canal azul - indice 0 por causa do Bgr

# salva a imagem
cv2.imwrite("imagem3.png", imagem)

cv2.imshow("Imagem RGB", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
