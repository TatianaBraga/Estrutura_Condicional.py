                             #Exercício Lista 2

# 1) Faça um programa que receba, via teclado, um número real. Se esse número for positivo, calcule a raíz quadrada do mesmo e imprima na tela.
# Se o número for negativo, imprima uma mensagem dizendo que não existe raíz quadrada real.
'''
s = float(input('Digite um valor real:  '))
if s>0:
    print(f'raiz de s = {s**0.5}')
else:
    print('Não existe raiz quadrada real para esse número!')
'''

# 2) Faça um programa que receba, via teclado, dois números reais e imprima na tela o maior deles, bem como a diferença entre eles.
# Se os números forem iguais, imprima a mensagem: números iguais.
'''
a = float(input('Digite o primeiro número real:'))
b = float(input('Digite o segundo número real:'))
if a>b:
    d = a-b
    print(f'O primeiro número é maior: {a}, sendo a diferença entre eles = {d} ')
elif b>a:
    d = b-a
    print(f'O segundo numero é maior: {b}, sendo a diferença entre eles = {d}')
else:
    print('Os dois números reais são iguais!')

'''

# 3) Faça um programa que receba, via teclado, um número inteiro positivo e exiba na tela uma mensagem informando se esse número é par ou se é múltiplo de 3
# ou se é par e múltiplo de 3 ou se não satifaz nenhuma das condições.
'''
n = int(input('Digite um número inteiro:'))
if n%2 == 0:
    if n%3 == 0:
        print('Este número é par e múltiplo de 3!')
elif n%3 == 0:
    print('Este número é múltiplo de 3!')
elif n%2 == 0:
    print('Este número é par!')
else:
    print('Este número não é par nem múltiplo de 3!')

'''

# 5) Faça um programa que receba, via teclado, o número que representa um mês e imprima na tela o mês por extenso (Ex: 3 −→ março) ou uma mensangem de erro
# caso não seja digitado um mês válido
'''
m = int(input('Digite o número do mês:'))
m2 = 1
m2*=2*m/2
if m2 == 1:
        print(f'{m2:.0f} −→ janeiro')
elif m2 == 2:
        print(f'{m2:.0f} −→ fervereiro')
elif m2 == 3:
        print(f'{m2:.0f} −→ março')
elif m2 == 4:
        print(f'{m2:.0f} −→ abril')
elif m2 == 5:
        print(f'{m2:.0f} −→ maio')
elif m2 == 6:
        print(f'{m2:.0f} −→ junho')
elif m2 == 7:
        print(f'{m2:.0f} −→ julho')
elif m2 == 8:
        print(f'{m2:.0f} −→ agosto')
elif m2 == 9:
        print(f'{m2:.0f} −→ setembro')
elif m2 == 10:
        print(f'{m2:.0f} −→ outubro')
elif m2 == 11:
        print(f'{m2:.0f} −→ novembro')
elif m2 == 12:
        print(f'{m2:.0f} −→ dezembro')
else:
        print(f'ERRO! −→ Mês não identificado!')
'''

# 6) Faça um programa que receba, via teclado, a altura, H (m), e o sexo, S (codificado da seguinte forma: M→ masculino e F → feminino),
# de uma pessoa e exiba o seu peso ideal, pi (Kg). Calcule o peso ideal usando as fórmulas: • Homens → pi = 72, 7H − 58; • Mulheres → pi = 62, 1H − 44, 7.
'''
a = float(input('Digite sua altura:'))
s = input('Digite seu sexo biologico:')
pi = float(input('Digite seu peso:'))
Masculino = 1
feminino = 2
if s == 'M':
    print(f'Masculino -→ pi = {(72.7*a - 58):.2f} kg')
elif s == 'F':
    print(f'Feminino -→ pi = {(62.1*a - 44.7):.2f} kg')

else:
    print('Comando invalido!')
'''

