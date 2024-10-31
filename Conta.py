class Conta():
    def __init__(self):
        self.nome = input("\nDigite o seu nome: ")
        self.__saldo = 0
        self.__cpf = input("\nDigite o seu CPF: ")
        self.__senha = int(input("\nDigite a sua senha: "))

    def extrato(self):
        senha = int(input("\nPara ver o seu extrato, digite a senha: "))
        if (senha == self.__senha):
            print("R$",self.__saldo)
            
        else:
            print("Senha Inválida.")
            

    def deposito(self):
        valor = float(input("\nDigite o valor que deseja depositar em sua conta: "))
        self.__saldo+=valor
        print(f"O valor depositado foi: R${valor}")
        

    def saque(self):
            senha = int(input("\nPara realizar o saque, digite a senha: "))
            if senha == self.__senha:
                valor = float(input("\nDigite o valor que deseja sacar: "))
                if valor <= self.__saldo:
                    self.__saldo -= valor
                    print(f"Você sacou: R${valor}")
                    print(f"Seu novo saldo é: R${self.__saldo}")
                else:
                    print("Saldo insuficiente.")
            else:
                print("Senha inválida.")