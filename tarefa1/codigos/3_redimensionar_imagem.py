import cv2

def rescaleImage(img, scale_percent):
    # img - A imagem a ser redimensionada (matriz do OpenCV).
    # scale_percent - A porcentagem de redimensionamento (ex: 50 para reduzir à metade).
    # calcula as novas dimensões da imagem
    width = int(img.shape[1] * scale_percent / 100) # largura
    height = int(img.shape[0] * scale_percent / 100) # altura
    new_dimensions = (width, height)
    
    # redimensiona utilizando o resize
    # o interpolation determina qual método de interpolação será utilizado, nesse caso o inter_area
    # que calcula uma média entre os pixels da imagem original para preservar os detalhes ao máximo - otimização
    resized_image = cv2.resize(img, new_dimensions, interpolation=cv2.INTER_AREA)
    
    # interpolação é usada para preencher ou combinar pixels de forma suave e evitar distorções

    return resized_image

if __name__ == "__main__":
    img = cv2.imread("tarefa1/amor.jpeg")

    resized_img = rescaleImage(img, 50)

    cv2.imshow("Imagem Original", img)
    cv2.imshow("Imagem Redimensionada - 50%", resized_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
