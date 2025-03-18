# Tarefa 6 - Descrição
## 1. Aplicando limiarização
Utilizando os algoritmos de Limiarização conhecidos, descubra os que melhor separam as partes relevantes das imagens abaixo.

https://drive.google.com/drive/folders/1u-rKiYBE59NaA8Ej9YgaOQDYwwipkYvE?usp=sharing

carta_getulio.jpg => separar o texto da carta do fundo
mapa1.gif, mapa2.gif e mapa3.gif => separar o mapa das linhas e letras

## 2. Exercício de Segmentação de Céu com Técnicas de Limiarização
O objetivo deste exercício é aplicar diferentes técnicas de limiarização para segmentar o céu em um conjunto de imagens. Você vai usar o Sky Dataset, que contém 60 imagens com suas respectivas segmentações de céu (ground truths).

Download do Dataset: Baixe o Sky Dataset, que contém imagens e suas respectivas segmentações de céu (ground truths): http://www.vision.ime.usp.br/~pmiranda/downloads/sky/SkyDataset.html

### Preparação dos Dados
Carregue as imagens e suas segmentações correspondentes usando OpenCV.

### Aplicação de Técnicas de Limiarização 
Aplique ao menos 3 técnicas de limiarização (binária, binária invertida, adaptativa, Otsu) para segmentar o céu nas imagens. Se quiser, você pode experimentar com diferentes espaços de cores (RGB, HSV, etc.) e canais.

### Cálculo da Acurácia 
Utilize as imagens de ground truth para calcular a acurácia da segmentação. A acurácia pode ser calculada como a razão entre o número de pixels corretamente classificados e o número total de pixels.

### Análise Comparativa 
Compare a acurácia das diferentes técnicas de limiarização. Identifique e apresente a técnica que obteve o melhor desempenho em termos de acurácia.
