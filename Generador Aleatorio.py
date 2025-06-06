# Generador de numeros aleatorios
# Flores Cruz Juan Sebastian
# Grupo: 4S11
# Materia: Simulacion

import random

# Intervalos acumulados para un dado
intervalos = [
    (0.0, 0.16666667, 1),
    (0.16666667, 0.33333333, 2),
    (0.33333333, 0.5, 3),
    (0.5, 0.66666667, 4),
    (0.66666667, 0.83333333, 5),
    (0.83333333, 1.0, 6),
]

def mostrar_intervalos():
    print("\nIntervalos de Lanzamiento de un Dado:")
    print("Lado\tP(x)\t\tF(x)\t\tIntervalo")
    prob = 1/6
    acumulado = 0
    for i in range(1, 7):
        inf = round(acumulado, 8)
        acumulado += prob
        sup = round(acumulado, 8)
        print(f"{i}\t{round(prob, 8)}\t{round(acumulado, 8)}\t[{inf}, {sup})")

def lanzar_dado():
    print("\nResultado de Lanzamientos:")
    print("Ui\t\tVA X=")
    for _ in range(5):
        ui = random.random()
        for inf, sup, valor in intervalos:
            if inf <= ui < sup:
                print(f"{round(ui, 8)}\t{valor}")
                break

# Bucle controlado por el usuario
contador = 1
while True:
    print(f"\n--- Lanzamiento #{contador} ---")
    mostrar_intervalos()
    lanzar_dado()
    entrada = input("\nPresiona [Enter] para lanzar de nuevo o escribe 'salir' para terminar: ")
    if entrada.lower() == "salir":
        print("Saliendo")
        break
    contador += 1
