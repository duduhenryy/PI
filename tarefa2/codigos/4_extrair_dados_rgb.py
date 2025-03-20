import cv2
import numpy as np

def predominant_color(image_path):

    image = cv2.imread(image_path)

    blue_channel, green_channel, red_channel = cv2.split(image)

    # cria imagens vazias (com todos os pixels em zero) do mesmo tamanho que a imagem original
    blue_image = np.zeros_like(image)
    green_image = np.zeros_like(image)
    red_image = np.zeros_like(image)

    # preenche apenas o canal de cor selecionado
    blue_image[:, :, 0] = blue_channel
    green_image[:, :, 1] = green_channel
    red_image[:, :, 2] = red_channel

    cv2.imwrite("blue_channel.png", blue_image)
    cv2.imwrite("green_channel.png", green_image)
    cv2.imwrite("red_channel.png", red_image)

    # calcula a média de todos os valores de pixel em cada canal
    blue_mean = np.mean(blue_channel)
    green_mean = np.mean(green_channel)
    red_mean = np.mean(red_channel)

    if red_mean > green_mean and red_mean > blue_mean:
        dominant_color = "vermelha"
    elif green_mean > red_mean and green_mean > blue_mean:
        dominant_color = "verde"
    else:
        dominant_color = "azul"

    print(f"Média do canal vermelho: {red_mean}")
    print(f"Média do canal verde: {green_mean}")
    print(f"Média do canal azul: {blue_mean}")
    print(f"A cor predominante é: {dominant_color}")

    return dominant_color

image_path = 'tarefa2/sources/parrot.jpg'

predominant_color(image_path)
