from Pokemon import *
from Pessoa import *

def escolherPokemonInicial(player):
    print("Shalom {}, agora você poderá escolher o pokemon que vai lhe acompanhar na sua jornada." .format(player));

    pikachu = PokemonEletrico("Pikachu", level=1);
    charmander = PokemonFogo("Charmander", level=1);
    squirtle = PokemonAgua("Squirtle", level=1);
    
    print("Você possui trẽs escolhas: ")
    print("1 - ", pikachu);
    print("2 - ", charmander);
    print("3 - ", squirtle);
    
    while True:
        escolha = input("Digite sua escolha: ")
        
        if (escolha == "1"):
            player.capturarPokemon(pikachu);
            break;
        elif (escolha == "2"):
            player.capturarPokemon(charmander);
            break;
        elif (escolha == "3"):
            player.capturarPokemon(squirtle);
            break;
        else:
            print("Escolha Inválida.")
    
player = Player("Bernardo");
#player.mostrarDinheiro();
#escolherPokemonInicial(player);

#inimigo = Inimigo("Gary", pokemons=[PokemonAgua("Squirtle", level=1)]);


#player.batalhar(inimigo);

player.explorar();

player.mostrarPokemons();