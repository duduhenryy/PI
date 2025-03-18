# Tarefa 7 - Descrição

## 1. Filtragem
Considere os seguintes filtros:

- Filtro da Média
- Filtro Gaussiano
- Filtro da Mediana
- Filtro Sobel
- Filtro Laplaciano
- Canny Edge


Crie uma função que receba uma imagem em tons de cinza e o nome do filtro. Essa função deve retornar a imagem com o filtro aplicado.

Apresente todas as imagens filtradas em um grid usando subplots.

## 2. Implementação de Convolução 2D Manual
Neste exercício, você irá implementar um filtro de convolução 2D sem utilizar funções prontas do OpenCV. O objetivo é criar um código que execute a operação de convolução de forma autônoma, gerando uma imagem modificada como resultado.

Requisitos:

A imagem de entrada pode estar em escala de cinza.
A função deve suportar matrizes de convolução 2x2 ou 3x3.
Assinatura da Função: Sua função deverá ser chamada da seguinte forma:

dest_image = conv2d(source_image, matrix)

Parâmetros:

- source_image: Imagem original em escala de cinza representada como uma matriz;
- matrix: Matriz 2x2 ou 3x3 que será usada na operação de convolução;
- dest_image: Imagem modificada, também representada como uma matriz.
 
## 3. Aprimoramento de Imagens Usando Filtros Passa-Baixa e Passa-Alta
O objetivo deste exercício é implementar uma técnica de aprimoramento de imagens que combine filtros passa-baixa e passa-alta.

Implementação de Filtros: Implemente duas funções que, respectivamente, a primeira aplique um determinado filtro passa-baixa e a segunda aplique um filtro passa-alta. Essas funções devem receber uma imagem em escala de cinza como entrada e retornam a imagem filtrada.

Combinação de Filtros: Crie uma função aprimora_imagem que combine as saídas dos filtros passa-baixa e passa-alta das funções anteriores para criar uma versão aprimorada da imagem original.

Análise: Mostre as imagens antes e depois do aprimoramento em um grid usando subplots.

Bônus: Implemente uma interface gráfica simples para carregar uma imagem e aplicar o aprimoramento.

