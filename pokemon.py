from nivel import Nivel
import colorama
colorama.init()

class Pokemon:
    def __init__(self, nombre: str, nivel: int) -> None:
        self.__nombre: str = nombre
        self.__nivel: Nivel = Nivel(nivel)
        self.__vidaActual = self.__nivel.getVida()
    
    def getNombre(self) -> str:
        return self.__nombre
    
    def getVidaActual(self) -> int:
        return self.__vidaActual
    
    def setVidaActual(self, daño: float):
        print("Daño recibido: ", daño)
        self.__vidaActual = self.__vidaActual - daño
        
    def atacar(self):
        return self.__nivel.getAtaque()
    
    def aumentoXP(self, xp: int):
        self.__nivel.aumentoXP(xp, self.__nombre)
        
    def xpDerrota(self):
        return self.__nivel.xpDerrota()
            
    def veinticincoPorciento(self):
        import random as r
        return r.randint(1,4)
    
    # Mostrar información
    def mostrarVidaActual(self):
        print(colorama.Fore.GREEN + f"{self.__nombre} vida actual: {int(self.__vidaActual)} de {self.__nivel.getVida()}")
    
    def derrota(self):
        print(colorama.Fore.LIGHTRED_EX + f"{self.__nombre} ha sido derrotado!")
        
    def sinVida(self):
        return self.getVidaActual() <= 0
    
    def __str__(self) -> str:
        return f"{self.__nombre}"
    
    def mostrarStats(self):
        return f" {self.__nombre} - Stats: Ataque: {self.__nivel.getAtaque()}, Defensa: {self.__nivel.getDefensa()}, Mana: {self.__nivel.getMana()}, Vida: {self.__nivel.getVida()}"
    
class PokemonElectrico(Pokemon):
    def __init__(self, nombre: str, nivel: int) -> None:
        super().__init__(nombre, nivel)
        self.danoElectrico = 0.4
    
    def atacar(self):
        if self.veinticincoPorciento() == 1:
            print(colorama.Fore.RED + "Crítico!!!!!!")
            return super().atacar() + (super().atacar() * self.danoElectrico)
        return super().atacar()
    
    def mostrarStats(self):
        return super().mostrarStats() + f", Daño Electrico: {self.danoElectrico}"
        

pikachu = PokemonElectrico("Pikachu", 5)
raichu = PokemonElectrico("Raichu", 10)

# Batalla
while True:
    if pikachu.sinVida() or raichu.sinVida():
        if pikachu.sinVida(): 
            pikachu.derrota()
            raichu.aumentoXP(pikachu.xpDerrota()) 
        else: 
            raichu.derrota()
            pikachu.aumentoXP(raichu.xpDerrota()) 
        break
    
    pikachu.mostrarVidaActual()
    pikachu.setVidaActual(raichu.atacar())
    raichu.mostrarVidaActual()
    raichu.setVidaActual(pikachu.atacar())
    
    