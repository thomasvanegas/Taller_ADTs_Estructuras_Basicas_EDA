# Importacion de paquetes y clases
from Persona import Persona
from Agente import Agente
from Fila import Fila



if __name__ == "__main__":
    # Instanciamiento de clases
    f = Fila()
    p1 = Persona()
    p2 = Persona()
    
    # Pruebas al método __str__
    print(p1)
    print(p2)
    print(f)