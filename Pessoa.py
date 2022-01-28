from Pokemon import *;
import random;

NOMES = [
        "John", "André", "Ash", "Gary", "Marcelo", "Patrícia", "Gustavo", "Lara", "Wilken"
    ]

POKEMONS = [
    PokemonFogo("Charmander"),
    PokemonFogo("Flarion"),
    PokemonFogo("Charmilion"),
    PokemonEletrico("Pikachu"),
    PokemonEletrico("Raichu"),
    PokemonAgua("Squirtle"),
    PokemonAgua("Magicarp")
]

class Pessoa:
    
    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome;
        else:
            self.nome = random.choice(NOMES);
            
        self.pokemons = pokemons;
    
    def __str__(self) -> str:
        return self.nome;
    
    def mostrarPokemons(self):
        if (self.pokemons):
            print("Pokemons de {}" .format(self));
            for pokemon in self.pokemons:
                print(pokemon);
        else:
            print("{} não possuí nenhum pokemon!" .format(self))
        
            
class Player(Pessoa):
    tipo = "Player";
    
    def capturarPokemon(self, pokemon):
        self.pokemons.append(pokemon);
        print("{} captutrou {} com sucesso!" .format(self, pokemon));
    
class Inimigo(Pessoa):
    tipo = "Inimigo";
    
    def __init__(self, nome=None, pokemons=[]):
        
        if not pokemons:
            for i in range(6):
                pokemons.append(random.choice(POKEMONS));
                       
        super().__init__(nome, pokemons);
        
        
meuInimigo = Inimigo();

meuInimigo.mostrarPokemons();
    
    

'''
    Testes

pokemon = PokemonEletrico("Pikachu");

pokemon2 = PokemonFogo("Charmander");

eu = Player(nome="Bernardo", pokemons=[pokemon, pokemon2]);

eu.mostrarPokemons();

eu = Player();

print(eu);

pokemon_selvagem = PokemonFogo("Charmander")

eu.capturarPokemon(pokemon_selvagem);

eu.mostrarPokemons();

'''

