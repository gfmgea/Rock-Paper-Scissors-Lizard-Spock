import random

#Função que escolhe aleatoriamente para o computador
def escolha_computador():
    """
    Essa funcao realiza a escolha aleatoria do computador nas 6 opcoes possiveis: Pedra, Papel, Tesoura, Lagarto, Spock
    """
    return random.choice(["Pedra", "Papel", "Tesoura", "Lagarto", "Spock"])

#Função com as regras que define quem vence com base nas escolhas
def determinar_vencedor(escolha_usuario, escolha_computador):
    """
    Essa funcao determina o vencedor com base na regra, como por exemplo: a pedra ganha da Tesoura e do Lagarto. O papel ganha da pedra e do Spock.
    Após isso, ela verifica se as escolhas foram iguais para empate
    E por fim, verifica se a escolha do usuario esta nas regras ganhando do computador ou nao, retornando usuario ou computador.
    """
    regras = {
        "Pedra": ["Tesoura", "Lagarto"],
        "Papel": ["Pedra", "Spock"],
        "Tesoura": ["Papel", "Lagarto"],
        "Lagarto": ["Papel", "Spock"],
        "Spock": ["Pedra", "Tesoura"]
    }
    
    if escolha_usuario == escolha_computador:
        return "Empate"
    elif escolha_computador in regras[escolha_usuario]:
        return "Usuário"
    else:
        return "Computador"

#Main
#Escolha do usuário
print("Escolha uma das opções: Pedra, Papel, Tesoura, Lagarto, Spock")
escolha_usuario = input("Sua escolha é: ").capitalize()

#Verifica se a escolha do usuário é válida dentro das opções oferecidas
opcoes_validas = ["Pedra", "Papel", "Tesoura", "Lagarto", "Spock"]
if escolha_usuario not in opcoes_validas:
    print("Escolha inválida. Tente novamente com uma escolha válida.")
else:
    #Escolha aleatória do computador
    escolha_pc = escolha_computador()
    
    #Quem vence
    vencedor = determinar_vencedor(escolha_usuario, escolha_pc)
    
    #Exibe resultados
    print(f"O computador escolheu: {escolha_pc}")
    if vencedor == "Empate":
        print("Empate!")
    else:
        print(f"O vencedor desta rodada é: {vencedor}")

#print(escolha_computador.__doc__)
#print(determinar_vencedor.__doc__)