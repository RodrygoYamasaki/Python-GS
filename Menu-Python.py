# Definição das listas e variáveis globais
baterias = [50, 30, 70]  # Simulando 3 baterias de "segunda vida", com capacidades iniciais
historico_geracao = []  # Lista que armazena o histórico de geração de energia
degradacao_bateria = [0.05, 0.03, 0.07]  # Taxa de degradação das baterias de "segunda vida"

def menu():
    """Função que exibe o menu principal e retorna a escolha do usuário."""
    print("\n--- Sistema de Armazenamento de Energia ---")
    print("1. Exibir Status das Baterias (Degradadas e Capacidade Atual)")
    print("2. Adicionar Energia ao Sistema (Armazenamento)")
    print("3. Remover Energia do Sistema (Descarregar)")
    print("4. Gerar Energia a partir de Fontes Renováveis (Solar e Eólica)")
    print("5. Exibir Histórico de Geração de Energia")
    print("6. Sair")
    opcao = int(input("Escolha uma opção: "))
    return opcao

def adicionar_energia(baterias, energia_adicionada):
    """Função que simula a adição de energia às baterias."""
    for i in range(len(baterias)):
        if baterias[i] < 100:
            capacidade_restante = 100 - baterias[i]
            if energia_adicionada <= capacidade_restante:
                baterias[i] += energia_adicionada
                print(f"{energia_adicionada} kWh adicionados à bateria {i + 1}.")
                return
            else:
                baterias[i] = 100
                energia_adicionada -= capacidade_restante
        if energia_adicionada <= 0:
            break
    if energia_adicionada > 0:
        print("Não há espaço suficiente nas baterias para armazenar toda a energia.")
    else:
        print("Energia adicionada com sucesso.")

def remover_energia(baterias, energia_removida):
    """Função que simula a remoção de energia do sistema de baterias."""
    for i in range(len(baterias)):
        if baterias[i] >= energia_removida:
            baterias[i] -= energia_removida
            print(f"{energia_removida} kWh removidos da bateria {i + 1}.")
            return
        elif baterias[i] > 0:
            energia_removida -= baterias[i]
            baterias[i] = 0
    if energia_removida > 0:
        print("Não há energia suficiente nas baterias para a remoção solicitada.")
    else:
        print("Energia removida com sucesso.")

def exibir_status(baterias):
    """Função que exibe o status atual das baterias e sua degradação."""
    print("\n--- Status das Baterias ---")
    for i, carga in enumerate(baterias):
        print(f"Bateria {i + 1}: {carga:.2f} kWh (Degradada em {degradacao_bateria[i] * 100:.0f}%)")

def gerar_energia():
    """Função que simula a geração de energia a partir de fontes renováveis."""
    import random
    energia_gerada = random.randint(5, 20)  # Simula geração entre 5 a 20 kWh
    print(f"\nEnergia gerada: {energia_gerada} kWh")
    return energia_gerada

def degradar_baterias():
    """Função que aplica degradação às baterias de segunda vida."""
    for i in range(len(baterias)):
        degradação = baterias[i] * degradacao_bateria[i]
        baterias[i] -= degradação
        if baterias[i] < 0:
            baterias[i] = 0
        print(f"Bateria {i + 1} degradou {degradação:.2f} kWh. Nova carga: {baterias[i]:.2f} kWh.")

def iniciar_sistema():
    """Função principal que gerencia o sistema com o menu interativo."""
    while True:
        degradar_baterias()  # Aplica degradação a cada iteração do ciclo
        opcao = menu()

        if opcao == 1:
            exibir_status(baterias)
        elif opcao == 2:
            energia_adicionada = int(input("Digite a quantidade de energia a adicionar (kWh): "))
            adicionar_energia(baterias, energia_adicionada)
        elif opcao == 3:
            energia_removida = int(input("Digite a quantidade de energia a remover (kWh): "))
            remover_energia(baterias, energia_removida)
        elif opcao == 4:
            energia_gerada = gerar_energia()
            historico_geracao.append(energia_gerada)
        elif opcao == 5:
            print("\nHistórico de Geração de Energia: ", historico_geracao)
        elif opcao == 6:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o sistema
iniciar_sistema()
