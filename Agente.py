# Importación de paquetes y clases
from Persona import Persona

class Agente():
    
    # atributo contador para el secuencial de ID's
    _contador_ids: int = 1
    
    """"
    Constructor
    """
    def __init__ (self):
        self._id: int = Persona._contador_ids
        
        # incrementando el contador de ids
        Persona._contador_ids += 1