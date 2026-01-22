import random

recompensas_rangos = [
    (2, 5, "Nada"),
    (6, 7, "1d6 de oro"),
    (8, 9, "1d8 de oro"),
    (10, 13, "2d6 de oro"),
]

recompensas_rangos_extras = [
    (14, 15, "Arma usada"),
    (16, 16, "Objeto curioso"),
    (17, 17, "Poción menor"),
    (18, 18, "Ración"),
    (19, 19, "tesoro menor"),
    (20, 20, "¡Crítico!"),
]

Critico_rangos = [
    (1, 1, "Sombrero de copa elegante"),
    (2, 2, "Anillo de magia +1 al ataque de conjuro"),
    (3, 3, "Amuleto de chispas +1"),
    (4, 4, "3d8 de gemas "),
    ]

Objetos_curiosos = [
    (1, "Collar de cobre simple – 5 oros"),
    (2, "Sortija de hierro oxidada – 3 oros"),
    (3, "Bolsa de gemas diminutas (cristales de cuarzo) – 10 oros"),
    (4, "Amuleto de hueso tallado – 8 oros"),
    (5, "Trozo de tela élfica resistente – 12 oros"),
    (6, "Garra de bestia montada en plata – 15 oros"),
    (7, "Bolsa de especias raras (azafrán seco, hierbas exóticas) – 20 oros"),
    (8, "Pergamino viejo con runas ilegibles – 8 oros"),
    (9, "Estatuilla de barro sagrado (rota) – 6 oros"),
    (10, "Moneda antigua (fuera de circulación, coleccionable) – 15 oros"),
    (11, "Copa de bronce golpeada – 10 oros"),
    (12, "Pequeño cofre con bisagras oxidadas – 12 oros"),
    (13, "Piedra mágica apagada (sin poder) – 20 oros"),
    (14, "Perla pequeña – 25 oros"),
    (15, "Lingote de plata – 40 oros"),
    (16, "Collar con un rubí diminuto – 50 oros"),
    (17, "Máscara ceremonial de madera pintada – 15 oros"),
    (18, "Botella de vino añejo (muy raro en la dungeon) – 30 oros"),
    (19, "Corona rota de hierro con incrustaciones falsas – 20 oros"),
    (20, "Reliquia enigmática (nadie sabe qué es) – 1d20 × 5 oros"),
]

armas_rangos = [
    (1, "Daga – 3 oros"),
    (2, "Cimitarra – 8 oros"),
    (3, "Espada corta – 8 oros"),
    (4, "Espada larga – 15 oros"),
    (5, "Espadón (gran espada) – 25 oros"),
    (6, "Hacha de mano – 5 oros"),
    (7, "Hacha de batalla – 13 oros"),
    (8, "Gran hacha – 23 oros"),
    (9, "Maza – 8 oros"),
    (10, "Martillo de guerra – 15 oros"),
    (11, "Martillo ligero – 5 oros"),
    (12, "Lanza – 3 oros"),
    (13, "Jabalinas (x3) – 5 oros"),
    (14, "Tridente – 10 oros"),
    (15, "Estoque – 15 oros"),
    (16, "Carcaj (si ya pagaron carcaj entonces es un arco corto) – 13 oros"),
    (17, "Arco corto (con 10 flechas) – 13 oros"),
    (18, "Arco largo (con 10 flechas) – 25 oros"),
    (19, "Ballesta ligera – 15 oros"),
    (20, "Espadón +1 – 30 oros"),
]

tesosro_menor_rangos = [
    (1, "Pergamino de nivel 2 aleatorio a tu elección dm"),
    (2, "Mapa de esta dungeon (Solo funciona con este dia)"),
    (3, "Bolsa con 1d8 gemas (cada una 5 oros)"),
    (4, "Repite tirada"),
]

poción_menor_rangos = [
    (1, "Poción de curación menor"),
    (2, "Poción de velocidad podrida"),
    ]


def obtener_recompensa(dado_extra1):
    for inicio, fin, recompensa in recompensas_rangos:
        if inicio <= dado_extra1 <= fin:
            return recompensa
        
def obtener_recompensa_extra(dado):
    for inicio, fin, recompensa in recompensas_rangos_extras:
        if inicio <= dado <= fin:
            return recompensa

dadoNumero = input("numero de dados (presiona Enter para continuar): ")

for i in range(int(dadoNumero)):
    dado = random.randint(1, 20)
    if dado == 1 :
        print("Resultado: 1 - PIFIA")
    if dado <= 13:
        recompensa = obtener_recompensa(dado)
        print(f"Resultado: {dado} - Recompensa: {recompensa}")
    elif dado >= 14:
        dado_extra = dado
        recompensa_extra = obtener_recompensa_extra(dado_extra)
        print(f"Recompensa Extra de {dado_extra} : {recompensa_extra}")

        if 14 <= dado_extra <= 15:
            arma_dado = random.randint(1, 20)
            for numero, arma in armas_rangos:
                if numero == arma_dado:
                    print(f"Arma obtenida: {arma}")
        
        if dado_extra == 16:
            objeto_dado = random.randint(1, 20)
            for numero, objeto in Objetos_curiosos:
                if numero == objeto_dado:
                    print(f"Objeto curioso obtenido: {objeto}")
        
        if dado_extra == 17:
            pocion_dado = random.randint(1, 2)
            for numero, pocion in poción_menor_rangos:
                if numero == pocion_dado:
                    print(f"Poción menor obtenida: {pocion}")
        
        if dado_extra == 18:
            racion_cant =  1
            print(f"{racion_cant} Ración")  
        
        if dado_extra == 19:
            tesoro_dado = random.randint(1, 4)
            for numero, tesoro in tesosro_menor_rangos:
                if numero == tesoro_dado:
                    print(f"Tesoro menor obtenido: {tesoro}")
        
        if dado_extra == 20:
            critico_dado = random.randint(1, 4)
            for numero, critico in Critico_rangos:
                if numero == critico_dado:
                    print(f"Recompensa Crítica obtenida: {critico}")
