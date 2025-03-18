import cv2

original_img = cv2.imread('tarefa3/jeongin.png')
mask_img = cv2.imread('tarefa3/jeongin_pintado.png')

original_height, original_width = original_img.shape[:2]
mask_img = cv2.resize(mask_img, (original_width, original_height)) # redimensiona para que as imagens fiquem iguais em dimensao

# fazer o blending
# realiza a soma ponderada das imagens - soma os pixels e gera um novo pixel, para a terceira imagem
# define pesos pra gerar translucidez entre as imagens, reduzindo a intensidade de cada pixel em todos os canais
# o último parametro é o gama, que está zerado
blended_img = cv2.addWeighted(mask_img, 0.2, original_img, 0.8, 0)

output_path = 'tarefa3/jeongin_loiro.png'
cv2.imwrite(output_path, blended_img)
print(f"Imagem com cabelo colorido salva em: {output_path}")