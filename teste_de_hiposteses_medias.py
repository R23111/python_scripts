####################################################################################################
#                                                                                                  #
#          Programa feito para verificação de respostas de uma lista de exercícios da UFRGS.       #
#   Program (wrote in portuguese) as a tool to check my answers from UFRGS course's exercise list  #
#                                                                                                  #
####################################################################################################


import os
from sys import platform
import scipy.stats
from scipy import special
import math


def clear_scr():
    if(platform == "linux" or platform == "linux2"):
        os.system('clear')
    elif(platform == "win32"):
        os.system('cls')


# Caso 1.a)
def um_pop():
    clear_scr()
    print("Comparação entre uma média e um valor padrão\n")
    print("O Desvio padrão vem da população.\n")

    Ha = input("Tipo de Ha (μ [>, !=, <] μ_0): ")
    alpha = float(input("Erro aceitável = "))
    Xm = float(input("Valor médio da amostra = "))
    mi = float(input("Valor Padrão = "))
    sigma = float(input("Sigma = "))
    n = int(input("Tamanho da amostra = "))

    Z = (Xm - mi) / (sigma / math.sqrt(n))

    sinal = Z/abs(Z)

    # print((scipy.stats.norm(0, 1).cdf(-1.5)))

    if(Ha == "!="):
        alpha = alpha/2

    # tabela de distribuição normal
    lim = abs(scipy.stats.norm(0, 1).ppf(alpha))

    if(Ha == "!="):
        alpha = alpha*2

    clear_scr()

    if(abs(Z) > lim):
        print(
            f"\n\n============================================================\n\n\t Foi possível, ao nível {alpha * 100}%, confirmar Ha. \n\n============================================================\n\n")
        print(f"Ho: μ = {mi} é falsa. \nHa: μ {Ha} {mi} é verdadeira.\n")
        print(
            f"Dados: \n\t Z = {Z} \n\t Zα = {lim * sinal} \n\t Nível de Significância α = {alpha * 100}%\n\n\n")

    else:
        print(
            f"\n\n============================================================\n\n\t Não foi possível, ao nível {alpha * 100}%, confirmar Ha. \n\n============================================================\n\n")
        print(f"Ho: μ = {mi} é verdadeira. \nHa: μ {Ha} {mi} é falsa.\n")
        print(
            f"Dados: \n\t Z = {Z} \n\t Zα = {lim * sinal} \n\t Nível de Significância α = {alpha * 100}%\n\n\n")


# Caso 1.b)
def um_amostra():
    clear_scr()
    print("Comparação entre uma média e um valor padrão\n")
    print("O Desvio padrão vem da amostra.\n")

    Ha = input("Tipo de Ha (μ [>, !=, <] μ_0): ")
    alpha = float(input("Erro aceitável = "))
    Xm = float(input("Valor médio da amostra = "))
    mi = float(input("Valor Padrão = "))
    S = float(input("S = "))
    n = int(input("Tamanho da amostra = "))

    T = (Xm - mi) / (S / math.sqrt(n))

    sinal = T/abs(T)

    if(Ha == "!="):
        alpha = alpha/2

    # tabela t de Student
    lim = abs(scipy.stats.t.ppf(alpha, n - 1))

    if(Ha == "!="):
        alpha = alpha*2

    clear_scr()

    if(abs(T) > lim):
        print(
            f"\n\n============================================================\n\n\t Foi possível, ao nível {alpha * 100}%, confirmar Ha. \n\n============================================================\n")
        print(f"Ho: μ = {mi} é falsa. \nHa: μ {Ha} {mi} é verdadeira.\n")
        print(
            f"Dados: \n\t T = {T} \n\t Tν = {lim * sinal} \n\t Nível de Significância α = {alpha * 100}%\n\n\n")

    else:
        print(
            f"\n\n============================================================\n\n\t Não foi possível, ao nível {alpha * 100}%, confirmar Ha. \n\n============================================================\n\n")
        print(f"Ho: μ = {mi} é verdadeira. \nHa: μ {Ha} {mi} é falsa.\n")
        print(
            f"Dados: \n\t T = {T} \n\t Tν = {lim * sinal} \n\t Nível de Significância α = {alpha * 100}%\n\n\n")


