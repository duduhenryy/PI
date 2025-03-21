import numpy as np

def conv2d(imagem, matriz):

    # define as dimensões da imagem e do kernel
    img_h, img_w = imagem.shape
    kernel_h, kernel_w = matriz.shape

    # verifica se o kernel está nos conformes - 2x2 ou 3x3
    if (kernel_h, kernel_w) not in [(2, 2), (3, 3)]:
        raise ValueError("A matriz de convolução (kernel) deve ser 2x2 ou 3x3.")

    # calcula o zero padding
    # ele adiciona bordas de zeros nas matrizes de imagens, garantindo que as convoluções sejam feitas em todos os pixels sem problemas
    pad_h, pad_w = kernel_h // 2, kernel_w // 2 # metade do tamanho arredondado para baixo

    # adiciona o zero padding na imagem
    matrizComPadding = np.pad(imagem, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)
                                        # adiciona pad_h elementos antes e depois de cada linha e pad_w antes e depois de cada coluna

    # cria uma matriz com as mesmas dimensões da imagem de saída preenchida com zeros
    imgConvolucionada = np.zeros_like(imagem, dtype=np.float32)

    # realiza a convolução percorrendo cada pixel i,j da imagem original
    for i in range(img_h):
        for j in range(img_w):

            # extrai a regiao da imagem do mesmo tamanho do kernel
            regiao = matrizComPadding[i:i + kernel_h, j:j + kernel_w]

            # faz a operação convolucional de multiplicar elemento por elemento entre a região da imagem e o kernel e somar os resultados
            # para calcular o valor do pixel resultante
            imgConvolucionada[i, j] = np.sum(regiao * matriz)

    # restringir os valores para a faixa de 0-255, que são de imagens
    imgConvolucionada = np.clip(imgConvolucionada, 0, 255)
    return imgConvolucionada.astype(np.uint8)

imagem = np.array([[10, 20, 30, 40],
                    [50, 60, 70, 80],
                    [90, 100, 110, 120],
                    [130, 140, 150, 160]])

kernel2x2 = np.array([[1, 0],
                    [1, 0]])

kernel3x3 = np.array([[1, 0, -1],
                    [1, 0, -1],
                    [1, 0, -1]])

imgConvolucionada = conv2d(imagem, kernel2x2)
print(imgConvolucionada)
