"""Verifica se uma palavra e um palindromo."""

palavra = input("Digite uma palavra: ").strip().lower()
palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print("E um palindromo.")
else:
    print("Nao e um palindromo.")