# Caso 2.a)
def dois_conhecidos():
    clear_scr()
    print("Comparação entre duas médias, e de σ conhecidos\n")

    Ha = input("Tipo de Ha (Xm1 [>, !=, <] Xm2): ")
    alpha = float(input("Erro aceitável = "))
    Xm1 = float(input("Valor médio da amostra 1 = "))
    Xm2 = float(input("Valor médio da amostra 2 = "))
    sigma1 = float(input("Sigma 1 = "))
    sigma2 = float(input("Sigma 2 = "))
    n1 = int(input("Tamanho da amostra 1 = "))
    n2 = int(input("Tamanho da amostra 2 = "))

    Z = (Xm1 - Xm2) / math.sqrt((sigma1**2 / n1) + (sigma2**2 / n2))

    sinal = Z/abs(Z)

    if(Ha == "!="):
        alpha = alpha/2

    # tabela de distribuição normal
    lim = abs(scipy.stats.norm(0, 1).ppf(alpha))

    if(Ha == "!="):
        alpha = alpha*2

    clear_scr()

    if(abs(Z) > lim):
        print(
            f"\n\n============================================================\n\n\t Foi possível, ao nível {alpha * 100}%, confirmar Ha. \n\n============================================================\n\n")
        print(
            f"Ho: μ1 = μ2 é falsa. \nHa: μ1 {Ha} μ2 é verdadeira.\n")
        print(
            f"Dados: \n\t Z = {Z} \n\t Zα = {lim * sinal} \n\t Nível de Significância α = {alpha * 100}%\n\n\n")

    else:
        print(
            f"\n\n============================================================\n\n\t Não foi possível, ao nível {alpha * 100}%, confirmar Ha. \n\n============================================================\n\n")
        print(
            f"Ho: μ1 = μ2 é verdadeira. \nHa: μ1 {Ha} μ2 é falsa.\n")
        print(
            f"Dados: \n\t Z = {Z} \n\t Zα = {lim * sinal} \n\t Nível de Significância α = {alpha * 100}%\n\n\n")


# Caso 2.b)
def dois_iguais():
    clear_scr()
    print("Comparação entre duas médias, e de σ desconhecidos, mas supostos como iguais\n")

    Ha = input("Tipo de Ha (Xm1 [>, !=, <] Xm2): ")
    alpha = float(input("Erro aceitável = "))
    Xm1 = float(input("Valor médio da amostra 1 = "))
    Xm2 = float(input("Valor médio da amostra 2 = "))
    S1 = float(input("S1 = "))
    S2 = float(input("S2 = "))
    n1 = int(input("Tamanho da amostra 1 = "))
    n2 = int(input("Tamanho da amostra 2 = "))

    ni = (n1 - 1) + (n2 - 1)

    S = ((S1 * (n1 - 1)) + S2 * (n2 - 1)) / ni

    T = (Xm1 - Xm2) / math.sqrt(((1/n1) + (1/n2)) * S)

    sinal = T/abs(T)

    if(Ha == "!="):
        alpha = alpha/2

    # tabela t de Student
    lim = abs(scipy.stats.t.ppf(alpha, ni))

    if(Ha == "!="):
        alpha = alpha*2

    clear_scr()

    if(abs(T) > lim):
        print(
            f"\n\n============================================================\n\n\t Foi possível, ao nível {alpha * 100}%, confirmar Ha. \n\n============================================================\n")
        print(f"Ho: μ1 = μ2 é falsa. \nHa: μ1 {Ha} μ2 é verdadeira.\n")
        print(
            f"Dados: \n\t T = {T} \n\t Tν = {lim * sinal} \n\t Nível de Significância α = {alpha * 100}%\n\n\n")

    else:
        print(
            f"\n\n============================================================\n\n\t Não foi possível, ao nível {alpha * 100}%, confirmar Ha. \n\n============================================================\n\n")
        print(f"Ho: μ1 = μ2 é verdadeira. \nHa: μ1 {Ha} μ2 é falsa.\n")
        print(
            f"Dados: \n\t T = {T} \n\t Tν = {lim * sinal} \n\t Nível de Significância α = {alpha * 100}%\n\n\n")


