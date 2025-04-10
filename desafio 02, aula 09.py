# Digite um numero da tabuada
num = int(input('Digite um numero da tabuada:'))

# Abrir o arquivo em modo de escrita
with open('tabuada.txt', 'w') as f:
    # Escrever o cabeçalho para o arquivo
    f.write(f"Tabuada do {num}\n\n")

    # Calcular a tabuada e salvar no arquivo
    for m in range(1, 11):
        resultado = f'{num} x {m} = {num * m}\n'
        f.write(resultado)

print("A tabuada foi salva em 'tabuada.txt'.")