# 7) Faça um programa que receba, via teclado, a velocidade de um carro ao passar por um radar.
# Se a velocidade ultrapassar 60 km/h, mostre uma mensagem informando que ele foi multado e qual o valor da multa.
# A multa vai custar R$ 7, 00 por cada km acima da velocidade permitida. Caso não tenha ultrapassado 60 km/h,
# mostre uma mensagem dizendo que ele está dentro do limite de velocidade permitido.
'''
D = float(input('Digite o valor da distância percorrida (em quilômetros):'))
T = float(input('Digite o valor do tempo em que o percurso foi analisado (em horas):'))
v = D/T
if v>=60:
    print(f' Você foi multado. O valor a ser cobrado na multa será: {(v-60)*7} reais')

else:
    print('Obrigado(a) por ser um cidadão consciente! Você está dentro do limite de velocidade. ')

'''

# 8) Faça um programa que calcule os volumes de um paralelepípedo, de um cone e de uma esfera. O programa deve receber, via teclado,
# a especificação da figura geométrica que se deseja calcular o volume, posteriormente, as informações necessárias para o cálculo e
# imprimir na tela o resultado calculado.
'''
v = int(input('Para calcular o volume de um paralelepidedo digite 1, para calcular o volume de um cone digite 2 e para calcular o volume de uma esfera digite 3:'))
r = float(input('Digite o raio da figura:'))
c = float(input('Digite o comprimento da figura:'))
l = float(input('Digite a largura da figura:'))
h = float(input('Digite a altura da figura:'))
pi = 3.14

if v == 1:
    print(f'O volume do paralelepipedo é v = {c*l*h:.2f} cm**3')
elif v == 2:
    print(f'O volume do cone é v = {(pi*(r**2)*h)/3:.2f} cm**3')
elif v == 3:
    print(f'O volume da esfera é v = {(4*pi*(r**3))/3:.2f} cm**3')
else:
    print('Comando invalido!')
'''

# 9) A velocidade vertical (m/s) de um míssil é dada por
    # v(t) =
        # 10t**2 − 2.5t, se 0 ≤ t ≤ 10
        # −0, 25t**2 + 1000, se 10 < t ≤ 20
        # 2(t − 20)2 + 45t, se 20 < t ≤ 30.
# Faça um programa que receba, via teclado, o tempo t (s), 0 ≤ t ≤ 30, calcule e imprima na tela a velocidade vertical do míssil.
'''
t = float(input('Digite o tempo de lançamento do míssil (s): '))
if 0<= t and t<= 10:
    print(f'A velocidaade do míssil é V(t) = {10*t**2 - 2.5*t} m/s ')
elif 10 < t <= 20:
    print(f'A velocidade do míssil é V(t) = {-0.25*t**2 + 1000} m/s')
elif 20 < t <= 30:
    print(f'A velocidade do míssil é V(t) = {2*(t - 20)**2 + 45*t} m/s')
else:
    print('Comando inválido.')
'''

# 10) Faça um programa que receba, via teclado, 3 notas (entre 0, 0 e 10, 0), descarte o valor da menor nota, calcule a média aritmética das duas maiores e exiba
# o valor na tela.
'''
n1 = float(input('Digite uma nota de 0.0 a 10.0: '))
n2 = float(input('Digite uma nota de 0.0 a 10.0: '))
n3 = float(input('Digite uma nota de 0.0 a 10.0: '))
if n1 < n2 and n1 < n3:
    print(f'média das maiores notas: {(n2 + n3)/2}')
elif n2 < n1 and n2 < n3:
    print(f'Média das maiores notas: {(n1 + n3)/2}')
elif n3 < n1 and n3 <n2:
    print(f'Média das maiores nota: {(n1 + n2)/2}')
'''

# 11) Faça um programa que receba, via teclado, 3 valores reais e uma letra. Se a letra for ‘A’, o programa deve calcular a média aritmética dos valores, se for ‘P’,
# a média ponderada, com pesos 5, 3 e 2 para o primeiro, segundo e terceiro valores respectivamente, se for ‘H’, a média harmônica e se a letra for ’G’ a
# média geométrica. Exiba na tela a média calculada.
'''
v = input('Digite uma letra: ')
v1 = float(input('Digite um número real: '))
v2 = float(input('Digite um número real: '))
v3 = float(input('Digite um número real: '))
if v =='a':
    print(f'Média aritmética: {(v1 + v2 + v3)/3:.2f}')
elif v == 'p':
    print(f'Média ponderada: {(5*v1 + 3*v2 + 2*v3)/10:.2f}')
elif v == 'h':
    print(f'Média Harmônica: {3/(1/v1 + 1/v2 + 1/v3) :.2f}')
elif v == 'g':
    print(f'Média Geométrica: {(v1*v2*v3)**0.5:.2f } ')
else:
    print('Comando inválido!')
'''

