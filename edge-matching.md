# Quebra-cabeça de combinação de borda 
### Edge-Matching Puzzle

O quebra-cabeça de correspondência de borda tem o objetivo de organizar peças, que possuem formato idêntico e padrões diferentes.

O objetivo é organizar uma coleção de peças que possuem formato idêntico, porém padrões diferentes. Assim, é necessário que as bordas de cada peça se encaixem com padrões iguais. 

Apesar disso, existem outras variações em que as peças possuem abstrações de positivo e negativo, para que as peças atraem o sinal oposto.

São mais desafiadores que quebra-cabeças normais porque não há uma imagem de referência, duas peças se encaixarem não há garantia que estão no lugar correto. Apenas resolvendo por completo, saberá se as peças estão cada uma no seu devido lugar.

# Formulação o problema como PLI

Formulando o quebra-cabeça como programação linear inteira, podemos ter o seguinte:

## Variáveis

- **ID da peça:** cada peça possui um identificador único e aparece apenas uma vez na solução
- **Cor das bordas:** cada peça será um quadrado que possui uma cor em cada lado
- **Coordenadas no tabuleiro:** a posição x e y em que a peça será inserida
- **Orientação da peça:** qual lado estará voltado para cima 

```
x = {
  "id": 0,
  "color": [0, 1, 2, 3],
  "coordenada": (1, 1),
  "up": 1
}
```

## Restrições

- Cada peça aparece exatamente uma vez na solução
- Cada peça é única na ordem de cores designadas aos lados
- As cores dos lados das peças adjacentes deverão ser iguais para encaixarem, tanto vertical quanto horizontalmente
- As peças podem girar 90º

## Função objetivo

Nossa função objetivo será maximizar a cobertura das cores.

