# a) - contar vogais em uma string
def contar_vogais(string):
    string = string.lower()
    vogais = 'aeiou'
    result = {vogal: string.count(vogal) for vogal in vogais} 
    return result

verifica = input("\nDigite a string que deseja ver quantas vogais tem: ")
resultado = contar_vogais(verifica)
print("Número de vogais:", resultado)

# b) - iverte palavra 
string = input("\nDigita a String que deseja inverter: ")
string_invertida = string[::-1]
print("Palavra Invertida:",string_invertida)  

# c) - verifica se a string é palindromo (Lê da mesma e forma de trás pra frente)
def verifica_palindromo(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]

verifica = input("Digite a string que deseja verificar: ")

if verifica_palindromo(verifica):
    print("A string é um palíndromo.")
else:
    print("A string não é um palíndromo.")