# Atividades do dia 24/10/2024 
# Ex. 01
n1=int(input("Digite o valor 01: "))
n2=int(input("Digite o valor 02: "))
total=n1+n2
print("A soma dos valores é:",total)

# Ex. 02
num = int(input("Digite o número que deseja saber se é Par ou Impar: "))
if num % 2 == 0:
    print(f"{num} é par.")
else:
    print(f"{num} é ímpar.")

# Ex. 03
num = int(input("Digite um número: "))
fatorial = 1
for n in range(1, num + 1):
    fatorial *= n
print(f"O fatorial de {num} é {fatorial}.")

# Ex. 04
n = int(input("Digite um número para ver a sequência de Fibonacci: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Ex. 05
num = int(input("Digite o número que deseja saber se é primo: "))
if num > 1:
    for n in range(2, num):
        if (num % n) == 0:
            print(f"{num} não é primo.")
            break
    else:
        print(f"{num} é primo.")
else:
    print(f"{num} não é primo.")

# Ex. 06
n1=int(input("Digite o primeiro número: "))
n2=int(input("Digite o segundo número: "))
n3=int(input("Digite o terceiro número: "))
media=(n1+n2+n3)/3
print(f"A média dos números é: {media:.2f}.")

# Ex. 07
num = int(input("Digite o número que deseja ver o quadrado dele: "))
quadrado = num ** 2
print(f"O quadrado de {num} é {quadrado}.")

# Ex.08
num=int(input('Tabuada do numero: '))
for n in range (11):
    print(f'{num} x {n} = {num*n}')

# Ex.09
n = int(input("Digite um número que deseja ver a soma de todos os antecessores: "))
soma = sum(range(1, n + 1))
print(f"A soma de 1 até {n} é {soma}.")

# Ex.10
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resultado = base ** expoente
print(f"{base} elevado a {expoente} é {resultado}.,")

# Ex.11
num1=int(input("Digite o primeiro número: "))
num2=int(input("Digite o segundo número: "))
num3=int(input("Digite o terceiro número: "))
maior = max(num1, num2, num3)
print(f"O maior número é {maior}.")

#Ex. 12
nota = float(input("Digite a nota (0 a 100): "))
if nota >= 90:
    print("Excelente")
elif 70 <= nota < 90:
    print("Bom")
elif 50 <= nota < 70:
    print("Regular")
else:
    print("Insuficiente")

# Ex. 13
idade = int(input("Digite a sua idade: "))
if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

# Ex. 14
numero = int(input("Digite um número (10 a 20): "))
if numero in range(10, 20):
    print ("{} está no intervalo!".format(numero))
else:   
    print ("{} não está no intervalo!".format(numero))

# Ex. 15 
num = int(input("Digite um número para verificar se é positivo, negativo ou zero: "))
if num == 0:
    print ("O número é",num)
    
elif num < 0:
    print ("O número",num,"é negativo")
    
else:   
    print ("O número",num,"é positivo")

#  Ex. 16
contador = 10
while contador >= 0:
    print(contador)
    contador -= 1

# Ex. 17
count = 0
for i in range(1, 101):
    if i % 2 == 0:
        count += 1
print("\nQuantidade de números pares entre 1 e 100:", count,"\n")

# Ex. 18
soma = 0
i = 1
while i < 50:
    if i % 2 != 0:
        soma += i
    i += 1
print("\nSoma dos números ímpares entre 1 e 50:", soma,"\n")

# Ex. 19
maior = None
for _ in range(10):
    numero = int(input("Digite um número inteiro: "))
    if maior is None or numero > maior:
        maior = numero
print("O maior número é:", maior)

# Ex. 20
quantidade = int(input("Digite a quantidade de números que deseja inserir: "))
soma = 0

for _ in range(quantidade):
    numero = int(input("Digite um número: "))
    soma += numero

media = soma / quantidade if quantidade > 0 else 0
print("A média dos números é:", media)

# Ex. 21
import random

numero_secreto = random.randint(1, 10)
chute = None

while chute != numero_secreto:
    chute = int(input("Adivinhe o número entre 1 e 10: "))
    if chute < numero_secreto:
        print("Tente um número maior.")
    elif chute > numero_secreto:
        print("Tente um número menor.")
print("Parabéns! Você adivinhou o número.")

# Ex. 22
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc <= 24.9:
    print("Peso ideal")
else:
    print("Acima do peso")

# Ex. 23
celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = celsius * (9 / 5) + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")

# Ex. 24
milhas = float(input("Digite a distância em milhas: "))
metros = milhas * 1609.34
centimetros = metros * 100
print(f"A distância em metros é: {metros:.2f} m")
print(f"A distância em centímetros é: {centimetros:.2f} cm")

# Atividade Extra
# while True:
vida_adversario = 100
print("Início da luta! O objetivo é reduzir a vida do adversário a 0.")

while vida_adversario > 0:
    print(f"\nVida do adversário: {vida_adversario}")
    print("Escolha seu ataque:")
    print("1: Golpe Fraco (10 de dano)")
    print("2: Golpe Médio (20 de dano)")
    print("3: Golpe Forte (30 de dano)")
    
    escolha = int(input("Digite o número do ataque escolhido: "))

    if escolha == 1:
        dano = 10
    elif escolha == 2:
        dano = 20
    elif escolha == 3:
        dano = 30
    else:
        print("Escolha inválida! Tente novamente.")
        continue  

    vida_adversario -= dano
    vida_adversario = max(vida_adversario, 0) 

    print(f"Você causou {dano} de dano! Vida do adversário: {vida_adversario}")

print("\nParabéns! Você venceu a luta!")