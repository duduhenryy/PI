import cv2
import numpy as np
import matplotlib.pyplot as plt

imagem = cv2.imread("tarefa10/dog.jpg")
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# cria uma máscara com as mesmas dimensoes da imagem
mascara = np.zeros(imagem.shape[:2], np.uint8)

# incializar o modelo de mistura de gaussianos do objeto e do fundo. ele precisa dessa estrutura para trabalhar
fundo_model = np.zeros((1, 65), np.float64)  # vetor de 65 escaláveis cheio de zeros com posições float do fundo
obj_model = np.zeros((1, 65), np.float64)  # vetor do objeto

# região de interesse do grabCut
altura, largura = imagem.shape[:2]
retangulo = (450, 100, 780, altura - 100)  # Formato: (x, y, largura, altura)

# aplica o grabCut
# parametros: a imagem, a mascara vazia, a regiao de interesse, as GMMs de fundo e objeto, o total de iterações e a key para iniciar com retangulo
cv2.grabCut(imagem, mascara, retangulo, fundo_model, obj_model, 5, cv2.GC_INIT_WITH_RECT)

# cria a mascara final, onde 0 e 2 são fundo e 1 e 3 são objeto
mascara_final = np.where((mascara == 2) | (mascara == 0), 0, 1).astype("uint8")
# se a posição ser fundo ou provavelmente fundo, será setada como 0 (fundo); caso contrário, 1 (objeto) e converte para inteiro

# adiciona um vetor que torna cada matriz de um escalar tridimensional, pois na imagem do opencv cada matriz é um vetor 3D
# necessário para que a multiplicação entre os pixels da imagem e as posições da mascara ocorram de forma correta e separe o fundo do objeto
objeto_segmentado = imagem * mascara_final[:, :, np.newaxis]

# aplica o filtro gaussiano no fundo para desfocar a imagem
fundo_desfocado = cv2.GaussianBlur(imagem, (51, 51), 0)

# cria a imagem final mesclando o fundo com o objeto
resultado = fundo_desfocado * (1 - mascara_final[:, :, np.newaxis]) + objeto_segmentado
# inverte a máscara para que o fundo seja multiplicado pelo desfoque e depois adiciona o cachorro

# Desenha a caixa envolvente vermelha na imagem original
imagem_com_caixa = imagem.copy()
cv2.rectangle(imagem_com_caixa, (retangulo[0], retangulo[1]), (retangulo[0] + retangulo[2], retangulo[1] + retangulo[3]), (255, 0, 0), 3)

plt.figure(figsize=(20, 10))
plt.subplot(1, 4, 1)
plt.title("Imagem Original")
plt.imshow(imagem)
plt.axis("off")

plt.subplot(1, 4, 2)
plt.title("Imagem com Caixa Envolvente")
plt.imshow(imagem_com_caixa)
plt.axis("off")

plt.subplot(1, 4, 3)
plt.title("Segmentação (GrabCut)")
plt.imshow(objeto_segmentado)
plt.axis("off")

plt.subplot(1, 4, 4)
plt.title("Imagem com Fundo Borrado")
plt.imshow(resultado.astype(np.uint8))
plt.axis("off")

plt.show()

cv2.imwrite("tarefa10/resultado_grabcut.jpg", cv2.cvtColor(resultado.astype(np.uint8), cv2.COLOR_RGB2BGR))
