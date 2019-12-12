#http://www.ceplac.gov.br/radar/cafe.htm 
#https://www.cafepoint.com.br/noticias/giro-de-noticias/saiba-mais-epoca-de-plantio-e-renovacao-de-cafezais-54780n.aspx
#global final_contr  global final_pro    global cont_p   global cont_c
cont_p = 0
cont_c = 0
final_pro = 'PONTOS POSITIVOS:\n'
final_contr = 'PONTOS NEGATIVOS:\n'
def tam_terreno():
    while True:
        terreno = input('Digite o tamanho aproximado do terreno para plantação de café:\n')
        if terreno.isnumeric() == True: 
            print('\n')
            break
        else:
            print('\nRepresente o valor com números.')
def altitude(): #OK
    global final_contr
    global final_pro
    global cont_p
    global cont_c
    #Altitude entre 450 a 800 m
    while True:
        altitude = input('Qual a altitude, em metros, do terreno de plantação?\n')
        if altitude.isnumeric() == True:
            altitude = float(altitude)
            if altitude < 450:
                print('Altitude baixa comparada ao ideal.\n')
                final_contr = final_contr + 'O terreno aprensenta uma altitude muito baixa, é recomendado um terreno com elevação entre 450 metros à 800 metros. '
                cont_c = cont_c + 1
            elif altitude >= 450 and altitude <= 800:
                print('Altitude ideal para plantação de café.\n')
                final_pro = final_pro + 'O terreno apresenta uma altitude ideal. '
                cont_p = cont_p + 1
            elif altitude > 100:
                print('Altitude alta comparada ao ideal.\n')
                final_contr = final_contr + 'O terreno aprensenta uma altitude muito alta, é recomendado um terreno com elevação entre 450 metros à 800 metros. '
                cont_c = cont_c + 1
            break
        else:
            print('\nRepresente o valor somente com números.')
def temperatura(): #OK
    global final_contr
    global final_pro
    global cont_p
    global cont_c
    #Temperatura de 18º a 22º C
    while True:
        temperatura = input('Digite a temperatura média,em graus celsius, da região:\n')
        if temperatura.isnumeric() == True:
            temperatura = float(temperatura)
            if temperatura < 18:
                print('Temperatura muito baixa para plantio de café.\n')
                final_contr = final_contr + 'A temperatura média do local é muito baixa e pode afetar a plantação. '
                cont_c = cont_c + 1
            elif temperatura > 22:
                print('Temperatura muito alta para plantio de café.\n')
                final_contr = final_contr + 'A temperatura média do local é muito alta e pode afetar a plantação. '
                cont_c = cont_c + 1
            else: 
                print('Temperatura ideal para o plantio de café.\n')
                final_pro = final_pro + 'A temperatura do local é a ideal para a plantação. '
                cont_p = cont_p + 1
            break
        else:
            print('\nRepresente o valor somente com números.')
def precipitação(): #OK
    global final_contr
    global final_pro
    global cont_p
    global cont_c
    #Precipitação anual de 600 a 1500 mm são suficientes
    while True:
        precip = input('Digite a precipitação anual, em milimetros:\n')
        if precip.isnumeric() == True:
            precip = float(precip)
            if precip < 600:
                print('Preciptação anual muito baixa para o plantio.\n')
                final_contr = final_contr + 'A preciptação anual é muito baixa, pouca chuva pode atrapalhar. '
                cont_c = cont_c + 1
            elif precip >= 600 and precip <= 1500:
                print('Preciptação anual ideal para o plantio.\n')
                final_pro = final_pro + 'Preciptação anual é ideal para a plantação. '
                cont_p = cont_p + 1
            elif precip > 1500:
                print('Preciptação anual muito alta para o plantio.\n')
                final_contr = final_contr + 'A preciptação anual é muito alta para a plantação, muita chuva pode atrapalhar. '
                cont_c = cont_c + 1
            break
        else:
            print('\nRepresente o valor somente com números.')   
def solo_profund(): #OK
    global final_contr
    global final_pro
    global cont_p
    global cont_c
    #deve ter profundidade mínima de 1 m
    while True:
        profund = input('Digite a profundidade do solo em metros:\n')
        if profund.isnumeric() == True:
            profund = float(profund)
            if profund < 1:
                print('A profundidade do solo deve ser de no mínimo 1 metro.\n')
                final_contr = final_contr + 'A profundidade do solo é menor que a ideal (mínimo de 1 metro). '
                cont_c = cont_c + 1
            else:
                print('Boa pronfundidade do solo.\n')
                final_pro = final_pro + 'O solo apresenta uma boa profundidade. '
                cont_p = cont_p + 1
            break
        else:
            print('\nRepresente o valor somente com números.')  
