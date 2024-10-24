# Ex. 01
# print("Kauã Miguel Oliveira dos Santos")

# Ex. 02
# nome = input("Digite seu nome: ")
# altura = float(input("Digite a sua altura: "))
# estadoCivil = input("Digite o seu estado civil: ")
# print ("O seu nome é:",nome,"sua altura é:",altura,"e o seu estado civil é:",estadoCivil)

# Ex. 03
# num = int(input("Digite um número: "))
# match num:
#   case 1:
#     print("O dia da semana correspondente é: Domingo")
#   case 2:
#     print("O dia da semana correspondente é: Segunda")
#   case 3:
#     print("O dia da semana correspondente é: Terça")
#   case 4:
#     print("O dia da semana correspondente é: Quarta")
#   case 5:
#     print("O dia da semana correspondente é: Quinta")
#   case 6:
#     print("O dia da semana correspondente é: Sexta")
#   case 7:
#     print("O dia da semana correspondente é: Sábado")

# Ex. 04
# idade=int(input("Digite a sua idade para saber se pode votar: "))
# if(idade>17):
#     print('Você é maior, já pode votar!')
# elif(idade<18):
#      print('Você é menor, não pode votar ainda!')

# Ex. 05
# for a in range (1,11):
#   print(a)

# Ex. 06
# num = 0
# while (num < 11):
#        print(num)
#        num = num + 1

# Atividades do dia 24/10/2024
# Ex. 01
# n1=int(input("Digite o valor 01: "))
# n2=int(input("Digite o valor 02: "))
# total=n1+n2
# print("A soma dos valores é:",total)

# Ex. 02
# num = int(input("Digite o número que deseja saber se é Par ou Impar: "))
# if num % 2 == 0:
#     print(f"{num} é par.")
# else:
#     print(f"{num} é ímpar.")

# Ex. 03
# num = int(input("Digite um número: "))
# fatorial = 1
# for n in range(1, num + 1):
#     fatorial *= n
# print(f"O fatorial de {num} é {fatorial}.")

# Ex. 04
# n = int(input("Digite um número para ver a sequência de Fibonacci: "))
# a, b = 0, 1
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# Ex. 05
# num = int(input("Digite o número que deseja saber se é primo: "))
# if num > 1:
#     for n in range(2, num):
#         if (num % n) == 0:
#             print(f"{num} não é primo.")
#             break
#     else:
#         print(f"{num} é primo.")
# else:
#     print(f"{num} não é primo.")

# Ex. 06
# n1=int(input("Digite o primeiro número: "))
# n2=int(input("Digite o segundo número: "))
# n3=int(input("Digite o terceiro número: "))
# media=(n1+n2+n3)/3
# print(f"A média dos números é: {media:.2f}.")

# Ex. 07
# num = int(input("Digite o número que deseja ver o quadrado dele: "))
# quadrado = num ** 2
# print(f"O quadrado de {num} é {quadrado}.")

# Ex.08
# num=int(input('Tabuada do numero: '))
# for n in range (11):
#     print(f'{num} x {n} = {num*n}')

# Ex.09
# n = int(input("Digite um número que deseja ver a soma de todos os antecessores: "))
# soma = sum(range(1, n + 1))
# print(f"A soma de 1 até {n} é {soma}.")

# Ex.10
# base = int(input("Digite a base: "))
# expoente = int(input("Digite o expoente: "))
# resultado = base ** expoente
# print(f"{base} elevado a {expoente} é {resultado}.,")

# Ex.11
# num1=int(input("Digite o primeiro número: "))
# num2=int(input("Digite o segundo número: "))
# num3=int(input("Digite o terceiro número: "))
# maior = max(num1, num2, num3)
# print(f"O maior número é {maior}.")

#Ex. 12
# nota = float(input("Digite a nota (0 a 100): "))
# if nota >= 90:
#     print("Excelente")
# elif 70 <= nota < 90:
#     print("Bom")
# elif 50 <= nota < 70:
#     print("Regular")
# else:
#     print("Insuficiente")

# Ex. 13
# idade = int(input("Digite a sua idade: "))
# if idade >= 18:
#     print("Você é maior de idade")
# else:
#     print("Você é menor de idade")

# Ex. 14
# numero = int(input("Digite um número (10 a 20): "))
# if numero in range(10, 20):
#     print ("{} está no intervalo!".format(numero))
# else:   
#     print ("{} não está no intervalo!".format(numero))

# Ex. 15 
num = int(input("Digite um número para verificar se é positivo, negativo ou zero: "))
if num == 0:
    print ("O número é",num)
    
else num > 0:   
    print ("O número",num,"é maior que 0")