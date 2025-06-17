from colorama import init, Fore, Style

init(autoreset=True)

largura = 40

print(Fore.YELLOW + "╔" + "═" * (largura - 2) + "╗")
print(Fore.CYAN + "║" + " LISTA DUPLA ".center(largura - 2) + "║")
print(Fore.YELLOW + "╚" + "═" * (largura - 2) + "╝")

def lista_dupla(lista1, lista2):
    lista_resultado = []

    # Primeira parte: elementos em lista1 que não estão em lista2
    for elemento in lista1:
        if elemento not in lista2:
            lista_resultado.append(elemento)

    # Segunda parte: elementos em lista2 que não estão em lista1
    for elemento in lista2:
        if elemento not in lista1:
            lista_resultado.append(elemento)

    return lista_resultado

lista1 = []
lista2 = []

i = 0
j = 0

# Loop para solicitar números para a primeira lista
print(Fore.YELLOW + "\n--- Preenchendo a PRIMEIRA Lista (5 números) ---" + Style.RESET_ALL)
while i < 5:
    try:
        numeroLista1 = int(input(Fore.BLUE + f"Digite o {i+1}º número para a Lista 1: " + Style.RESET_ALL))
        if numeroLista1 in lista1:
            print(Fore.RED + f"O número {numeroLista1} já foi digitado na Lista 1. Por favor, digite um número diferente." + Style.RESET_ALL)
        else:
            lista1.append(numeroLista1)
            i += 1
    except ValueError:
        print(Fore.RED + "Entrada inválida. Por favor, digite apenas números inteiros." + Style.RESET_ALL)

print(Fore.YELLOW + "\n" + "=" * largura + Style.RESET_ALL) # Uma linha de separação visual
print(Fore.YELLOW + "--- Preenchendo a SEGUNDA Lista (5 números) ---" + Style.RESET_ALL)

# Loop para solicitar números para a segunda lista
while j < 5:
    try:
        numeroLista2 = int(input(Fore.GREEN + f"Digite o {j+1}º número para a Lista 2: " + Style.RESET_ALL))
        if numeroLista2 in lista2:
            print(Fore.RED + f"O número {numeroLista2} já foi digitado na Lista 2. Por favor, digite um número diferente." + Style.RESET_ALL)
        else:
            lista2.append(numeroLista2)
            j += 1
    except ValueError:
        print(Fore.RED + "Entrada inválida. Por favor, digite apenas números inteiros." + Style.RESET_ALL)

lista_resultado = lista_dupla(lista1, lista2) # Chama a função para obter a lista resultante com elementos únicos de ambas as listas

print(Fore.YELLOW + "\n-------- Resultados --------" + Style.RESET_ALL) # Corrigi a cor aqui de YELOW para YELLOW
print(Fore.GREEN + f"\nLista resultante (elementos únicos de ambas as listas): {lista_resultado}" + Style.RESET_ALL)
print(Fore.MAGENTA + f"Quantidade de elementos únicos encontrados: {len(lista_resultado)}" + Style.RESET_ALL)
print(Fore.WHITE + f"Lista 1: {lista1}" + Style.RESET_ALL)
print(Fore.WHITE + f"Lista 2: {lista2}" + Style.RESET_ALL)
print(Fore.CYAN + "\n-------- Programa encerrado. --------\n".center(largura - 2) + Style.RESET_ALL)