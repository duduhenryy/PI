import cv2
import numpy as np

# define a faixa de cor do objeto a ser rastreado em hsv - cor, saturação e valor

#um intervalo de valores no espaço de cores HSV que define uma cor específica (ou um conjunto de cores semelhantes) para ser
# detectada em uma imagem. ela é usada para segmentar ou destacar objetos de uma determinada cor, como pele, roupas, frutas, entre outros

cor_baixa = np.array([29, 86, 6])
cor_alta = np.array([64, 255, 255])

# inicia a captura de vídeo (usa 0 para webcam)
cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, cor_baixa, cor_alta)

    # encontra os contornos da máscara correspondente a regiao com a cor desejada
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # verifica se há contornos detectados
    if contours:
        
        c = max(contours, key=cv2.contourArea) # seleciona o maior contorno
        x, y, w, h = cv2.boundingRect(c)  # obter as coordenadas da caixa envolvente do contorno

        # desenha a caixa
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) # frame, onde começa, até onde vai, cor, expessura

    cv2.imshow("Rastreamento", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
