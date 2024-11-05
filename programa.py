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
