import cv2

def paste(src, dst, x, y): # src: imagem maior e dst: imagem menor

    dst_height, dst_width = dst.shape[:2] # desconsidera os canais (considera só o que ta nos indices 0 e um do shape)

    # substituir o conteúdo da região na imagem maior pela imagem menor
    src[y:y + dst_height, x:x + dst_width] = dst
    return src

imgOriginal = cv2.imread('tarefa2/amor.jpeg')

imgCortada = cv2.imread('tarefa2/clockImg.jpeg')

# define as coordenadas de colar a imagem cortada
x = 285
y = 285

newImg = paste(imgOriginal, imgCortada, x, y)

output_path = 'tarefa2/imgComOutra.jpeg'
cv2.imwrite(output_path, newImg)
print(f"Imagem colada salva em: {output_path}")
