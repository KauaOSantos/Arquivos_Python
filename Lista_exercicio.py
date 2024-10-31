# Ex. 01
print("Kauã Miguel Oliveira dos Santos")

# Ex. 02
nome = input("Digite seu nome: ")
altura = float(input("Digite a sua altura: "))
estadoCivil = input("Digite o seu estado civil: ")
print ("O seu nome é:",nome,"sua altura é:",altura,"e o seu estado civil é:",estadoCivil)

# Ex. 03
num = int(input("Digite um número: "))
match num:
  case 1:
    print("O dia da semana correspondente é: Domingo")
  case 2:
    print("O dia da semana correspondente é: Segunda")
  case 3:
    print("O dia da semana correspondente é: Terça")
  case 4:
    print("O dia da semana correspondente é: Quarta")
  case 5:
    print("O dia da semana correspondente é: Quinta")
  case 6:
    print("O dia da semana correspondente é: Sexta")
  case 7:
    print("O dia da semana correspondente é: Sábado")

# Ex. 04
idade=int(input("Digite a sua idade para saber se pode votar: "))
if(idade>17):
    print('Você é maior, já pode votar!')
elif(idade<18):
     print('Você é menor, não pode votar ainda!')

# Ex. 05
for a in range (1,11):
  print(a)

# Ex. 06
num = 0
while (num < 11):
       print(num)
       num = num + 1