# TAREFA 1 - Descrições

## 1. Carregue uma imagem e um vídeo do seu computador.
Seu primeiro passo é carregar e exibir uma imagem de sua escolha a partir do seu computador usando Python e OpenCV. Certifique-se de que a imagem é exibida corretamente na célula abaixo.
Em seguida, selecione um arquivo de vídeo de seu computador e exiba-o usando uma janela gráfica do OpenCV.

## 2. Extração de informações de imagens
Modifique o código do exercício anterior para que, além de carregar e exibir a imagem, também extraia e mostre na tela as seguintes informações sobre a imagem: suas dimensões, o número de canais, o tamanho em bytes e o tipo de dados de cada pixel.

## 3. Redimensionamento de Imagens
Neste exercício, você irá explorar o redimensionamento de imagens com a biblioteca OpenCV. Sua tarefa é criar uma função rescaleImage(), que redimensiona uma imagem fornecida de acordo com um fator de escala em porcentagem.
A função rescaleImage() deve aceitar dois parâmetros: a imagem a ser redimensionada e a porcentagem de redimensionamento. Por exemplo, rescaleImage(img, 50) deve reduzir a imagem à metade de seu tamanho original, enquanto rescaleImage(img, 200) deve dobrar seu tamanho.

## 4. Manipulação de Pixels: Criando uma Imagem RGB
Neste exercício, você vai se aprofundar na manipulação de pixels utilizando o OpenCV. O objetivo é gerar uma imagem de dimensões 600x300 que será dividida em três colunas iguais, cada uma preenchida por uma das cores primárias de luz - vermelho, verde e azul.

Siga as instruções abaixo:

Crie uma imagem vazia de tamanho 600x300.
Divida a imagem em três colunas iguais. Na primeira coluna, preencha todos os pixels com a cor vermelha (lembre-se, a cor é representada em formato BGR no OpenCV). Na segunda coluna, preencha todos os pixels com a cor verde. Na terceira coluna, preencha todos os pixels com a cor azul.
Salve a imagem resultante em disco com o nome "imagem3.png".