# Caso 2.c)
def dois_diferentes():
    clear_scr()
    print("Comparação entre duas médias, e de σ desconhecidos, mas supostos como iguais\n")

    Ha = input("Tipo de Ha (Xm1 [>, !=, <] Xm2): ")
    alpha = float(input("Erro aceitável = "))
    Xm1 = float(input("Valor médio da amostra 1 = "))
    Xm2 = float(input("Valor médio da amostra 2 = "))
    S1 = float(input("S1 = "))
    S2 = float(input("S2 = "))
    n1 = int(input("Tamanho da amostra 1 = "))
    n2 = int(input("Tamanho da amostra 2 = "))

    ni = ((S1/n1) + (S2/n2))**2 / \
        ((((S1/n1)**2)/(n1-1)) + (((S2/n2)**2)/(n2-1)))

    T = (Xm1 - Xm2) / math.sqrt((S1/n1) + (S2/n2))

    sinal = T/abs(T)

    if(Ha == "!="):
        alpha = alpha/2

    # tabela t de Student
    lim = abs(scipy.stats.t.ppf(alpha, int(ni)))

    if(Ha == "!="):
        alpha = alpha*2

    clear_scr()

    if(abs(T) > lim):
        print(
            f"\n\n============================================================\n\n\t Foi possível, ao nível {alpha * 100}%, confirmar Ha. \n\n============================================================\n")
        print(f"Ho: μ1 = μ2 é falsa. \nHa: μ1 {Ha} μ2 é verdadeira.\n")
        print(
            f"Dados: \n\t T = {T} \n\t Tν = {lim * sinal} \n\t Nível de Significância α = {alpha * 100}%\n\n\n")

    else:
        print(
            f"\n\n============================================================\n\n\t Não foi possível, ao nível {alpha * 100}%, confirmar Ha. \n\n============================================================\n\n")
        print(f"Ho: μ1 = μ2 é verdadeira. \nHa: μ1 {Ha} μ2 é falsa.\n")
        print(
            f"Dados: \n\t T = {T} \n\t Tν = {lim * sinal} \n\t Nível de Significância α = {alpha * 100}%\n\n\n")


def variancia():
    clear_scr()
    v = []
    n = int(input("Tamanho da amostra: "))

    clear_scr()

    for i in range(n):
        v.append(float(input()))

    sum = 0

    for i in range(n):
        sum += v[i]

    media = sum / n

    varsum = 0

    for i in range(n):
        varsum += (v[i] - media)**2

    variancia = varsum / n

    clear_scr()

    print(
        f"\n\n============================================================\n\n\t Média = {media} \n\t Variancia = {variancia}\n\n============================================================\n\n")


def options():
    clear_scr()

    print("TESTE DE HIPOTESES MÉDIAS \n\n")

    option = int(input("Uma [1] ou duas [2] médias?\n>> "))

    if(option == 1):
        clear_scr()
        option = int(
            input("O desvio vem da pupulação [1] ou da amostra [2]\n>> "))
        if(option == 1):
            um_pop()  # Caso 1.a) -> referencia à minhas anotações pessoais
            return
        elif(option == 2):
            um_amostra()  # Caso 1.b)
            return
        else:
            print("invalid option")

    if(option == 2):
        clear_scr()
        option = int(
            input("Os desvios são conhecidos? Sim [1] ou Nao [2]\n>> "))
        if(option == 1):
            dois_conhecidos()  # Caso 2.a)
            return
        elif(option == 2):
            clear_scr()
            option = int(
                input("Os desvios sao iguais [1] ou diferentes [2]?\n>> "))
            if(option == 1):
                dois_iguais()  # Caso 2.b)
                return
            elif(option == 2):
                dois_diferentes()  # Caso 2.c)
                return
            else:
                print("invalid option")
        else:
            print("invalid option")
    else:
        print("invalid option")

    input("\n\nPrecione Enter para continuar...")
    return


if __name__ == "__main__":
    while(True):
        clear_scr()
        op = int(
            input("[1] Variancias e Média \n[2] Testes de Hipóteses Médias \n[3] Sair\n>> "))
        if(op == 1):
            variancia()
        elif(op == 2):
            options()
        elif(op == 3):
            clear_scr()
            break
        input("\n\nPrecione Enter para continuar...")
