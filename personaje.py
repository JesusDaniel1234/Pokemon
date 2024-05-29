from pokemon import Pokemon

class Personaje:
    def __init__(self, nombre: str) -> None:
        self.nombre: str = nombre
        self.listaPokemones: list[Pokemon] = []
        
    def addPokemon(self, pokemon: Pokemon) -> None:
        self.listaPokemones.append(pokemon)

    def listarPokemones(self) -> None:
        if len(self.listaPokemones)!=0:
            for i in self.listaPokemones:
                print(i)
        else:
            print("No hay pokemones en la lista.")
            
    def statsPokemon(self) -> None:
        if len(self.listaPokemones) != 0:
            for i in self.listaPokemones:
                print(i.mostrarStats())
        else:
            print("No hay pokemones en la lista.")

        
p1 = Pokemon("Pikachu", 10)
p2 = Pokemon("Charmander", 6)

personaje = Personaje("Jesús")

# personaje.addPokemon(p2)
# personaje.addPokemon(p1)

personaje.statsPokemon()