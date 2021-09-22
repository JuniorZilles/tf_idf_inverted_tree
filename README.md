# Trabalho de Introdução a Recuperação de Informação

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

O objetivo deste trabalho é aplicar os conhecimentos adquiridos em aula para a implementação de um sistema de recuperação de informações baseado no modelo vetorial. A aplicação possui quatro objetivos principais que serão avaliados separadamente:

1. Montar um índice baseado em arquivo invertido contendo as frequências de cada termo em cada documento da coleção (50% da nota);
2. Representar cada documento no modelo vetorial (25% da nota);
3. Calcular a similaridade entre a consulta e os documentos que contém pelo menos uma das palavras (15% da nota);
4. Apresentar um ranking ordenado conforme a similaridade previamente calculada (10% da nota).

## Getting Started <a name = "getting_started"></a>

Para executar é necessario ter instalado na máquina:

### Prerequisites

[python](https://www.python.org/)
[pip](https://pip.pypa.io/en/stable/installation/)

### Installing

Instalado os requisitos é necessário rodar o comando abaixo:

```
pip install -r requirements.txt
```

## Usage <a name = "usage"></a>

Colocar a pasta com os arquivos a indexar dentro da pasta `arquivos`

```
- arquivos
    - pasta com arquivos .txt para indexação
- src
- LICENSE
- README.md
- Requirements.txt
- run.py
```

Caso for utilizar linha de comando usar o seguinte comando:
```
python run.py
```

Pela IDE executar o arquivo run.py utilizando o F5
