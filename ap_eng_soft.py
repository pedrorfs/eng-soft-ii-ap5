def get_IMC(weight, height):
    imc = weight / (height * height)
    return imc


def getTimes(distance, pace):
    times = []
    aux = 0
    for i in range(int(distance)):
        aux += pace
        times.append(aux)
    return times


name = input("Olá, qual é o seu nome? ")
print(f"{name}, aqui está o menu com algumas opções:")
option = ""
while True:
    print("------------------")
    print(f"A - Calcular IMC")
    print(f"B - Treinamento de Corrida")
    print(f"C - Encerrar programa")
    option = input("Digite a opção desejada:")
    if option == "C":
        print("...programa encerrado, até mais!")
        break
    if option == "A":
        print('''Vamos calcular o seu IMC(Índice de Massa Corporal). Para isso precisaaremos de algumas informações.\nPor favor, insira as informações mostradas abaixo:''')
        height = float(input("Altura(m): "))
        weight = float(input("Peso(KG): "))
        imc = get_IMC(weight, height)
        print(f"O seu IMC é {imc}")
        if imc < 18.5:
            print("Você está abaixo da faixa de valores ideal")
        elif imc > 29.9:
            print("Você está acima da faixa de valores ideal")
        else:
            print("O seu IMC está na faixa de valores ideal")
    if option == "B":
        print('Informe nos as seguintes informações para que seja possível estimar o tempo que você deverá ter em cada trecho da corrida')
        km = float(input("Distância(Km): "))
        pace = float(input("Pace(Ritmo min/Km): "))
        times = getTimes(km, pace)
        for idx, x in enumerate(times):
            print(f'{idx + 1}: {x}')