def solo_tipo(): #OK
    global final_contr
    global final_pro
    global cont_p
    global cont_c
    #Não ser pedregoso ou excessivamente arenoso, de preferência fértil e de boa drenagem.
    #Áreas de baixada são ináptas ao plantio mesmo com sistema de drenagem artificial.
    while True:
        tipo1 = input('O solo é pedregoso? S/N\n')
        if tipo1.upper() == 'S' or tipo1.upper() == 'N':
            if tipo1.upper() == 'S':
                print('Solo pedregoso pode atrapalhar.\n')
                cont_c = cont_c + 1
                final_contr = final_contr + 'O solo é pedregoso. '
                break
            else:
                print('O ideal é o solo não ser pedregoso.\n')
                cont_p = cont_p + 1
                final_pro = final_pro + 'O solo não é pedregoso. '
                break
        else: 
            print('\nPor favor responda com "S" ou "N"')
    while True:
        tipo2 = input('O solo é excessivamente arenoso? S/N\n')
        if tipo2.upper() == 'S' or tipo2.upper() == 'N':
            if tipo2.upper() == 'S':
                print('Solo excessivamente arenoso pode atrapalhar.\n')
                cont_c = cont_c + 1
                final_contr = final_contr + 'O solo é excessivamente arenoso. '
                break
            else:
                print('O ideal é o solo não ser excessivamente arenoso.\n')
                cont_p = cont_p + 1
                final_pro = final_pro + 'O solo não é excessivamente arenoso. '
                break
        else: 
            print('\nPor favor responda com "S" ou "N"')
    while True:
        tipo3 = input('O solo é fértil? S/N\n')
        if tipo3.upper() == 'S' or tipo3.upper() == 'N':
            if tipo3.upper() == 'S':
                print('O ideal é o solo ser fértil.\n')
                cont_p = cont_p + 1
                final_pro = final_pro + 'O solo é fértil. '
                break
            else:
                print('Solo infértil pode atralhar.\n')
                cont_c = cont_c + 1
                final_contr = final_contr + 'O solo não é fértil. '
                break
        else: 
            print('\nPor favor responda com "S" ou "N"')
    while True:
        tipo4 = input('O solo é de boa drenagem? S/N\n')
        if tipo4.upper() == 'S' or tipo4.upper() == 'N':
            if tipo4.upper() == 'S':
                print('O solo ter uma boa drenagem é o ideal.\n')
                cont_p = cont_p + 1
                final_pro = final_pro + 'O solo tem uma boa drenagem. '
                break
            else:
                print('O solo não ter uma boa drenagem pode atrapalhar.\n')
                cont_c = cont_c + 1
                final_contr = final_contr + 'O solo não tem uma boa drenagem. '
                break
        else: 
            print('\nPor favor responda com "S" ou "N"')
def epoca_plantar(): #OK
    global final_contr
    global final_pro
    global cont_p
    global cont_c
    while True:
        epoca = input('''Em qual época do ano será a plantação?
    1 - Janeiro\n    2 - Fevereiro\n    3 - Março\n    4 - Abril
    5 - Maio\n    6 - Junho\n    7 - Julho\n    8 - Agosto
    9 - Setembro\n    10 - Outubro\n    11 - Novembro\n    12 - Dezembro\n''')
        if epoca.isnumeric() == True:
            epoca = float(epoca)
            if epoca == 11 or epoca == 12:
                print('Essa é a melhor época do ano para se plantar o café arábica.\n')
                final_pro = final_pro + 'Ótima época do ano para se plantar o café arábica. '
                cont_p = cont_p + 1
            else:
                print('''Essa não é a melhor epoca do ano para se plantar o café arábica.
                A melhor época é entre novembro e dezembro.\n''')
                final_contr = final_contr + 'Não é recomendado o plantio de café nessa época do ano, será melhor entre Novembro e Dezembro. '
                cont_c = cont_c + 1
            break
        else:
            print('\nRepresente o valor somente com números.')
def finale(): #OK
    while True:
        answer = input('Exibir conclusões finais? S/N\n')
        if answer.upper() == 'S':
            conc_final = True
            break
        elif answer.upper() == 'N':
            conc_final_final = False
            break
        else:
            answer = input('Resposta incorreta. Responda com "S" ou "N".')
    return conc_final
print('''Projeto para identificação de possíveis impecílios e vantagens para uma platanção de café.
Será necessário fornecer alguns dados:''')
tam_terreno()
altitude()
temperatura()
precipitação()
solo_profund()
solo_tipo()
epoca_plantar()
if cont_p > cont_c:
    resp =  'esse é um bom local para se plantar o café arábica.'
else:
    resp = 'esse NÃO é um bom local para se plantar o café arábica.'
if finale() == True:
    print(final_pro + '\n')
    print(final_contr)
    print('\nQuanto mais pontos positivos, melhor será sua plantação. O contrário só prejudicará a mesma.\n')
    print(f'Temos um total de {cont_p} pontos postivos e {cont_c} negativos. Matematicamente falando, {resp}')
    print('\nFim')
else:
    print('\nFim')
