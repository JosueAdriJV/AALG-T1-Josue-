import random

class EquipoDeVoley:
    def __init__(self, nombre):
        self.nombre = nombre
        self.setGanados = 0
        self.partidosPerdidos = 0
        self.partidosGanados = 0

    def RegistrarSet(self):
        self.setGanados += 1
        print(f"{self.nombre} ganó un set. Total sets ganados: {self.setGanados}")

    def resetearSet(self):
        self.setGanados = 0

def Puntos():
    return random.randint(10, 28)

def PuntosExtras():
    return random.randint(0, 6)

def JugarPartido(equipo1, equipo2):
    while equipo1.setGanados < 3 and equipo2.setGanados < 3:
        puntos1 = Puntos()
        puntos2 = Puntos()
        print(f"{equipo1.nombre}: {puntos1} puntos y  {equipo2.nombre}: {puntos2} puntos")

        if puntos1 >= 25 or puntos2 >= 25:
            if puntos1 > puntos2:
                equipo1.RegistrarSet()
            elif puntos2 > puntos1:
                equipo2.RegistrarSet()
            else:
                while puntos1 == puntos2:
                    puntos1 += PuntosExtras()
                    puntos2 += PuntosExtras()
                if puntos1 > puntos2:
                    equipo1.RegistrarSet()
                else:
                    equipo2.RegistrarSet()
        else:
            while puntos1 <= 25 and puntos2 <= 25:
                puntos1 += PuntosExtras()
                puntos2 += PuntosExtras()
                if puntos1 != puntos2 and (puntos1 >= 25 or puntos2 >= 25):
                    break
            if puntos1 > puntos2:
                equipo1.RegistrarSet()
            else:
                equipo2.RegistrarSet()

        if equipo1.setGanados == 3:
            equipo1.partidosGanados += 1
            equipo2.partidosPerdidos += 1
            print(f"\n{equipo1.nombre} Equipo Ganador\n")
            equipo1.resetearSet()
            equipo2.resetearSet()
            break

        elif equipo2.setGanados == 3:
            equipo2.partidosGanados += 1
            equipo1.partidosPerdidos += 1
            print(f"\n{equipo2.nombre} Equipo Ganador\n")
            equipo1.resetearSet()
            equipo2.resetearSet()
            break

def ResultadosDelTorneo(equipo1, equipo2):
    print("\nResultados del Torneo:")
    print(f"{equipo1.nombre} - Partidos Ganados: {equipo1.partidosGanados}, Partidos Perdidos: {equipo1.partidosPerdidos}")
    print(f"{equipo2.nombre} - Partidos Ganados: {equipo2.partidosGanados}, Partidos Perdidos: {equipo2.partidosPerdidos}")

def main():
    nombre1 = input("Nombre del primer equipo: ")
    nombre2 = input("Nombre del segundo equipo: ")
    equipo1 = EquipoDeVoley(nombre1)
    equipo2 = EquipoDeVoley(nombre2)

    cantidad = int(input("¿Cuántos partidos jugarán?: "))

    for i in range(cantidad):
        print(f"\nPartido {i+1}")
        JugarPartido(equipo1, equipo2)

    ResultadosDelTorneo(equipo1, equipo2)

if __name__ == "__main__":
    main()
