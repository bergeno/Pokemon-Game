from time import sleep
from Pokemon import *;
import random;
from termcolor import colored

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
    
    def __init__(self, nome=None, pokemons=[], dinheiro = 100):
        if nome:
            self.nome = nome;
        else:
            self.nome = random.choice(NOMES);
            
        self.pokemons = pokemons;
        
        self.dinheiro = dinheiro;
    
    def __str__(self) -> str:
        return self.nome;
    
    def mostrarPokemons(self):
        if (self.pokemons):
            print(colored("Pokemons de {}","yellow") .format(self));
            for index,pokemon in enumerate(self.pokemons):
                print("{} - {}".format(index, pokemon));
        else:
            print("{} não possuí nenhum pokemon!" .format(self));
            
    def escolherPokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print("{}: {}, eu escolho você!!!!" .format(self, pokemon_escolhido));
            return pokemon_escolhido;
        else:
                print("Esse jogador não possui nenhum pokemon para ser escolhido.");
                
    def ganharDinheiro(self, quantidade):
        self.dinheiro += quantidade;
        print("Você ganhou $ {}" .format(quantidade));
        self.mostrarDinheiro();
        
    def mostrarDinheiro(self):
        print("Você possui $ {}".format(self.dinheiro))
        
            
    def batalhar(self, pessoa):
        print("{} iniciou uma batalha com {}" .format(self, pessoa));
        
        pessoa.mostrarPokemons();
        pokemonInimigo = pessoa.escolherPokemon();
        
        pokemon = self.escolherPokemon();
        
        if pokemon and pokemonInimigo:
            while True:
                vitoria = pokemon.atacar(pokemonInimigo);
                if vitoria:
                    print("{} ganhou a batalha" .format(self));
                    self.ganharDinheiro(pokemonInimigo.level * 100);
                    break;
                sleep(0.5);
                vitoriaInimiga = pokemonInimigo.atacar(pokemon);
                
                if vitoriaInimiga:
                    print("{} ganhou a batalha" .format(pessoa))
                    break;
                sleep(0.5);
                  
        else:
            print("[ERRO] Essa batalha não pode acontecer.")
            
        
            
class Player(Pessoa):
    tipo = "Player";
    
    def capturarPokemon(self, pokemon):
        self.pokemons.append(pokemon);
        print("{} captutrou {} com sucesso!" .format(self, pokemon));
        
    def escolherPokemon(self):
        self.mostrarPokemons();
        
        while True:
            escolha = input("Escolha o seu pokemon: ");
            
            if (self.pokemons):
                try:
                    escolha = int(escolha);
                    pokemon_escolhido = self.pokemons[escolha];
                    print(colored("{}:", "blue").format(self), "{}, eu escolho você!!!!" .format(pokemon_escolhido));
                    return pokemon_escolhido;
                except:
                    print("Escolha Inválida.");
            else:
                print("Esse jogador não possui nenhum pokemon para ser escolhido.");
        
    def explorar(self):
        if random.random() <= 0.3:
            pokemon = random.choice(POKEMONS);
            print("Um pokemon selvagem apareceu: {}" .format(pokemon));
            
            escolha = input("Deseja tentar capturar esse pokemon? (s/n) ")
            
            if escolha == "s":
                if random.random() >= 0.5:
                    self.capturarPokemon(pokemon);
                else:
                    print("Esse pokemon fugiu.");
            else:
                print("Ok, boa viagem!");
        else:
            print("Essa exploração não deu em nada.");
            return None;
    
class Inimigo(Pessoa):
    tipo = "Inimigo";
    
    def __init__(self, nome=None, pokemons=[]):
        
        if not pokemons:
            for i in range(6):
                pokemons.append(random.choice(POKEMONS));
                       
        super().__init__(nome, pokemons);
        

    
    

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

