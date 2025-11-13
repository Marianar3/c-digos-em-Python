
import random
import time

def exibir_saldo(saldo):
    """Exibe o saldo atual do jogador de forma formatada."""
    print(f"\n--- Seu Saldo Atual: R$ {saldo:.2f} ---")

def jogar_roleta(saldo, valor_aposta):
    """Simula uma rodada na roleta da casa de apostas."""
    if valor_aposta > saldo:
        print("Você não tem saldo suficiente para essa aposta!")
        return saldo

    print("\n--- Jogando na Roleta ---")
    print("Escolha um número de 0 a 36.")
    escolha_jogador = input("Digite seu número: ")

    try:
        escolha_jogador = int(escolha_jogador)
        if not (0 <= escolha_jogador <= 36):
            print("Número inválido. Escolha entre 0 e 36.")
            return saldo
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        return saldo

    print("Girando a roleta...")
    time.sleep(1)
    numero_sorteado = random.randint(0, 36)
    print(f"A roleta parou no número: {numero_sorteado}")

    if escolha_jogador == numero_sorteado:
        ganho = valor_aposta * 36  # Pagamento clássico da roleta (35:1 + stake)
        print(f"Parabéns! Você acertou! Ganhou R$ {ganho:.2f}!")
        return saldo + ganho
    else:
        print(f"Que pena! Você perdeu R$ {valor_aposta:.2f}.")
        return saldo - valor_aposta

def simular_investimento(saldo, valor_investido):
    """Simula um investimento com retorno variável."""
    if valor_investido > saldo:
        print("Você não tem saldo suficiente para investir esse valor!")
        return saldo

    print("\n--- Simulando Investimento ---")
    print("Seu dinheiro está sendo investido em um fundo de ações...")
    time.sleep(1.5)

    # Simula o retorno do investimento (pode ser positivo ou negativo)
    chance_sucesso = random.random() # Gera um número entre 0.0 e 1.0

    if chance_sucesso < 0.6: # 60% de chance de um retorno positivo moderado
        retorno = valor_investido * random.uniform(1.05, 1.15) # Retorno entre 5% e 15%
        print(f"Seu investimento rendeu! Ganhou R$ {retorno - valor_investido:.2f}.")
        return saldo + (retorno - valor_investido)
    elif chance_sucesso < 0.85: # 25% de chance de um retorno baixo ou sem retorno
        retorno = valor_investido * random.uniform(0.98, 1.02) # Retorno entre -2% e 2%
        print(f"Seu investimento teve um retorno pequeno ou neutro. Mudança: R$ {retorno - valor_investido:.2f}.")
        return saldo + (retorno - valor_investido)
    else: # 15% de chance de uma perda moderada
        perda = valor_investido * random.uniform(0.85, 0.95) # Perda entre 5% e 15%
        print(f"Seu investimento teve uma pequena perda de R$ {valor_investido - perda:.2f}.")
        return saldo - (valor_investido - perda)

def menu_principal(saldo):
    """Exibe o menu principal e gerencia as ações do jogador."""
    while True:
        exibir_saldo(saldo)
        print("\nO que você deseja fazer?")
        print("1. Apostar na roleta (Alto Risco, Alto Retorno)")
        print("2. Investir (Risco Moderado, Retorno Variável)")
        print("3. Ver meu Patrimônio (Estratégia de Longo Prazo)")
        print("4. Sair do Jogo")

        escolha = input("Digite o número da sua escolha: ")

        if escolha == '1':
            try:
                valor_aposta = float(input("Quanto você quer apostar na roleta? R$ "))
                saldo = jogar_roleta(saldo, valor_aposta)
            except ValueError:
                print("Por favor, digite um valor numérico válido.")
        elif escolha == '2':
            try:
                valor_investimento = float(input("Quanto você quer investir? R$ "))
                saldo = simular_investimento(saldo, valor_investimento)
            except ValueError:
                print("Por favor, digite um valor numérico válido.")
        elif escolha == '3':
            print("\n--- Análise de Patrimônio ---")
            print(f"Seu patrimônio total é de R$ {saldo:.2f}.")
            if saldo < 1000:
                print("Você ainda está no começo da sua jornada financeira. Continue poupando e investindo!")
            elif saldo < 5000:
                print("Bom progresso! Mantenha a disciplina e explore investimentos com riscos calculados.")
            else:
                print("Excelente! Você está construindo um patrimônio sólido. Continue focado nos seus objetivos!")
            time.sleep(2)
        elif escolha == '4':
            print("\nObrigado por jogar! Lembre-se: a educação financeira é o melhor investimento!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# --- Início do Jogo ---
print("Bem-vindo ao 'Dinheiro ou Azar'!")
print("O jogo onde você decide se confia no seu planejamento ou na sorte das apostas.")

saldo_inicial = 1000.00
saldo_jogador = saldo_inicial

menu_principal(saldo_jogador)
