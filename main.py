from time import sleep
from Pokemon import *
from Pessoa import *
from termcolor import colored

def escolherPokemonInicial(player):
    print("-")
    print("Agora você poderá escolher o pokemon que vai lhe acompanhar na sua jornada.");

    pikachu = PokemonEletrico("Pikachu", level=1);
    charmander = PokemonFogo("Charmander", level=1);
    squirtle = PokemonAgua("Squirtle", level=1);
    
    print("Você possui três escolhas: ")
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





if __name__ == "__main__":
    print(colored("=================================", "yellow"));
    print(colored('Bem vindo ao mundo dos Pokemons!', 'red'));
    print(colored("=================================", "yellow"))
    
    sleep(1)
    nome = input("Qual é o seu nome? ");
    player = Player(nome);
    
    print("Olá {}, esse é um mundo habitado por pokemons, a partir de agora sua missão é se tornar um mestre dos pokemons!" .format(nome))
    sleep(3)
    print("Capture o máximo de pokemons que conseguir e lute com os seus inimigos.")
    sleep(1);
    player.mostrarDinheiro();
    
    sleep(2);
    
    if player.pokemons:
        print("Já vi que você já possui pokemons.");
        sleep(1.5)
        player.mostrarPokemons();
    else:
        print("Parece que você não possui nenhum pokemon, portanto precisa escolher um.");
        sleep(2)
        escolherPokemonInicial(player);
    
    sleep(2)
    
    print("Pronto! Agora que você já possui um pokemon, derrote o seu rival Garry.")
    
    inimigo = Inimigo("Gary", pokemons=[PokemonAgua("Squirtle", level=1)]);
    
    sleep(2)
    
    player.batalhar(inimigo);
    
    while True:
        print("----------------------------- ");
        print("1 - Explorar o mundo");
        print("2 - Lutar com um inimigo.")
        print("0 - Sair do jogo")
       
        escolha  = input("O que deseja fazer? ")
        if escolha == "0":
            print("Fechando o jogo...")
            sleep(2);
            break;
        elif escolha == "1":
            player.explorar();
        elif escolha == "2":
            inimigoAleatorio = Inimigo();
            player.batalhar(inimigoAleatorio);
        else: 
            print("Escolha inválida.");
    
    # player = Player("Bernardo");
    # player.mostrarDinheiro();
    # escolherPokemonInicial(player);



    # player.batalhar(inimigo);

    # player.explorar();

    # player.mostrarPokemons();