import cv2

# carrega o vídeo pra leitura
cap = cv2.VideoCapture("tarefa1/video.mp4")

while cap.isOpened():
    # processa o vídeo frame por frame - enquanto o video estiver aberto e os frames puderem ser lidos
    ret, frame = cap.read() # lê o frame do vídeo; ret - indica se a leitura foi bem-sucedida (True) ou não (False)
                            # frame - o frame atual do vídeo

    cv2.imshow('Vídeo', frame) # exibe o frame lido

        # opção onde o usuário clica em 'q' para sair da reprodução, interrompendo a leitura dos frames
        # espera uma ação do teclado por 25 mls; o argumento especifica o tempo entre cada frame
    if cv2.waitKey(25) & 0xFF == ord('q'): #o ord converte o 'q' para o valor correspondente ao que encerrará a reprodução
        break

cap.release()
cv2.destroyAllWindows()
