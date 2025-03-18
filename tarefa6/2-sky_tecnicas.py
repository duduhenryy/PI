import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# calcular acurácia
def calcular_acuracia(predicao, ground_truth):
    pixels_corretos = np.sum(predicao == ground_truth)
    pixels_totais = predicao.size
    return pixels_corretos / pixels_totais

caminho_imagens = "tarefa7/data"
caminho_mascaras = "tarefa7/gabarito"

# carregar imagens e máscaras
images = [cv2.imread(os.path.join(caminho_imagens, img)) for img in os.listdir(caminho_imagens)]
masks = [cv2.imread(os.path.join(caminho_mascaras, mask), 0) for mask in os.listdir(caminho_mascaras)]

acuracias = {"Binária": [], "Binária Invertida": [], "Adaptativa": [], "Otsu": []}

for image, mask in zip(images, masks):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # converte as imagens para tons de cinza
    
    # limiarização binária
    _, limBinaria = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    acuracias["Binária"].append(calcular_acuracia(limBinaria, mask))
    
    # binária invertida
    _, limBinariaInv = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    acuracias["Binária Invertida"].append(calcular_acuracia(limBinariaInv, mask))
    
    # adaptativa
    limAdaptativa = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    acuracias["Adaptativa"].append(calcular_acuracia(limAdaptativa, mask))
    
    # otsu
    _, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    acuracias["Otsu"].append(calcular_acuracia(otsu, mask))

for metodo in acuracias:
    print(f"{metodo}: Acurácia Média = {np.mean(acuracias[metodo])}")

# exemplo
exemplo_index = 0
imagem_exemplo = cv2.cvtColor(images[exemplo_index], cv2.COLOR_BGR2RGB)
mask_exemplo = masks[exemplo_index]

gray_exemplo = cv2.cvtColor(images[exemplo_index], cv2.COLOR_BGR2GRAY)
_, binaria_exemplo = cv2.threshold(gray_exemplo, 127, 255, cv2.THRESH_BINARY)
_, binaria_inv_exemplo = cv2.threshold(gray_exemplo, 127, 255, cv2.THRESH_BINARY_INV)
adaptativa_exemplo = cv2.adaptiveThreshold(gray_exemplo, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41, 10)
_, otsu_exemplo = cv2.threshold(gray_exemplo, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.imshow(imagem_exemplo)
plt.title("Imagem Original")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(mask_exemplo, cmap="gray")
plt.title("Ground Truth")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(binaria_exemplo, cmap="gray")
plt.title("Binária")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(binaria_inv_exemplo, cmap="gray")
plt.title("Binária Invertida")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(adaptativa_exemplo, cmap="gray")
plt.title("Adaptativa")
plt.axis("off")

plt.subplot(2, 3, 6)
plt.imshow(otsu_exemplo, cmap="gray")
plt.title("Otsu")
plt.axis("off")

plt.tight_layout()
plt.show()
