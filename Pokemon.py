import random;

class Pokemon:
    def __init__(self, especie, level=0, nome=None, ataque=None, vida=None):  
        self.especie = especie;
        
        
        if level != 0:
            self.level = level;
        else:
            self.level=random.randint(1, 100)
        if vida:
            self.vida = vida;
        else:
            self.vida = self.level * 10;
        if ataque:
            self.ataque == ataque;
        else:
            self.ataque = self.level * 5;
        if nome:
            self.nome = nome;
        else:
            self.nome = especie;
        
    def __str__(self):
        return "{}(Lvl {})" .format(self.especie, self.level);
    
    def atacar(self, pokemon):
        ataqueEfetivo = int(self.ataque * random.random() * 1.3)
        pokemon.vida -= ataqueEfetivo; 
        print("{} perdeu {} de vida." .format(pokemon, ataqueEfetivo));
        
        if pokemon.vida <= 0:
            print("{} foi derrotado." .format(pokemon));
            self.vida = self.level * 10;
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
    

