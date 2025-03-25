import cv2
import numpy as np

def videoErosao(caminho_imagem, caminho_video):

    imagem = cv2.imread(caminho_imagem, 0)

    # configuracoes dos parametros do video (formato, fps, dimensões e escala de cinza)
    height, width = imagem.shape
    out = cv2.VideoWriter(caminho_video, cv2.VideoWriter_fourcc(*'mp4v'), 5, (width, height), isColor=False)

    # definicao do kernel
    kernel = np.ones((3, 3), np.uint8)

    # aplica a erosao varias vezes 
    clone_imagem = imagem.copy()

    while cv2.countNonZero(clone_imagem) > 0: # conta os pixels que nao sao zeros. o loop continua enquanto houverem pixels brancos nela
        for _ in range(10):  # grava o quadro atual adicionando 10 copias da imagem para deixar as transicoes mais suave
            out.write(clone_imagem)
        clone_imagem = cv2.erode(clone_imagem, kernel) # realiza a erosao na imagem clone

    out.release()
    print(f"Vídeo de erosão salvo em {caminho_video}")


def videoDilatacao(caminho_imagem, caminho_video):

    imagem = cv2.imread(caminho_imagem, 0)

    height, width = imagem.shape
    out = cv2.VideoWriter(caminho_video, cv2.VideoWriter_fourcc(*'mp4v'), 5, (width, height), isColor=False)

    kernel = np.ones((5, 5), np.uint8) # o kernel foi maior para o video nao ficar tao grande

    # aplica a dilatacao até que a imagem fique completamente branca
    clone_imagem = imagem.copy()
    while not np.all(clone_imagem == 255):  # enquanto todos os pixels nao forem brancos
        
        for _ in range(10):  # mesma estrategia para desacelerar um pouco o vídeo
            out.write(clone_imagem)
        clone_imagem = cv2.dilate(clone_imagem, kernel)

    out.release()
    print(f"Vídeo de dilatação salvo em {caminho_video}")

# Exemplo de uso
caminho_imagem = "tarefa8/sources/j.png"
output_erosao = "tarefa8/sources/video_erosao.mp4"
output_dilatacao = "tarefa8/sources/video_dilatacao.mp4"

videoErosao(caminho_imagem, output_erosao)
videoDilatacao(caminho_imagem, output_dilatacao)
