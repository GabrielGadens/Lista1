#1. Adicione mais 2 atributos e 2 métodos à classe Mago.
#2. Instancie 3 objetos da classe mago e invoque seus métodos.
#3. Crie uma classe Data, com os seguintes atributos: dia, mês e ano. Além do construtor padrão, a
#classe deverá ter um construtor personalizado que recebe dia, mês e ano por parâmetro. Essa classe
#deve ter também dois métodos: imprimirData, que não recebe parâmetro, e
#imprimirDataPorExtenso, que recebe o nome de uma cidade por parâmetro. Ambos os métodos
#não retornam dados.
class Mago:
    def __init__(self, nome, idade, escola, poder, altura):
        # Atributos de instância
        self.nome = nome 
        self.idade = idade   
        self.escola = escola
        self.poder = poder
        self.altura = altura
        
    def andar(self):
        print('Estou andando')
    
    def falar(self):
        print('Ola Terraqueo! Meu nome é ',self.nome)
        
    def invocarMagia(self):
        print('Invocando magia!')
    
    def informaAltura(self):
        print('Eu tenho ',(self.altura/100),' metros' )
    
    def apresentaPoder(self):
        print('Cuide-se, eu posso ',self.poder)
        
class Data:
    def __init__(self,dia,mes,ano):
        self.dia=dia
        self.mes=mes
        self.ano=ano
    
    def imprimirData(self):
        print('hoje é dia ',self.dia,' de ',self.mes,' de ',self.ano)
    def imprimiDataPorExtenso(self,nomeCidade):
        print(nomeCidade,', dia ',self.dia,' de ',self.mes,' de ',self.ano)

        
AK = Mago('Alok',45,'Unisinos','Remixar',182)
PS = Mago('Pedro Sampaio', 28, 'Kondzilla','Cantar',175)
LS = Mago('Léo Stronda', 25, 'Escola de Monstros','Esmagar',168)
BB = Mago('Bambam', 56, 'Mutantes','Quebrar',185)

AK.falar()
AK.apresentaPoder()
AK.informaAltura()
print('\n')
BB.falar()
BB.apresentaPoder
BB.informaAltura
BB.apresentaPoder()

A = Data(15,'março',2010)
B = Data(19,'abril',2015)
print()
A.imprimirData()
A.imprimiDataPorExtenso('São Leopoldo')
print()
B.imprimirData()
B.imprimiDataPorExtenso('Esteio')