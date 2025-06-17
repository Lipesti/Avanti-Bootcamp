from colorama import init, Fore

init(autoreset=True)

largura = 40

print(Fore.YELLOW + "╔" + "═" * (largura - 2) + "╗")
print(Fore.CYAN + "║" + " LISTA DE NÚMEROS ÍMPARES ".center(largura - 2) + "║")
print(Fore.YELLOW + "╚" + "═" * (largura - 2) + "╝")
# Função que receba uma lista de números e retorne outra lista com os números ímpares.

def filtro_impares (lista): # Função que recebe uma lista de números
    lista_impares = [] # Lista para armazenar os números ímpares
    for numero in lista: # Percorre cada número na lista
        if numero % 2 != 0: # Verifica se o número é ímpar
            lista_impares.append(numero) # Adiciona o número ímpar à lista de números ímpares
    return lista_impares # Retorna a lista de números ímpares

minha_lista_de_numeros = [] # Lista de números fornecida pelo usuário

for i in range(10): # Loop para solicitar 10 números ao usuário
    numero = int(input(f"Digite o {i+1}º número: ")) # Solicita um número ao usuário
    minha_lista_de_numeros.append(numero) # Adiciona o número à lista
numeros_impares = filtro_impares(minha_lista_de_numeros) # Chama a função para filtrar os números ímpares
print(f"\nLista com os números ímpares: {numeros_impares}") # Exibe a lista de números ímpares
print(f"Quantidade de números ímpares encontrados: {len(numeros_impares)}") # Exibe a quantidade de números ímpares encontrados
print(f"Lista de números digitados: {minha_lista_de_numeros}" ) # Exibe os números digitados
