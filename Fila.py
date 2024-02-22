# Importacion de paquetes y clase
from Persona import Persona

# Orden FIFO -> FILA <-> COLA <-> QUEUE

class Fila:

    def __init__ (self):
        """
            Constructor: Implentación de una fila de personas, inicialmente, vacia.
        """
        self._fila_personas = []

    def enqueue(self, persona: Persona):
        """
            Se agrega una Persona al final de la fila
        """
        self._fila_personas.append(persona)

    def dequeue(self) -> Persona:
        """
            Obtiene la primera persona de la fila (Fist in)
        """
        persona = self._fila_personas[0]
        self._fila_personas = self._fila_personas[1:]
        return persona

    def size(self) -> int:
        """
            Método que retorna el número de personas que hay en la fila. Retorna un int.
        """
        return len(self._fila_personas)

    def isEmpty(self):
        """"
            Método que comprueba si la fila está vacia. Retorna True si está vacia.
        """
        return self.size() == 0

    def __iter__(self):
        """
            Retorna un iterador en orden FIFO para el Queue.
            Reutiliza el iterador de la lista.
        """
        return iter(self._fila_personas)
