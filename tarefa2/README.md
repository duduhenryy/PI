# TAREFA 2 - Descrições

## 1. Manipule pixels para criar um triângulo
Crie um algoritmo que receba as coordenadas de três pontos de um triângulo: p1, p2 e p3. Use essas informações para pintar um triângulo de cor preta em uma imagem.

Salve a imagem resultante em disco, fazendo com que o triângulo preto ocupe a região definida pelos três pontos mencionados.

Considere o exemplo abaixo:

<img width="338" alt="Image" src="https://github.com/user-attachments/assets/5a5a6cc7-0c3e-4a3d-b341-664cdb55a91d" />

## 2. Extração de Região de Interesse (ROI) em uma Imagem
Sua tarefa é criar uma função chamada crop(). Essa função deve receber cinco parâmetros: uma imagem, as coordenadas x e y, e as dimensões de altura e largura da região a ser recortada. A função deve retornar o segmento da imagem correspondente a essa região.

Suponha a imagem abaixo, que chamaremos de messiImg:

![Image](https://github.com/user-attachments/assets/c51ea539-fdc9-4205-aa3c-d68bf5a2f265)

Por exemplo, se sua função for chamada com os seguintes parâmetros:

- x_bola = 336
- y_bola = 287
- largura_bola = 163
- altura_bola = 49

ballImg = crop(messiImg, x_bola, y_bola, largura_bola, altura_bola)

A variável ballImg deve conter apenas a imagem da bola.

![Image](https://github.com/user-attachments/assets/11cd9da3-77cf-469a-b097-f0232b9bac80)

## 3. Colar Imagem em uma Posição Específica
Neste exercício, você criará uma função chamada paste(), que "cola" uma imagem menor (destino) em uma imagem maior (origem).

A função paste() deve receber quatro parâmetros:

- src (source): A imagem original onde a imagem menor será colada.
- dst (destination): A imagem menor que será colada na imagem original.
- x, y: As coordenadas da posição na imagem original onde a imagem menor será colada.

A função deve retornar a imagem original modificada com a imagem menor colada na posição especificada.
Por exemplo, ao chamar a função abaixo:

newImg = paste(messiImg, ballImg, x, y)

O resultado será a imagem newImg, com a ballImg colada na posição (x, y) da imagem messiImg.

![Image](https://github.com/user-attachments/assets/0ce38f62-c506-4908-bb6f-d5b714a93011)

## 4. Trabalhando com Canais de Cores

![Image](https://github.com/user-attachments/assets/12423af5-8d3a-434d-abd6-0c4be3dda5c8)

Neste exercício, seu objetivo é determinar qual é a cor predominante — "vermelha", "verde" ou "azul" — em uma imagem dada.

Você deve criar um algoritmo que execute as seguintes etapas:

Extrair Canais de Cores: Separe a imagem em três canais de cores diferentes, gerando três novas imagens. Cada uma deve conter apenas um dos canais de cor: vermelho, verde e azul, respectivamente.

Calcular a Média de Cores: Para cada imagem de canal de cor, calcule a média dos tons, somando os valores de todos os pixels e dividindo pelo total de pixels.

Determinar a Cor Predominante: Compare as médias dos três canais e determine a maior delas, ou seja, qual cor é predominante. Se a imagem do canal vermelho tiver a maior média, então a imagem é mais "vermelha", e assim por diante.
