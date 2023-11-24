def getIMC(weight, height):
    imc = weight / (height * height)
    return imc

def getTimes(distance, pace):
    times = []
    aux = 0
    for i in range(int(distance)):
        aux += pace
        times.append(aux)
    return times

def test_getIMC():
    assert getIMC(60, 2) == 15

def test_getTimes():
    assert getTimes(5, 4) == [4, 8, 12, 16, 20]