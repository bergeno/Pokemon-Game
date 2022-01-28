from Pokemon import *;

class Pessoa:
    
    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome;
        else:
            self.nome = "Anônimo";
            
        self.pokemons = pokemons;
    
    def __str__(self) -> str:
        return self.nome;
    
    def mostrarPokemons(self):
        for pokemon in self.pokemons:
            print(pokemon);
        
            
class Player(Pessoa):
    tipo = "Player";
    
class Inimigo(Pessoa):
    tipo = "Inimigo";
    

'''

pokemon = PokemonEletrico("Pikachu");

pokemon2 = PokemonFogo("Charmander");

eu = Player(nome="Bernardo", pokemons=[pokemon, pokemon2]);

eu.mostrarPokemons();

'''