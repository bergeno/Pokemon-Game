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
            for index,pokemon in enumerate(self.pokemons):
                print("{} - {}".format(index, pokemon));
        else:
            print("{} não possuí nenhum pokemon!" .format(self));
            
    def escolherPokemon(self):
        self.mostrarPokemons();
        
        while True:
            escolha = input("Escolha o seu pokemon: ");
            
            if (self.pokemons):
                try:
                    escolha = int(escolha);
                    pokemon_escolhido = self.pokemons[escolha];
                    print("{}: {}, eu escolho você!!!!" .format(self, pokemon_escolhido));
                    return pokemon_escolhido;
                except:
                    print("Escolha Inválida.");
            else:
                print("Esse jogador não possui nenhum pokemon para ser escolhido.")
    
    def batalhar(self, pessoa):
        print("{} iniciou uma batalha com {}" .format(self, pessoa));
        
        pessoa.mostrarPokemons();
        pessoa.escolherPokemon();
        
        self.escolherPokemon();
        
            
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
    
    def escolherPokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print("{}: {}, eu escolho você!!!!" .format(self, pokemon_escolhido));
        else:
                print("Esse jogador não possui nenhum pokemon para ser escolhido.")
        
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

