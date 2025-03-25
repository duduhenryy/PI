import cv2
import numpy as np
import matplotlib.pyplot as plt

def aplicar_filtro(imagem, filtro):
    
    if filtro == "media":

        # filtro de suavização que calcula a media dos valores dos pixels em uma janela deslizante conhecida como kernel sobre a imagem
        kernel = np.ones((5, 5), dtype=np.float32) / 25 # cria um kernel 5x5
        return cv2.filter2D(imagem, -1, kernel) # -1 preserva o mesmo tipo de dado
    
    elif filtro == "gaussiano":

        # utiliza a função gaussiana para o cálculo dos coeficientes da máscara (quanto mais centralizado maior o valor)
        return cv2.GaussianBlur(imagem, (3, 3), 0) # tamanho do kernel e o DP, que será calculado automaticamente
    
    elif filtro == "mediana":

        # filtro nao linear, pois nao é feita a convolução da mascara
        # a intensidade de cada pixel é dada através da mediana de seus vizinhos, e é muito eficaz para ruidos sal e pimenta
        return cv2.medianBlur(imagem, 5)
    
    elif filtro == "sobel":

        # detector de bordas a partir de gradientes em direções horizontais e verticais
        # combina essas informações para gerar a magnitude do gradiente resultante
        sobelx = cv2.Sobel(imagem, 5, 1, 0, ksize=3)
        sobely = cv2.Sobel(imagem, 5, 0, 1, ksize=3)
        sobel = cv2.magnitude(sobelx, sobely)
        return np.uint8(np.absolute(sobel)) # converte os valores de volta para uma imagem normalizada
    
    elif filtro == "laplaciano":

        # filtro de realce (derivação) que utiliza derivadas de segunda ordem
        # realça bordas na imagem, mas ameniza regioes com níveis de cinza constantes
        laplaciano = cv2.Laplacian(imagem, 5)
        return np.uint8(np.absolute(laplaciano))
    
    elif filtro == "canny edge":

        # detecta bordas a partir de multiplos estágios, sendo eles a suavização com filtro gaussiano, cálculo de gradientes com Sobel
        # supressão não máxima (reduz "bordas falsas") e histerese (sa dois thresholds para decidir bordas fortes e fracas)
        return cv2.Canny(imagem, 100, 200)
    
    else:
        raise ValueError("Filtro desconhecido: " + filtro)

imagem = cv2.imread("tarefa7/sources/totoro.jpg", 0)

# realiza a aplicação dos filtros na imagem a partir da função
filtros = ["media", "gaussiano", "mediana", "sobel", "laplaciano", "canny edge"]
imagens_filtradas = [aplicar_filtro(imagem, filtro) for filtro in filtros]

# exibe as imagens em um grid
plt.figure(figsize=(12, 8))
for i, (filtro, img) in enumerate(zip(filtros, imagens_filtradas)):
    plt.subplot(2, 3, i + 1) # grid de 2 linhas e 3 colunas cujas janelas são preenchidas a cada iteração
    plt.imshow(img, cmap="gray")
    plt.title(filtro.capitalize()) # adiciona o nome do filtro no topo de cada subplot
    plt.axis("off")
plt.tight_layout()
plt.show()
