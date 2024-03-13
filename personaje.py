
# Define la clase personaje
class Personaje:

    # Constructor de la clase con parámetro
    def __init__(self, nombre):
        
        # Atributos de la clase
        self.nombre = nombre
        self.nivel = 1  # Nivel inicial del personaje (no hay máximo)
        self.experiencia = 0  # Experiencia inicial del personaje (entre 0 y 99)

    # Método getter que retorna los atributos en forma de un string
    @property
    def estado(self):
        return (f"NOMBRE:  {self.nombre}\t\tNIVEL:  {self.nivel}\t\t EXP:  {self.experiencia}")

    # Método mutador del estado del personaje
    @estado.setter
    def estado(self, exp: int):

        # suma la experiencia recibida con la que ya tenía
        temp_exp = self.experiencia + exp

        # Actualizar el nivel basado en la experiencia acumulada
        while temp_exp >= 100:
            self.nivel += 1
            temp_exp -= 100

        # Ajustar la experiencia si es negativa y el nivel no es 1
        while temp_exp < 0:
            
            # Si tiene un nivel mayor a uno se ajusta nivel y experiencia
            if self.nivel > 1:
                temp_exp = 100 + temp_exp
                self.nivel -= 1
            # Si el nivel es menor a 1 solo se lleva la experiencia a cero
            else:
                temp_exp = 0
        
        # Se actualiza el nivel de experiencia
        self.experiencia = temp_exp

    # Método que compara el nivel de una instancia y otra, retornando True or False
    def __lt__(self, other):
        return self.nivel < other.nivel

    # Método que compara el nivel de una instancia y otra, retornando True or False
    def __gt__(self, other):
        return self.nivel > other.nivel

    # Método para compara el nivel de una instancia y otra, buscando igualdad, retornando booleano
    def __eq__(self, other):
        return self.nivel == other.nivel

    # Método que calcula la probabilidad de ganar contra otro personaje. Retorna la probabilidad
    def get_probabilidad_ganar(self, other):

        # Si el nivel es menor
        if self < other:
            return 0.33     # 33% de probabilidades de ganar
        
        # Si el nivel es mayor
        elif self > other:  # 66% de probabilidades de ganar
            return 0.66
        
        # Si los niveles son iguales 
        else:
            return 0.5      # 50% de probabilidades de ganar

    # Método que muestra un diálogo y opciones para el jugador antes de la batalla
    @staticmethod
    def mostrar_dialogo_opcion(probabilidad_ganar):
        
        # Recibe como parámetro la probabilidad de ganar y retorna la opción ingresada por el jugador
        return int(
            input(
                f"\nCon tu nivel actual, tienes {probabilidad_ganar * 100}% "
                "de probabilidades de ganarle al Orco.\n"
                "\nSi ganas, ganarás 50 puntos de experiencia y el orco perderá 30. \n"
                "Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.\n"
                "\n¿Qué deseas hacer?\n"
                "1. Atacar\n"
                "2. Huir\n"
            )
        )
