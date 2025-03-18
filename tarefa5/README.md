# Tarefa 5 - Descrição
## 1. Construção de Histograma
Faça um algoritmo que carregue uma imagem, converta-a para preto e branco e gere um histograma nos moldes do que é apresentado abaixo:

## 2. Construção de Histograma Colorido
Faça um procedimento similar ao apresentado acima, mas para uma imagem colorida.
 
## 3. Equalização de Histograma
Procure pela técnica de Equalização de Histograma e a implemente para aumentar o contraste de uma imagem escolhida por você. Feito isso, produza o histograma de ambas as imagens (antes e depois) para que você possa fazer uma comparação visual.
  
## 4. Meu primeiro buscador de imagens!
Objetivo: Aprender a comparar imagens por meio de seus histogramas, utilizando diferentes métricas de distância.
 
### Instruções:

Crie uma pasta com ao menos 5 imagens. Duas delas devem ser visualmente similares (não idênticas) e serão chamadas de S1 e S2. As demais imagens diferentes serão D1, D2 e D3;

Implemente uma função que receba a imagem S1 e compare-a com S2, D1, D2 e D3 utilizando seus histogramas;

Calcule a distância de S1 para cada imagem usando as métricas de Correlação, Chi-Square e Bhattacharyya;

Para cada imagem, calcule a distância total da seguinte forma:

$$
\text{Distância Total} = \sqrt{(1 - \text{Corr})^2 + \text{Chi-Sq}^2 + \text{Bhatta}^2}
$$


Retorne o nome da imagem que apresentou a menor distância em relação a S1.
