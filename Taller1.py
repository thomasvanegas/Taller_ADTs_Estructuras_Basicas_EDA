# Importacion de paquetes y clases
from Persona import Persona
from Agente import Agente
from Fila import Fila

# Funciones optimizacion de agentes
def calcularTiempoEsperaFilaPromedio(f: list[Persona]):

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
        persona = Persona()
        f.enqueue(persona)
    
    # Creacion de N agentes
    for i in range(n):
        agente = Agente()
        agentes.append(agente)

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