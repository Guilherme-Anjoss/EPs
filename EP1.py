from os import system, name
#Exemplos de cores que podem ser usadas no terminal:
# GRAY    = '\033[30m'
# RED     = '\033[31m'
# GREEN   = '\033[32m'
# YELLOW  = '\033[33m'
# BLUE    = '\033[34m'
# VIOLET  = '\033[35m'
# CYAN    = '\033[36m'
# WHITE   = '\033[37m'

def limpaTela():
    """
    Função que limpa a tela do terminal quando finaliza algumas etapas da execução do programa.
    """
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def Pagamento(o, pag, valor):
    """
    o = opção que o usuário escolheu na tela de opções da função Opções()
    pag = o pagamento pelo produto digitado na função Maquina()
    valor = o preço do produto que o usuário escolheu
    Essa função recebe a opção do usuário, o pagamento, e o valor do produto escolhido, calcula e valida o pagamento(caso o dinheiro inserido não seja o suficiente o programa pede para inserir mais dinheiro) e caso tenha troco entrega o troco nota por nota. 
    """
    GREEN   = '\033[32m'
    RED     = '\033[31m'
    print(RED)
    if pag < valor:
        pag2 = float(input("Pagamento insuficiente! Adicione mais dinheiro: "))
        Pagamento(o, pag + pag2, valor)
    troco = pag - valor 
    print(GREEN)
    if troco == 0:
        print(f"Valor pago: R${pag}\n")
        print("Obrigado pela compra!")
    if troco > 0:
        print(f"Valor pago: R${pag}\n")
        print(f"O seu troco é de R${troco:.2f}")
        print("Pegue o seu troco:")
        if troco >= 100:
            qtnota = int(troco) // 100
            print(f'R$100,00\n'*qtnota) if qtnota > 1 else print('R$100,00')
            troco -= qtnota * 100
        if troco >= 50:
            qtnota = int(troco) // 50
            print(f'R$50,00\n'*qtnota) if qtnota > 1 else print('R$50,00')
            troco -= qtnota * 50
        if troco >= 20:
            qtnota = int(troco) // 20
            print(f'R$20,00\n'*qtnota) if qtnota > 1 else print('R$20,00')
            troco -= qtnota * 20
        if troco >= 10:
            qtnota = int(troco) // 10
            print(f'R$10,00\n'*qtnota) if qtnota > 1 else print('R$10,00')
            troco -= qtnota * 10
        if troco >= 5:
            qtnota = int(troco) // 5
            print(f'R$5,00\n'*qtnota) if qtnota > 1 else print('R$5,00')
            troco -= qtnota * 5
        if troco >= 2:
            qtnota = int(troco) // 2
            print(f'R$2,00\n'*qtnota) if qtnota > 1 else print('R$2,00')
            troco -= qtnota * 2
        if troco >= 1:
            qtnota = int(troco) // 1
            print(f'R$1,00\n'*qtnota) if qtnota > 1 else print('R$1,00')
            troco -= qtnota * 1
            troco += 0.001
        troco += 0.001
        if troco >= 0.5:
            qtnota = int(troco) / 0.5
            print(f'R$0,50\n'*qtnota) if qtnota > 1 else print('R$0,50')
            troco -= 0.5
        if troco >= 0.25:
            qtnota = int(troco) / 0.25
            print(f'R$0,25\n'*qtnota) if qtnota > 1 else print('R$0,25')
            troco -= 0.25
        qtnota = 0
        if troco >= 0.10:
            troco -= 0.10
            qtnota += 1
            print(f'R$0,10\n') if qtnota > 1 else print('R$0,10')
            if troco >= 0.10:
                troco -= 0.10
                qtnota += 1
                print(f'R$0,10\n') if qtnota > 1 else print('R$0,10')
        if troco >= 0.05:
            troco -= 0.05
            print(f'R$0,05\n') if qtnota > 1 else print('R$0,05')
        if troco >= 0.04:
            print(f'R$0,01\n'*4) if qtnota > 1 else print('R$0,01')
        if troco >= 0.03:
            print(f'R$0,01\n'*3) if qtnota > 1 else print('R$0,01')
        if troco >= 0.02:
            print(f'R$0,01\n'*2) if qtnota > 1 else print('R$0,01')
        if troco >= 0.01:
            print(f'R$0,01\n') if qtnota > 1 else print('R$0,01')
        print("\nObrigado pela compra!")

def Informaçoes(copos, cafe, leite, agua, gelo, solvente, chocolate, faturamento):
    """
    Essa função recebe as informaçãoes internas calculadas pela função Maquina() e depois imprime as informações internas da maquina.
    """
    BLUE = '\033[34m'
    print(BLUE)
    print("\nInformações Internas ->")
    print(f"\nCopos: {copos}\nÁgua: {agua}ml\nCafé solúvel: {cafe}g\nLeite em Pó: {leite}g\nCubos de gelo: {gelo}\nSolvente descafeínante: {solvente}g\nChocolate: {chocolate}g\nFaturamento: R${faturamento:.2f}")

