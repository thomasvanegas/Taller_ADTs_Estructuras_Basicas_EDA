# Importacion de paquetes y clases
from Persona import Persona
from Agente import Agente
from Fila import Fila



if __name__ == "__main__":
    # Instanciamiento de clases
    f = Fila()
    
    # Creación de personas
    for i in range(10):
        persona = Persona()
        f.enqueue(persona)
    
    # Pruebas al método __str__
    for persona in f:
        print(persona)

    print(f)