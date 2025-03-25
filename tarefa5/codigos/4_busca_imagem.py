import cv2
import numpy as np
import os

# calcula o histograma normalizado de uma imagem em escala de cinza

def calcular_histograma(image):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    cv2.normalize(hist, hist)
    return hist

# compara dois histogramas usando as métricas correlação, chi quadrado e bhattacharyya
# correlação: avalia o quanto dois histogramas são semlhantes. se for 1, eles são identicos; se for -1 eles são totalmente diferentes
# chi quadrado: analisa o quão diferentes dois histogramas são, com uma soma de diferenças quadradas entre eles. quanto maior o valor,
#               mais diferentes são os histogramas.
# bhatta: medida de similaridade, que leva em consideração a distribuição e a forma dos histogramas. valores próximos a 0 indica
#         que os histogramas são muito semelhantes

def comparar_histogramas(hist1, hist2):
    corr = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    chi_sq = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CHISQR)
    bhatta = cv2.compareHist(hist1, hist2, cv2.HISTCMP_BHATTACHARYYA)
    return corr, chi_sq, bhatta

# calcula a distância total baseada na fórmula fornecida

def calcular_distancia_total(corr, chi_sq, bhatta):
    total_distance = np.sqrt((1 - corr)**2 + chi_sq**2 + bhatta**2)
    return total_distance

# compara S1 com uma lista de imagens e encontra a mais similar com base na menor distância total

def encontrar_img_semelhante(caminho_s1, caminhos_imagens):
    s1_image = cv2.imread(caminho_s1, cv2.IMREAD_GRAYSCALE)
    s1_hist = calcular_histograma(s1_image)

    distancias = {}
    metricas = {}

    for image_path in caminhos_imagens:
        # carrega a imagem comparada e calcular seu histograma
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        hist = calcular_histograma(image)

        # calcula as métricas de distância
        corr, chi_sq, bhatta = comparar_histogramas(s1_hist, hist)

        # calcula a distância total
        total_distance = calcular_distancia_total(corr, chi_sq, bhatta)
        distancias[image_path] = total_distance
        metricas[image_path] = (corr, chi_sq, bhatta)

    # encontra a imagem com a menor distância total
    imagem_mais_semelhante = min(distancias, key=distancias.get)
    return imagem_mais_semelhante, distancias, metricas

caminho_s1 = "tarefa5/sources/S1.jpg"
caminhos_imagens = ["tarefa5/sources/S2.jpg", "tarefa5/sources/D1.jpg", "tarefa5/sources/D2.jpg", "tarefa5/sources/D3.jpg"]  # Lista de imagens a comparar

imagem_mais_semelhante, distancias, metricas = encontrar_img_semelhante(caminho_s1, caminhos_imagens)

print("Imagem mais similar a S1:", imagem_mais_semelhante)
print("\nDistâncias totais e métricas:")
for image, distance in distancias.items():
    corr, chi_sq, bhatta = metricas[image]
    print(f"Imagem: {image}")
    print(f"  Correlação: {corr:.4f}")
    print(f"  Chi-Square: {chi_sq:.4f}")
    print(f"  Bhattacharyya: {bhatta:.4f}")
    print(f"  Distância Total: {distance:.4f}\n")
