import os
from time import sleep

def endereco_para_entrega( opcao_endereco):
    if opcao_endereco == "1":
        print("Solicitando o pedido...")
        sleep(2)
        print("O pedido será entregue para o endereço já cadastrado, muito obrigado!")
    elif opcao_endereco == "2":
        novo_endereco = input(f"Qual o novo endereço que você gostaria de entregar?{os.linesep}")
        print("Solicitando o pedido...")
        sleep(2)
        print(f"O seu pedido será entregue no endereço: {novo_endereco}, muito obrigado!")
    elif opcao_endereco == "3":
        print("Solicitando o pedido...")
        sleep(2)
        print(f"Seu pedido ficará pronto de 15 a 25 minutos, muito obrigado!")

def processar_cardapio_secudaria(opcoes_principal, opcao_secudaria):
    OPCAO_01_PRINCIAL_SECUDARIA_01 = f"[1]-Big:{os.linesep}filé, abacaxi, presunto, queijo cheddar, bacon, alface e tomate + Batata pequena + Refri 300ml.{os.linesep}"
    OPCAO_01_PRINCIAL_SECUDARIA_02 = f"[2]-BigFrango:{os.linesep}frango desfiado, presunto, queijo mussarela, bacon, milho verde, ervilha, alface e tomate) + Batata pequena + Refri 300ml."
    OPCAO_02_PRINCIPAL_SECUDARIA_01 = f"[1]-Filet mignon com cheddar.{os.linesep}"
    OPCAO_02_PRINCIPAL_SECUDARIA_02 = f"[2]-Camarão catupiry.{os.linesep}"
    OPCAO_03_PRINCIPAL_SECUDARIA_01 = f"[1]-Pizza estilo Nova York:{os.linesep}massa fininha e fatia grandona, queijo e requeijão cremoso.{os.linesep}"
    OPCAO_03_PRINCIPAL_SECUDARIA_02 = f"[2]-Frango com Requeijão:{os.linesep}Frango, queijo Hut e requeijão cremoso"
    if opcoes_principal == "1" and opcao_secudaria == "1":
        print(f"Seu pedido:{os.linesep}{OPCAO_01_PRINCIAL_SECUDARIA_01}")
    elif opcoes_principal =="1" and opcao_secudaria == "2":
        print(f"Seu pedido:{os.linesep}{OPCAO_01_PRINCIAL_SECUDARIA_02}")
    elif opcoes_principal == "2" and opcao_secudaria == "1":
        print(f"Seu pedido:{os.linesep}{OPCAO_02_PRINCIPAL_SECUDARIA_01}")
    elif opcoes_principal == "2" and opcao_secudaria == "2":
        print(f"Seu pedido:{os.linesep}{OPCAO_02_PRINCIPAL_SECUDARIA_02}")
    elif opcoes_principal == "3" and opcao_secudaria == "1":
        print(f"Seu pedido:{os.linesep}{OPCAO_03_PRINCIPAL_SECUDARIA_01}")
    elif opcoes_principal == "3" and opcao_secudaria == "2":
        print(f"Seu pedido:{os.linesep}{OPCAO_03_PRINCIPAL_SECUDARIA_02}")
    else:
        print("Escolha um opção válida!")


def processar_cardapio_principal(opcoes_principal):
    OPCAO_01_PRINCIPAL = f"[1]-Big:{os.linesep}filé, abacaxi, presunto, queijo cheddar, bacon, alface e tomate + Batata pequena + Refri 300ml.{os.linesep}[2]-BigFrango:{os.linesep}frango desfiado, presunto, queijo mussarela, bacon, milho verde, ervilha, alface e tomate) + Batata pequena + Refri 300ml."
    OPCAO_02_PRINCIPAL = f"[1]-Filet mignon com cheddar.{os.linesep}[2]-Camarão catupiry.{os.linesep}"
    OPCAO_03_PRINCIPAL = f"[1]-Pizza estilo Nova York:{os.linesep}massa fininha e fatia grandona, queijo e requeijão cremoso.{os.linesep}[2]-Frango com Requeijão:{os.linesep}Frango, queijo Hut e requeijão cremoso"
    if opcoes_principal == "1":
        print(OPCAO_01_PRINCIPAL)
    elif opcoes_principal == "2":
        print(OPCAO_02_PRINCIPAL)
    elif opcoes_principal == "3":
        print(OPCAO_03_PRINCIPAL)
    else:
        print("Digite uma opcão válida!")


def cadastro_cliente(cadastro_usuario):
    numero_para_contato = input(f"Qual seu número com DD para contato?{os.linesep}")
    if cadastro_usuario == "1" and len(numero_para_contato) == 11:
        ...
    elif cadastro_usuario == "2" and len(numero_para_contato) == 11:
        # Pedir o endereco
        endereco_usuario = input(f"Qual seu endereço para entrega?{os.linesep}")
        print("Estamos cadastrando...")
        sleep(4)
        print(f"Você foi cadastrado com sucesso!{os.linesep}")
    else:
        digite_numero_valido = input(f"Digite um número válido{os.linesep}")
        while len(digite_numero_valido) > 11:
            digite_numero_valido = input(f"Digite um número válido{os.linesep}")
        endereco_usuario = input(f"Qual seu endereço?{os.linesep}")
        print("Estamos cadastrando...")
        sleep(4)
        print(f"Você foi cadastrado com sucesso!{os.linesep}")


# Programa principal
def start():
    # Apresentar o chatbot
    print("Olá! Bem-vindo! :)")
    # Pedir o nome
    nome_usuario = input(f"Qual seu nome?{os.linesep}")
    # Boas vindas
    print(f"É um prazer lhe atender {nome_usuario}, eu me chamo Cookie!")
    # Cadastro do cliente
    cadastro_usuario = input(
        f"Você já possui um cadastro?{os.linesep}[1]-Sim [2]-Não{os.linesep}"
    )
    cadastro_cliente(cadastro_usuario)
    # Oferecer o menu de opções
    opcoes_principal = input(
        f"O que você gostaria de pedir hoje? {os.linesep}[1]-Sanduiches{os.linesep}[2]-Calzones{os.linesep}[3]-Pizza{os.linesep}"
    )
    # Processar a resposta enviadas
    processar_cardapio_principal(opcoes_principal)

    opcao_secudaria = input(f"Escolha a sua opção:{os.linesep}")

    processar_cardapio_secudaria(opcoes_principal, opcao_secudaria)

    opcao_endereco = input(f"Poderia me informar como será a entrega?{os.linesep}[1]-Entregar para o endereço cadastrado.{os.linesep}[2]-Cadastrar um novo endereço.{os.linesep}[3]-Retirada.{os.linesep}")

    endereco_para_entrega( opcao_endereco)
    
# Quando iniciar o arquivo vamos rodar essa função
if __name__ == "__main__":
    start()
