class Nivel:
    def __init__(self, valor: int) -> None:
        self.__ataque: int = 5
        self.__defensa: int = 6
        self.__mana: int = 12
        self.__vida: int = 120
        
        self.__valor: int = valor
        
        self.__xp: int = 0
        self.__limiteXP: int = 50    
        
        if self.__valor != 1:
            self.__subirNivel()
            self.__obtenerValorLimiteXP()
            
    def getAtaque(self) -> int:
        return self.__ataque
    
    def getDefensa(self) -> int:
        return self.__defensa
    
    def getMana(self) -> int:
        return self.__mana
    
    def getVida(self) -> int:
        return self.__vida
    
    def getLimiteXP(self) -> int:
        return self.__limiteXP
    
    def getXP(self) -> int:
        return self.__xp
    
    def getNivel(self) -> int:
        return self.__valor
    
    def xpDerrota(self):
        return self.__valor * 100

    def __subirNivel(self):
        for i in range(1,self.__valor):
            self.__ataque += 1 
            self.__defensa += 1 
            self.__mana += 1 
            
        # Formula para hallar la vida:
        # 10 + ((NIVEL / 100) * ((2 * 72) + 22 + 72)) + NIVEL
        self.__vida = 10 + ((self.__valor/100)*((2*72)+22+72)) + self.__valor 

    def __obtenerValorLimiteXP(self):
        self.__limiteXP += self.__valor * (self.__limiteXP * 0.5)
                
    def __esXPIgualLimite(self):
            self.__xp = self.__xp - self.__limiteXP
            self.__valor += 1
            print("Ahora es nivel: ", self.__valor)
            self.__obtenerValorLimiteXP()
            
    def aumentoXP(self, xp: int, nombre: str):
        self.__xp += xp
        while self.__xp >= self.__limiteXP:
            print(f"{nombre} ha subido de nivel!!")
            self.__esXPIgualLimite()


nivel = Nivel(40)

print(nivel.getVida())