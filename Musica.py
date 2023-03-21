#4. Adapte o exercício de revisão (mini-spotify), proponto uma classe Musica. Quais seriam seus
#atributos? Quais seriam alguns dos seus possíveis métodos? Como poderíamos representar uma
#playlist?
from datetime import datetime
class Musica:
    def __init__(self, nome, artistas, genero, ano, duracao):
        self.nome = nome 
        self.artistas = artistas   
        self.genero = genero
        self.ano = ano
        self.duracao = duracao
        
    def duracaoMinutos(self):
        return (self.duracao)/60
    
    def idadeDaMusica(self):
        anoAtual=datetime.now().year
        print('A música tem ',int(anoAtual)-(self.ano),' anos')
    
    def __str__(self):
        return 'Música: {} Artista(s): {}  Genêro: {} Lançada em: {} Duração: {:.2f} min'.format(self.nome,self.artistas,self.genero,self.ano,self.duracaoMinutos())

M1 = Musica('Fa fe fi fo Funk','Anira','Funk',2019,188)
M2 = Musica('Sofrência de programar','Ada & Turing','Sertanejo',1998,180)
M3 = Musica('Rock’n Rolo', 'The Buns','Rock',	1984, 241)
M4 = Musica('Grifinoria Girls', 'Katy Potter', 'Pop',	2017, 145 ) 
M5 = Musica('Outra musica', 'Anira', 'Funk', 2019, 185 ) 

print(M1)
M1.idadeDaMusica()
print(M2)
M2.idadeDaMusica()
print(M3)
M3.idadeDaMusica()
print(M4)
M4.idadeDaMusica()
print(M5)
M5.idadeDaMusica()