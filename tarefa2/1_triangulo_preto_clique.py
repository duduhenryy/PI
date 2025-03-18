import cv2
import numpy as np

image = cv2.imread('tarefa2/amor.jpeg')
points = []


def select_points(event, x, y, flags, param):
    global points, image
    if event == cv2.EVENT_LBUTTONDOWN: # identifica que o botao esquerdo foi pressionado
        # adiciona o ponto clicado na lista
        points.append((x, y))

        # desenha um pequeno círculo vermelho com raio de 5 pixels no ponto onde o usuário clicou
        cv2.circle(image, (x, y), 5, (0, 0, 255), -1)
        cv2.imshow("Escolha 3 pontos", image)

        if len(points) == 3:
            # cria uma lista com os pontos do triângulo
            triangle_cnt = np.array(points)
            
            # desenha o triângulo preenchido com cor preta
            cv2.drawContours(image, [triangle_cnt], 0, (0, 0, 0), -1)
            cv2.imshow("Escolha 3 pontos", image)

            output_path = 'tarefa2/imgTrianguloClique.jpeg'
            cv2.imwrite(output_path, image)
            print(f"Imagem salva em: {output_path}")
            cv2.destroyAllWindows()

cv2.imshow("Escolha 3 pontos", image)
cv2.setMouseCallback("Escolha 3 pontos", select_points)
cv2.waitKey(0)
cv2.destroyAllWindows()