# 12) Para doar sangue é necessário ter entre 16 e 69 anos, pesar no mínimo 50 kg e estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas).
# Faça um programa que receba, via teclado, essas informações e imprima na tela se a pessoa pode ou não doar sangue.
'''
i = int(input('Digite a sua idade: '))
p = float(input('Digite o seu peso: '))
h = float(input('Digite quantas horas de sono você dormiu nass últimas 24 horas: '))
if 16 <= i <= 69 and p >= 50 and h >= 6:
    print('Você está apto a realizar a doação de sangue.')
else:
    print('Você não está apto a fazer a doação de sangue')

'''
# 13) Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente de imposto sobre o produto:
# MG = 7%
# ES = 8%
# SP = 12%
# RJ = 15%
# Faça um programa que receba, via teclado, o valor do produto e o estado destino e calcule o preço final do produto acrescido do imposto do estado em que ele será
# vendido. Se o estado digitado não for válido, mostrar uma mensagem de erro.
'''
e = input('Digite a sigla do estado RJ para o estado do Rio de Janeiro, MG para Minas Gerais, SP para São Paulo e ES para o estado do Espirito Santo: ')
v = float(input('Digite o valor do produto: '))
if e == 'MG':
    print(f'O valor do produto no estado de Minas Gerais será: {v*(1 + 0.07):.2f}')
elif e == 'ES':
    print(f'O valor do produto no estado do Espirito Santo será: {v*( 1 + 0.08):.2f}')
elif e == 'SP':
    print(f'O valor no estado de São Pualo será: {v*(1 + 0.12):.2f}')
elif e == 'RJ':
    print(f'O valor do produto no estado do Rio de Janeiro será: {v* (1 + 0.15):.2f}')
else:
    print('O produto não é comecializado neste estado!')
'''

# 14) A nota final de um estudante é calculada a partir de 3 notas atribuídas, respectivamente, a um trabalho de laboratório (peso 2), a uma avaliação
# semestral (peso 3) e a um exame final (peso 5). Faça um programa que receba, via teclado, as notas dessas avaliações, calcule e exiba na tela a média do aluno
# e sua situação de acordo com o critério:
# • média ≥ 6: Aprovado;
# • 6 > média ≥ 3: Recuperação;
# • média < 3: Reprovado.
'''
n1 = float(input('Digite a nota que o aluno tirou no trabalho de laboratótio: '))
n2 = float(input('Digite a nota que o aluno tirou na avaliação semestral: '))
n3 = float(input('Digite a nota que o aluno tirou no exame final: '))
m = (2*n1 + 3*n2 + 5*n3)/10
if m >= 6:
    print('Aluno aprovado!')
elif 3 <= m < 6:
    print('Aluno em recuperação!')
elif m<3:
    print('Aluno reprovado!')

'''
# 15) Faça um programa que receba, via teclado, o peso (em kg) e a altura (em m) de uma pessoa, calcule seu IMC (índice de massa corporal)
# e exiba na tela uma mensagem de acordo com o critério:
# • IMC < 17 : Muito abaixo do peso;
# • 17 ≤ IMC < 18,5: Abaixo do peso;
# • 18,5 ≤ IMC < 25 : Peso normal;
# • 25 ≤ IMC < 30 : Acima do peso;
# • 30 ≤ IMC < 35 : Obesidade I;
# • 35 ≤ IMC < 40 : Obesidade II (severa);
# • IMC ≥ 40 : Obesidade III (mórbida).
'''
p = float(input('Digite seu peso: '))
h = float(input('Digite sua altura: '))
IMC = p/h**2
if IMC < 17:
    print('Você está muito abaixo do peso.')
elif 17 <= IMC < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= IMC < 25:
    print('Você está em seu peso normal')
elif 25 <= IMC < 30:
    print('Você está acima do peso!')
elif 30 <= IMC < 35:
    print('Você está em situação de obesidade I!')
elif 35 <= IMC < 40:
    print('Você está em situação de de obesidade II (severa)!')
elif IMC >= 40:
    print('Você está em situação de obesidaade III (morbida)!')
'''

