# Importacion de paquetes y clases
from Persona import Persona
from Agente import Agente
from Fila import Fila



if __name__ == "__main__":
    # Instanciamiento de clases
    f = Fila()
    agentes = []
    
    # Creación de personas
    for i in range(20):
        persona = Persona()
        f.enqueue(persona)
    
    # Creacion de agentes
    for i in range(5):
        agente = Agente()
        agentes.append(agente)

    # Pruebas al método __str__
    for persona in f:
        print(persona)

    print(f)