def Maquina(copos, cafe, leite, agua, gelo, solvente, chocolate, faturamento = 0):
    """
    Essa função armazena o estoque de ingredientes dos produtos, recebe a opção e o pagamento do cliente. A função também e encarregada de fazer as vendas e calcular o faturamento da maquina e a quantidade de ingredientes no estoque depois de uma venda.
    """
    RED = '\033[31m'
    BLUE = '\033[34m'
    YELLOW = '\033[33m'
    GREEN   = '\033[32m'
    Opções(copos, cafe, leite, agua, gelo, solvente, chocolate, faturamento = 0)
    print(YELLOW)
    o = int(input("Escolha uma opção: "))
    if o == 8:
        Informaçoes(copos, cafe, leite, agua, gelo, solvente, chocolate, faturamento)
        exit("\nObrigado e volte sempre!\n")
    elif o == 6:
        print(BLUE)
        print("\nInformações dos Produtos ->")
        print("\nCafé Expresso: R$3,00\n- 7g de café solúvel\n- 30ml de água")
        print("\nCafé com Leite: R$4,50\n- 10g de café solúvel\n- 30g de leite em pó\n- 200ml de água")
        print("\nCafé Gelado: R$7,65\n- 7g de café solúvel\n- 100ml de água\n- 20g de leite em pó\n- 6 cubos de gelo")
        print("\nCafé Descafeínado: R$6.50\n- 10g de café solúvel\n- 250ml de água\n- 5g de solvente descafeínante")
        print("\nChocolate Quente: R$9,00\n- 50g de chocolate\n- 25g de leite em pó\n- 150ml de água")
        print(RED)
        continua = input("Desaja continuar comprando? [S/N] ")
        if continua == "S":
            Maquina(copos, cafe, leite, agua, gelo, solvente, chocolate, faturamento)
        else:
            Informaçoes(copos, cafe, leite, agua, gelo, solvente, chocolate, faturamento)
            exit("\nObrigado e volte sempre!\n")
    elif o == 7:
        Informaçoes(copos, cafe, leite, agua, gelo, solvente, chocolate, faturamento)
        print(RED)
        continua = input("Desaja continuar comprando? [S/N] ")
        if continua == "S":
            Maquina(copos, cafe, leite, agua, gelo, solvente, chocolate, faturamento)
        else:
            Informaçoes(copos, cafe, leite, agua, gelo, solvente, chocolate, faturamento)
            exit("\nObrigado e volte sempre!\n")
    elif o == 1:
        valor = 3.00
        print(BLUE)
        print("\n1 - Café Expresso......R$3,00")
        print(GREEN)
        pag = float(input("Digite o pagamento: "))
        Pagamento(o, pag, valor)
        print(RED)
        continua = input("Desaja continuar comprando? [S/N] ")
        if continua == "S":
            Maquina(copos - 1, cafe - 7, leite, agua - 30, gelo, solvente, chocolate, faturamento + 3.00)
        else:
            Informaçoes(copos - 1, cafe - 7, leite, agua - 30, gelo, solvente, chocolate, faturamento + 3.00)
            exit("\nObrigado e volte sempre!\n")
    elif o == 2:
        valor = 4.50
        print(BLUE)
        print("\n2 - Café com leite.....R$4,50")
        print(GREEN)
        pag = float(input("Digite o seu pagamento: "))
        Pagamento(o, pag, valor)
        print(RED)
        continua = input("Desaja continuar comprando? [S/N] ")
        if continua == "S":
            Maquina(copos - 1, cafe -10, leite - 30, agua - 200, gelo, solvente, chocolate, faturamento + 4.50)
        else:
            Informaçoes(copos - 1, cafe -10, leite - 30, agua - 200, gelo, solvente, chocolate, faturamento + 4.50)
            exit("\nObrigado e volte sempre!\n")
        
    elif o == 3:
        valor = 7.65
        print(BLUE)
        print("\n3 - Café Gelado........R$7.65")
        print(GREEN)
        pag = float(input("Digite o seu pagamento: "))
        Pagamento(o, pag, valor)
        print(RED)
        continua = input("Desaja continuar comprando? [S/N] ")
        if continua == "S":
            Maquina(copos - 1, cafe - 7, leite - 20, agua - 100, gelo - 6, solvente, chocolate, faturamento + 7.65)
        else:
            Informaçoes(copos - 1, cafe - 7, leite - 20, agua - 100, gelo - 6, solvente, chocolate, faturamento + 7.65)
            exit("\nObrigado e volte sempre!\n")
        
    elif o == 4:
        valor = 6.50
        print(BLUE)
        print("\n4 - Café Descafeinado ..R$6,50")
        print(GREEN)
        pag = float(input("Digite o seu pagamento: "))
        Pagamento(o, pag, valor)
        print(RED)
        continua = input("Desaja continuar comprando? [S/N] ")
        if continua == "S":
            Maquina(copos - 1, cafe - 10, leite, agua - 250, gelo, solvente - 5, chocolate, faturamento + 6.50)
        else:
            Informaçoes(copos - 1, cafe - 10, leite, agua - 250, gelo, solvente - 5, chocolate, faturamento + 6.50)
            exit("\nObrigado e volte sempre!\n")
    elif o == 5:
        valor = 9.00
        print(BLUE)
        print("\n4 - Chocolate Quente....R$9,00")
        print(GREEN)
        pag = float(input("Digite o seu pagamento: "))
        Pagamento(o, pag, valor)
        print(RED)
        continua = input("Desaja continuar comprando? [S/N] ")
        if continua == "S":
            Maquina(copos - 1, cafe, leite - 25, agua - 150, gelo, solvente, chocolate - 50, faturamento + 9.00)
        else:
            Informaçoes(copos - 1, cafe, leite - 25, agua - 150, gelo, solvente, chocolate - 50, faturamento + 9.00)
            exit("\nObrigado e volte sempre!\n")

