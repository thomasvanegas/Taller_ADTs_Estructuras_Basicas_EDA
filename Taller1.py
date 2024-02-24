# Importacion de paquetes y clases
from Persona import Persona
from Agente import Agente
from Fila import Fila

# Funciones optimizacion de agentes
def calcularTiempoEsperaFilaPromedio(f: list[Persona]) -> int:

    # f <=> fila

    tiempos: list[int] = []
    sumatoria = 0

    # obtener en tiempo de espera en la fila de cada persona
    for persona in f:
        tiempo_espera = persona.getTiempoEsperaFila()
        tiempos.append(tiempo_espera)


    for tiempo in tiempos:
        sumatoria += tiempo


    promedio = sumatoria / len(tiempos)

    # list -> numpy array
    # array = np.array(tiempo_espera)
    # promedio = np.mean(array)

    print(f"El promedio de los tiempos de espera en la fila es: {promedio}")

    return promedio

def calcularTiempoOcupacionAgentePromedio(a: list[Agente]):
    # Variables globales
    tiempos: list[int] = []
    sumatoria = 0

    for agente in a:
        if isinstance(agente, Agente):
            tiempo_ocupado = agente.getTiempoOcupado()
            tiempos.append(tiempo_ocupado)

            for tiempo in tiempos:
                sumatoria += tiempo

            promedio = sumatoria / len(tiempos)

        else:
            print("El objeto pasado como agente, no es una instancia de la clase Agente")
        
        print(f"El promedio de tiempo ocupado de los agentes es: {promedio}")



def optimizarNumeroAgentes():
    return 0

# Ejecución, Inicialización, Presentación de los resultados de la simulación.
if __name__ == "__main__":

    # Instanciamiento de clases - Creación de la fila y lista de agentes
    f = Fila()
    agentes: list[Agente] = []

    # Solicitud de datos -> Solicitud de los N agentes y M personas.
    m = int(input("Ingrese, por favor, la cantidad de personas: "))
    n = int(input("Ingrese, por favor, la cantidad de agentes: "))
    
    # Creación de M personas
    for i in range(m):
        tiempo_llegada = int(input(f"Digite el tiempo de llegada de la persona {i + 1}: [0, 28800] -> "))
        tiempo_espera_fila = int(input(f"Digite el tiempo de espera en la fila de la persona {i + 1}: [1, 1800] -> "))
        persona = Persona(tiempo_llegada, tiempo_espera_fila)
        f.enqueue(persona)
    
    # Creacion de N agentes
    for i in range(n):
        agente = Agente()
        agentes.append(agente)


    # --- ORDENAMIENTO DE LAS PERSONAS EN LA FILA POR TIEMPO DE LLEGADA ---
    fila_ordenada = sorted(f, key= lambda x: x.getTiempoLlegada())

    # Imprimiendo la fila ordenada por tiempo de llegada
    for persona in fila_ordenada:
        print(f"\nSoy la persona con id: {persona.getId()} y mi tiempo de llegada fue: {persona.getTiempoLlegada()}\n")

    # Pruebas al método __str__ de la clase Persona
    for persona in f:
        print(persona)
    
    # Pruebas al método __str__ de la clase Agente
    for agente in agentes:
        print(agente)

    # Pruebas al método __str__ de la clase Fila
    print(f)
    
    print("\n --- TIEMPO PROMEDIO DE ESPERA EN LA FILA --- ")
    calcularTiempoEsperaFilaPromedio(f)

    print("\n --- TIEMPO PROMEDIO DE OCUPACION DE TODOS LOS AGENTES --- ")
    calcularTiempoOcupacionAgentePromedio(agentes)