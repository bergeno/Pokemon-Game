class Pokemon:
    def __init__(self, especie, level=1, nome=None):  
        self.especie = especie;
        self.level = level;
        
        if nome:
            self.nome = nome;
        else:
            self.nome = especie;
        
    def __str__(self):
        return "{}(Lvl {})" .format(self.especie, self.level);
    
    def atacar(self, pokemon):
        print("{} atacou {}!".format(self.nome, pokemon));
        
class PokemonEletrico(Pokemon):
    tipo = "Elétrico";
    def atacar(self, pokemon):
        print("{} lançou um raio de trovão em {}" .format(self, pokemon));

class PokemonFogo(Pokemon):
    tipo = "Fogo"
    def atacar(self, pokemon):
        print("{} lançou uma bola de fogo na cabeça de {}" .format(self, pokemon));
        
class PokemonAgua(Pokemon):
    tipo = "Água"
    def atacar(self, pokemon):
        print("{} lançou uma jato d'agua em {}" .format(self, pokemon));