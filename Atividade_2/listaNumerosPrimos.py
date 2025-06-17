from colorama import init, Fore, Style

init(autoreset=True)

largura = 40

print(Fore.YELLOW + "╔" + "═" * (largura - 2) + "╗")
print(Fore.CYAN + "║" + " LISTA DE NÚMEROS PRIMOS ".center(largura - 2) + "║")
print(Fore.YELLOW + "╚" + "═" * (largura - 2) + "╝")

def lista_primos(numeros): # Função que recebe uma lista de números e retorna uma lista com os números primos.
    primos = [] # Lista para armazenar os números primos 
    for numero in numeros: # Percorre cada número na lista 
        if numero > 1: # Verifica se o número é maior que 1, pois números menores ou iguais a 1 não são primos
            for i in range(2, int(numero**0.5) + 1): # Verifica se o número é divisível por algum número entre 2 e a raiz quadrada do número 
                if numero % i == 0: # Se o número for divisível por algum desses números, não é primo
                    break 
            else: # Se não encontrou nenhum divisor, o número é primo
                primos.append(numero) 
    return primos

numeros_digitados = [] 
i = 0
while i < 10: # Loop para solicitar 10 números únicos ao usuário
    try: # Solicita um número ao usuário
        numero = int(input(Fore.BLUE + f"Digite o {i+1}º número (Único): " + Style.RESET_ALL)) # Solicita um número ao usuário

        if numero in numeros_digitados: # Verifica se o número já foi digitado
            print(Fore.RED + f"O número {numero} já foi digitado. Por favor, digite um número diferente." + Style.RESET_ALL) # Se o número já foi digitado, solicita um novo número
        else: 
            numeros_digitados.append(numero) # Adiciona o número à lista de números digitados
            i += 1 # Incrementa o contador apenas se o número for único 
    except ValueError: # Trata a exceção caso o usuário digite algo que não seja um número inteiro
        print(Fore.RED + "Entrada inválida. Por favor, digite apenas números inteiros." + Style.RESET_ALL) 

numeros_primos = lista_primos(numeros_digitados) # Chama a função para filtrar os números primos
print(Fore.GREEN + f"\nLista com os números primos: {numeros_primos}" + Style.RESET_ALL)
print(Fore.GREEN + f"Quantidade de números primos encontrados: {len(numeros_primos)}" + Style.RESET_ALL)
print(Fore.GREEN + f"Lista de números digitados (únicos e na ordem): {numeros_digitados}" + Style.RESET_ALL)  

print(Fore.CYAN + "\n-------- Programa encerrado. --------\n".center(largura - 2) + Style.RESET_ALL)