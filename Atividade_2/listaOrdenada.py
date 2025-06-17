from colorama import init, Fore, Style

init(autoreset=True)

largura = 40

print(Fore.YELLOW + "╔" + "═" * (largura - 2) + "╗")
print(Fore.CYAN + "║" + " LISTA ORDENADA ".center(largura - 2) + "║")
print(Fore.YELLOW + "╚" + "═" * (largura - 2) + "╝")


lista_de_pessoas = []

def ordenar_lista(lista_pessoas):
    return sorted(lista_pessoas)
while True: 
    try:
        nome = input(Fore.BLUE + "Digite o nome da pessoa (ou 'sair' para encerrar): " + Style.RESET_ALL).strip()
        if nome.lower() == 'sair':
            break
        idade = int(input(Fore.GREEN + "Digite a idade da pessoa: " + Style.RESET_ALL))
        lista_de_pessoas.append((nome, idade))
    except ValueError:
        print(Fore.RED + "Entrada inválida. Por favor, digite uma idade válida." + Style.RESET_ALL)
lista_ordenada = ordenar_lista(lista_de_pessoas)
print(Fore.YELLOW + "\nLista de pessoas ordenada por nome:")
for pessoa in lista_ordenada:
    print(Fore.CYAN + f"Nome: {pessoa[0]}, Idade: {pessoa[1]}" + Style.RESET_ALL)
print(Fore.WHITE + "\n-------- Programa encerrado. --------\n".center(largura - 2) + Style.RESET_ALL)