# 16) Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# • até 10 litros, sem desconto;
# • de 10 até 20 litros, desconto de 3% por litro;
# • acima de 20 litros, desconto de 5% por litro.
# Gasolina:
# • até 10 litros, sem desconto;
# • de 10 até 20 litros, desconto de 4% por litro;
# • acima de 20 litros, desconto de 6% por litro.
# Faça um programa que receba, via teclado, o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima na tela o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 4,60 o preço do litro do álcool é R$ 3,40.
'''
q = float(input('Digite  quantidade de combustível vendido em litros: '))
t = input('Digite o tipo de combustível ( G-gasolina para gasolina e A-álcool para álcool): ')
A = 3.40
G = 4.60
if q <= 10 and t == 'A-álcool':
    print(f'O valor a ser pago será: {A:.2f}')
elif 10< q <= 20 and t == 'A-álcool':
    print(f'O valor a ser pago será: {A*0.97:.2f}')
elif 20 < q and t == 'A-álcool':
    print(f'O valor a ser pago será: {A*0.95:.2f}')

elif q <= 10 and t == 'G-gasolina':
    print(f'O valor a ser pago será: {G:.2f}')
elif 10< q <= 20 and t == 'G-gasolina':
    print(f'O valor a ser pago será: {G*0.96:.2f}')
elif 20 < q and t == 'G-gasolina':
    print(f'O valor a ser pago será: {G*0.94:.2f}')
else:
    print('Comando inválido!')
'''

# 17) Um comerciante está vendendo frutas com a seguinte tabela de preços:
# Morango:
# • Até 5 Kg: R$ 9,50 por Kg;
# • Acima de 5 Kg: R$ 8,75 por Kg.
# Maçã:
# • Até 5 Kg: R$ 8,00 por Kg;
# • Acima de 5 Kg: R$ 7,25 por Kg.
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 70,00, receberá ainda um desconto de 10% sobre este total.
# Faça um programa que receba, via teclado, a quantidade (em Kg) de morangos e de maçãs compradas, calcule e exiba na tela o valor a ser pago pelo cliente.
'''
n = input('Digite o nome da fruta que deseja comprar: ')

if n == 'morango':
    morango = float(input('Digite a quantidade de morango (Kg): '))
    if morango<= 5:
        print(f'O valor a ser pago pelos morangos será: {morango*9.50:.2f} reais!')
    if morango > 5:
        print(f'O valor a ser pago pelos morangos será: {morango * 8.75:.2f} reais!')
    if morango >= 8 or morango*8.75 >= 70:
        print(f'O valor da compra de morango com o desconto de 10% será: {(morango*8.75)*0.9} ')

elif n == 'maçã':
    maçã = float(input('Digite a quantidade de maça (Kg): '))
    if maçã <= 5:
        print(f'O valor a ser pago pelos maçãs será: {maçã*8.00:.2f} reais!')
    if maçã >5:
        print(f'O valor a ser pago pelos maçãs será: {maçã * 7.25:.2f} reais!')
    if maçã >= 8 or maçã * 8.75 >= 70:
        print(f'O valor da compra de maçã com o desconto de 10% será: {(maçã*7.25)*0.9:.2f} ')
else:
    print('Comando inválido!')
'''

# 18) Faça um programa que receba, via teclado, um número inteiro representado um ano e exiba na tela se esse ano é, ou não, um ano bissexto.
'''
n = int(input("Entre com um ano: "))
if n%400==0:
    print("O ano é bissexto!")
elif n%4==0 and n%100!=0:
    print("Ano é bissexto!")
else:
    print("O ano não é bissexto!")
'''
# 19) Faça um programa que receba, via teclado, 3 valores
# reais representando o comprimento de 3 segmentos de reta x, y e z; verifique e exiba na tela se, a partir desses segmentos de reta, é possível formar um
# triângulo. Se for possível, imprima também qual o tipo de triângulo que pode ser formado: equilátero, isósceles ou escaleno.

x = int(input('Digite um valor para a abscissa: '))
y = int(input('Digite um valor para a ordenada: '))
z = int(input('Digite um valor para a cota: '))
if x == y and x == z and y == z:
    print('É equilatero!')    
elif x == y or y ==z:
    print('É isósceles!')
else:
    print('É escaleno!')























    



