# Calculadora de Fatorial

Este projeto contém uma função em Python que calcula o fatorial de um número inteiro não negativo. A função `fatorial` permite ao usuário visualizar o cálculo passo a passo, se desejado.

## Funcionalidade

- Cálculo do fatorial de um número inteiro não negativo.
- Opção para exibir o cálculo passo a passo.

## Função `fatorial`

```python
def fatorial(n, show=False):
    """
    Calcula o fatorial de um número inteiro não negativo.
    
    :param n: Número do qual se deseja calcular o fatorial.
    :param show: Se True, exibe o cálculo passo a passo.
    :return: O fatorial de n.
    """
    if n < 0:
        return "Fatorial não definido para números negativos."
    
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
        f *= c
    if show:
        print('= ', end='')
   return f


print(fatorial(int(input('Digite um número: ')), show=True))
help(fatorial)
```

## Descrição

### Parâmetros:
- **n**: Um número inteiro não negativo do qual se deseja calcular o fatorial.
- **show**: Um parâmetro booleano que, se definido como `True`, exibe o cálculo passo a passo.

### Retorno:
O fatorial de `n`. Se `n` for negativo, retorna uma mensagem informando que o fatorial não está definido para números negativos.

## Como Funciona
1. A função verifica se `n` é negativo. Se for, retorna uma mensagem de erro.
2. Inicializa a variável `f` como 1, que armazenará o resultado do fatorial.
3. Utiliza um loop `for` para multiplicar `f` pelos números de `n` até 1.
4. Se `show` for `True`, imprime cada número do cálculo, seguido de "x", até o último número, onde imprime o resultado final.
5. Retorna o valor do fatorial calculado.

## Exemplo de Uso
O código inclui uma chamada para a função `fatorial`, solicitando ao usuário que digite um número. O resultado do fatorial é exibido, juntamente com o cálculo, se `show` for `True`.

```python
print(fatorial(int(input('Digite um número: ')), show=True))
```

## Documentação
A função também possui uma documentação que pode ser acessada usando o comando help(fatorial), que fornece informações sobre os parâmetros e o funcionamento da função.
