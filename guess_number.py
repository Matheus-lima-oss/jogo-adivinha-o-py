import random

print("Seja muito bem vindo ao Guess Number do Matheus!")

numero_entrada = input("Digite o número teto do desafio: ")

if numero_entrada.isdigit():
    numero_entrada = int(numero_entrada)
else:
    print("Erro: valor informado não é numérico. Favor execute novamente e informe um número!")
    quit()

random_number = random.randint(0, numero_entrada)

n_numeros = 0

while True:
    resposta_usuario = input("Adivinhe o número: ")

    if resposta_usuario.isdigit():
        resposta_usuario = int(resposta_usuario)
    else:
        print("Erro: valor informado não é numérico. Favor informe um número!")
        continue

    n_numeros = n_numeros + 1
    if resposta_usuario == random_number:
        print("Acertou!")
        break
    elif resposta_usuario > random_number:
        print("Chutou alto, o número randomico é menor que isso.")
    else:
        print("Chutou baixo, o número randomico é maior que isso.")

print("N de tentativas: " + str(n_numeros))
