# Importación de paquetes y clases
from pickle import FALSE
from Persona import Persona

class Agente():
    
    # atributo contador para el secuencial de ID's
    _contador_ids: int = 1
    
    """"
    Constructor
    """
    def __init__ (self):
        self._id: int = Persona._contador_ids
        self.ocupado = False
        self.tiempo_ocupado = 0

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
    
    def getOcupado(self):
        return self._ocupado
    
    def setOcupado(self, ocupado: bool):
        self._ocupado = ocupado
    
    def getTiempoOcupado(self):
        return self._tiempo_servicio
    
    def setTiempoOcupado(self, tiempo_ocupado: int):
        self._tiempo_ocupado = tiempo_ocupado

    # Sobrecargando el método print()
    def __str__(self) -> str:
        return f"""
                Soy el agente con id: {self.id},
                y mi tiempo total ocupado fue: {self.tiempo_ocupado}
                """