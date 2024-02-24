# Importacion de paquetes
import random

class Persona:
    
    # atributo contador para el secuencial de ID's
    _contador_ids: int = 1
    
    """
    Constructor
    """
    def __init__ (self, tiempo_llegada: int, tiempo_espera_fila: int):
        self._id: int = Persona._contador_ids
        self._tiempo_llegada: int = tiempo_llegada #random.randint(0, 28800)
        self._tiempo_servicio: int = random.randint(300, 3600)
        self._tiempo_espera_fila: int = tiempo_espera_fila #random.randint(1, 1800)
        
        # incrementando el contador de ids
        Persona._contador_ids += 1

    """
    Construcción de los metodos getters y setters para garantizar el encapsulamiento
    """
    def getId(self):
        return self._id
    
    def setId(self):
        self._id = Persona._contador_ids
        # incrementando el contador de ids
        Persona._contador_ids += 1
    
    def getTiempoLlegada(self):
        return self._tiempo_llegada
    
    def setTiempoLlegada(self, tiempo_llegada: int):
        self._tiempo_llegada = tiempo_llegada
    
    def getTiempoServicio(self):
        return self._tiempo_servicio
    
    def setTiempoServicio(self, tiempo_servicio: int):
        self._tiempo_servicio = tiempo_servicio

    def getTiempoEsperaFila(self):
        return self._tiempo_espera_fila
    
    def setTiempoEsperaFila(self, tiempo_espera_fila: int):
        self._tiempo_espera_fila = tiempo_espera_fila

    # Sobrecargando el método print()
    def __str__ (self) -> str:
        return f"""
                Soy la persona con id: {self._id} \n 
                La hora de llegada fue a los {self._tiempo_llegada} segundos \n
                Mi tiempo de espera en la fila fue de: {self._tiempo_espera_fila} segundos \n
                El tiempo total del servicio fue de: {self._tiempo_servicio} segundos
                """