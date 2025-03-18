import cv2

main_image = cv2.imread('tarefa3/jeongin.png')
watermark = cv2.imread('tarefa3/image.png', cv2.IMREAD_UNCHANGED)  # preserva o alpha se tiver

main_height, main_width = main_image.shape[:2]
watermark = cv2.resize(watermark, (main_width, main_height), interpolation=cv2.INTER_AREA) # redimensiona a marca dagua pra ela abrangir toda imagem original

# Verificar se a marca d'água tem um canal alpha (transparência)
if watermark.shape[2] == 4:
    # Dividir canais BGR e Alpha da marca d'água
    wm_b, wm_g, wm_r, wm_alpha = cv2.split(watermark)
    
    # Criar uma máscara e seu inverso a partir do canal alpha
    mask = cv2.merge([wm_alpha, wm_alpha, wm_alpha])
    inv_mask = cv2.bitwise_not(mask)
    
    # Usar a máscara para combinar as imagens
    background = cv2.bitwise_and(main_image, inv_mask)  # Remover área onde a marca d'água será aplicada
    foreground = cv2.bitwise_and(cv2.merge([wm_b, wm_g, wm_r]), mask)  # Somente a marca d'água
    
    # Combinar o plano de fundo com o plano de frente
    combined = cv2.add(background, foreground)
    main_image = combined
else:
    # Caso a marca d'água não tenha canal alpha, aplicar blending simples
    alpha = 0.2  # Transparência
    main_image = cv2.addWeighted(main_image, 1 - alpha, watermark, alpha, 0)

# Salvar a imagem resultante
output_path = 'tarefa3/watermark.png'
cv2.imwrite(output_path, main_image)
print(f"Imagem com marca d'água salva em: {output_path}")