def Opções(copos, cafe, leite, agua, gelo, solvente, chocolate, faturamento = 0):
    """
    Essa função é encarregada de imprimir a tabela de preços e as opções de funcionamento da maquina.
    """
    CYAN = '\033[36m'
    YELLOW = '\033[33m'
    VIOLET = '\033[35m'
    limpaTela()
    print(VIOLET)
    print("/"*44)
    print("/             COFFEE MACHINE               /")
    print("/"*44)
    print(f"\n{YELLOW}:=:=:=:=:=:=:=:= PRODUTOS =:=:=:=:=:=:=:=:=:")
    print(f"{YELLOW}|                                          |")
    print(f"{YELLOW}|{CYAN} 1 - Café Expresso.................R$3,00 {YELLOW}|") if  copos >= 1 and agua >= 30 and cafe >= 7 else print(f"{YELLOW}|{CYAN} 1 - Café Expresso...........Indisponível {YELLOW}|")
    print(f"{YELLOW}|{CYAN} 2 - Café com Leite................R$4,50 {YELLOW}|") if copos >= 1 and agua >= 200 and leite >= 30 else print(f"{YELLOW}|{CYAN} 2 - Café com Leite..........Indisponível {YELLOW}|")
    print(f"{YELLOW}|{CYAN} 3 - Café Gelado...................R$7,65 {YELLOW}|") if copos >= 1 and agua >= 100 and cafe >= 7 and leite >= 20 and gelo >= 6 else print(f"{YELLOW}|{CYAN} 3 - Café Gelado.............Indisponível {YELLOW}|")
    print(f"{YELLOW}|{CYAN} 4 - Café Descafeínado.............R$6,50 {YELLOW}|") if copos >= 1 and agua >= 250 and cafe >= 10 and solvente >= 5 else print(f"{YELLOW}|{CYAN} 4 - Café Descafeínado.......Indisponível {YELLOW}|")
    print(f"{YELLOW}|{CYAN} 5 - Chocolate Quente..............R$9,00 {YELLOW}|") if copos >= 1 and agua >= 150 and leite >= 25 and chocolate >= 50 else print(f"{YELLOW}|{CYAN} 5 - Chocolate Quente........Indisponível {YELLOW}|")
    print(f"{YELLOW}|                                          |")
    print(f"{YELLOW}|=:=:=:=:=:=:= OUTRAS OPÇÕES :=:=:=:=:=:=:=|")
    print(f"{YELLOW}|                                          |")
    print(f"{YELLOW}|{CYAN} 6 - Informações dos Produtos             {YELLOW}|")
    print(f"{YELLOW}|{CYAN} 7 - Informações Internas                 {YELLOW}|")
    print(f"{YELLOW}|{CYAN} 8 - Finalizar                            {YELLOW}|")
    print(f"{YELLOW}|                                          |")
    print(":=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=::")
    if copos == 0:
        print("\nINFELIZMENTE A MÁQUINA ESTÁ SEM COPOS SUFICIENTES!")
    if agua < 30:
        print("\nINFELIZMENTE A MÁQUINA ESTÁ SEM ÁGUA SUFICIENTE!")
    if copos == 0 and agua < 30:
        print("\nINFELIZMENTE A MÁQUINA ESTÁ SEM AGUA E COPOS SUFICIENTE!")

def main():
    Maquina(10, 200, 200, 1200, 25, 15, 200)

main()