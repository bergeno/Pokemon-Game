import random;

class Pokemon:
    def __init__(self, especie, level=1, nome=None):  
        self.especie = especie;
        
        
        if level:
            self.level = level;
        else:
            self.level=random.randint(1, 100)
        
        if nome:
            self.nome = nome;
        else:
            self.nome = especie;
        
        self.ataque = level * 5;
        self.vida = level * 10;
        
    def __str__(self):
        return "{}(Lvl {})" .format(self.especie, self.level);
    
    def atacar(self, pokemon):
        pokemon.vida -= self.ataque; 
        print("{} perdeu {} de vida." .format(pokemon, self.ataque));
        
        if pokemon.vida <= 0:
            print("{} foi derrotado." .format(pokemon));
            return True;
        else:
            return False;
        
class PokemonEletrico(Pokemon):
    tipo = "Elétrico";
    def atacar(self, pokemon):
        print("{} lançou um raio de trovão em {}" .format(self, pokemon));
        return super().atacar(pokemon);

class PokemonFogo(Pokemon):
    tipo = "Fogo"
    def atacar(self, pokemon):
        print("{} lançou uma bola de fogo na cabeça de {}" .format(self, pokemon));
        return super().atacar(pokemon);
        
class PokemonAgua(Pokemon):
    tipo = "Água"
    def atacar(self, pokemon):
        print("{} lançou uma jato d'agua em {}" .format(self, pokemon));
        return super().atacar(pokemon);