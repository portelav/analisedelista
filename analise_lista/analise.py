def analisar_lista(numeros):
    if not numeros:
        print("A lista está vazia.")
        return

    quantidade = len(numeros)
    soma = sum(numeros)
    media = soma / quantidade
    maior = max(numeros)
    menor = min(numeros)
    pares = len([n for n in numeros if n % 2 == 0])


    print(f"Média: {media:.2f}")
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
    print(f"Números pares: {pares}")