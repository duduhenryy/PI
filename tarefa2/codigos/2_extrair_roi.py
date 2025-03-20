import cv2

def crop(image, x, y, width, height):
    corte = image[y:y + height, x:x + width]
    # posição inicial do y até a altura (posição final)
    # o mesmo ocorre com o x
    return corte

img = cv2.imread('tarefa2/sources/amor.jpeg')

x_relogio = 879
y_relogio = 493
largura_relogio = 106
altura_relogio = 66

clockImg = crop(img, x_relogio, y_relogio, largura_relogio, altura_relogio)

output_path = 'tarefa2/sources/clockImg.jpeg'
cv2.imwrite(output_path, clockImg)
print(f"Imagem salva em: {output_path}")
