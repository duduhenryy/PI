import cv2
import matplotlib.pyplot as plt

imgCarta = cv2.imread('tarefa7/sources/carta_getulio.jpg', 0)

# limiarizacao - tecnica que consiste em pegar uma imagem e representá-la em apenas preto e branco

# limiarização global - passa a imagem, o limiar, tom das cores acima do limiar e o tipo de limiarização como parâmetro

_, limGlobal = cv2.threshold(imgCarta, 200, 255, cv2.THRESH_BINARY)

# limiarização adaptativa - difere da global pq a global usa um mesmo limiar na imagem toda; a adaptativa permite que cada
# regiao da imagem tenha um limiar proprio que é calculado pelo método. ela se ajusta., por isso o nome adaptativa. passa
# como parametro a imagem, valor maximo do limiar, qual metodo vai ser utilizado, o tipo de binarizacao a ser usado, o tamanho do
# bloco onde sera calculado o limiar e o valor do C, que será subtraído pela fórmula

limAdaptativa = cv2.adaptiveThreshold(imgCarta, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41, 10) # essa calcula pela média da area

# limiarização otsu - especie de limiarização automatica, onde ele mesmo calcula automaticamente o melhor valor de limiar para separar
# os níveis de intensidade da imagem em dois grupos: fundo e objeto. baseia-se na maximização da variância interclasses ou na
# minimização da variância intraclasses e tem como parametros a imagem, o limiar 0, valor maximo do limiar e a soma com a flag de otsu

_, limOtsu = cv2.threshold(imgCarta, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


titulos = ['Original', 'Global', 'Adaptativa', 'Otsu']
imagensCarta = [imgCarta, limGlobal, limAdaptativa, limOtsu]

for i in range(len(imagensCarta)):
    plt.subplot(1, 4, i+1)
    plt.imshow(imagensCarta[i], cmap='gray')
    plt.title(titulos[i])
    plt.axis('off')

plt.show()

# Fazendo para os mapas

mapa1 = cv2.imread('tarefa7/sources/mapa1.jpg', 0)
mapa2 = cv2.imread('tarefa7/sources/mapa2.jpg', 0)
mapa3 = cv2.imread('tarefa7/sources/mapa3.jpg', 0)

_, limGlobalMapa1 = cv2.threshold(mapa1, 127, 255, cv2.THRESH_BINARY)
_, limGlobalMapa2 = cv2.threshold(mapa2, 127, 255, cv2.THRESH_BINARY)
_, limGlobalMapa3 = cv2.threshold(mapa3, 127, 255, cv2.THRESH_BINARY)

limAdaptativaMapa1 = cv2.adaptiveThreshold(mapa1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41, 10)
limAdaptativaMapa2 = cv2.adaptiveThreshold(mapa2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41, 10)
limAdaptativaMapa3 = cv2.adaptiveThreshold(mapa3, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41, 10)

_, limOtsuMapa1 = cv2.threshold(mapa1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
_, limOtsuMapa2 = cv2.threshold(mapa2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
_, limOtsuMapa3 = cv2.threshold(mapa3, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


imgsMapa1 = [mapa1, limGlobalMapa1, limAdaptativaMapa1, limOtsuMapa1]
for i in range(len(imgsMapa1)):
    plt.subplot(1, 4, i+1)
    plt.imshow(imgsMapa1[i], cmap='gray')
    plt.title(titulos[i])
    plt.axis('off')
plt.show()

imgsMapa2 = [mapa2, limGlobalMapa2, limAdaptativaMapa2, limOtsuMapa2]
for i in range(len(imgsMapa2)):
    plt.subplot(1, 4, i+1)
    plt.imshow(imgsMapa2[i], cmap='gray')
    plt.title(titulos[i])
    plt.axis('off')
plt.show()

imgsMapa3= [mapa3, limGlobalMapa3, limAdaptativaMapa3, limOtsuMapa3]
for i in range(len(imgsMapa3)):
    plt.subplot(1, 4, i+1)
    plt.imshow(imgsMapa3[i], cmap='gray')
    plt.title(titulos[i])
    plt.axis('off')
plt.show()
