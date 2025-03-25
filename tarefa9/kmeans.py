import cv2
import numpy as np

imagem = cv2.imread("tarefa9/sources/yn.png")
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# conversão da cópia da imagem original para o formato que o k-means trabalha: matriz de pixels de dimensoes -1 para linhas (valor n) e
# 3 colunas (RGB). cada linha é um pixel a ser aplicado no k-means
copia = imagem.copy()
copia = cv2.resize(copia, (0, 0), fx= 0.2, fy=0.2)
matriz_pixels = copia.reshape((-1, 3))

# converte para float pq o k-means trabalha com numeros reais
matriz_pixels = np.float32(matriz_pixels)

# criterios para interromper o k-means: o epslon (demarca o quão diferentes os conjuntos estão: se o valor for muito proximo de 0, terão
# muitas iterações para garantir que os conjuntos estão diferentes) e o max iter (define o número máximo de iterações)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 40, 0.1) # número de iterações e o valor do epslon
# quem for atendido primeiro, encerra a execução do algoritmo

K = 256  # numero de cores

_, labels, centroides = cv2.kmeans(matriz_pixels, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
# labels = gavetas. a quantidade de cores são as gavetas e cada pixel vai para uma delas
# centroides = média de cores daquele conjunto - a cor a ser atribuída na imagem. quando um pixel vai pra gaveta, recebe a cor do centroide
# parametros: matriz de pixels, numero de cores, rotulos pre estabelecidos, criterios, número de restarts do algoritmo,

# converte os floats para inteiros
centroides = np.uint8(centroides)

imagem_centroides = centroides[labels.flatten()] # o labels é a matriz do mesmo tamanho da imagem onde cada posição é a gaveta, não a cor
# o flatten transforma em um vetor de uma dimensão. as cores dos centroides são aplicados nas posições desse vetor.

# redimensiona para a forma original da imagem
imagem_segmentada = imagem_centroides.reshape(copia.shape)
imagem_segmentada = cv2.cvtColor(imagem_segmentada, cv2.COLOR_RGB2BGR)

cv2.imshow("imagem segmntada", imagem_segmentada)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("tarefa9/sources/imagem_8bits.jpg", cv2.cvtColor(imagem_segmentada, cv2.COLOR_RGB2BGR))
