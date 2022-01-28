class Pokemon:
    def __init__(self, tipo, especie, level=1, nome=None):
        self.tipo = tipo;
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
    def atacar(self, pokemon):
        print("{} lançou um raio do trovão em {}" .format(self, pokemon));

class PokemonFogo(Pokemon):
    def atacar(self, pokemon):
        print("{} encinerou {}" .format(self, pokemon));


    
pokemon = Pokemon("Fogo", "Charmander");

pokemon2 = PokemonEletrico("Pikachu");

pokemon3 = PokemonFogo("HellBoy");

print(pokemon);

print(pokemon2);

print(pokemon3);


pokemon.atacar(pokemon2);
pokemon2.atacar(pokemon);