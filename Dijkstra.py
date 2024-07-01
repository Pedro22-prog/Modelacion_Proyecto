from collections import defaultdict
from heapq import heappush, heappop

# Grafo con las tarifas de los vuelos
graph = {
    'CCS': {'AUA': 40, 'CUR': 35, 'BON': 60, 'SXM': 300, 'SDQ': 180, 'POS': 150, 'BGI': 180},
    'AUA': {'CUR': 15, 'BON': 15, 'SXM': 85},
    'CUR': {'BON': 15, 'SXM': 80},
    'SDQ': {'SXM': 50},
    'SXM': {'SBH': 45, 'BGI': 70, 'PTP': 100},
    'POS': {'BGI': 35, 'SXM': 90, 'PTP': 80, 'FDF': 75},
    'BGI': {'SXM': 70},
    'PTP': {'SXM': 100, 'SBH': 80}
}

# Diccionario para almacenar las rutas
routes = defaultdict(list)

# Función para encontrar la ruta más corta
def dijkstra(graph, start, end, has_visa):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        cost, node, path = heappop(queue)
        if node == end:
            routes[f"{start} to {end}"].append(path + [node])
            return cost, path + [node]
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph[node].items():
            if neighbor == end or (has_visa and neighbor in ['AUA', 'BON', 'CUR', 'SXM', 'SDQ']):
                heappush(queue, (cost + weight, neighbor, path + [node]))
    return float('inf'), []

# Función para validar el código del aeropuerto
def validate_airport_code(code):
    return len(code) == 3 and code.isupper() and code in graph

# Función para validar la visa
def validate_visa(visa):
    return visa.lower() in ['s', 'n']

# Interfaz de usuario
while True:
    origin = input("Ingrese el código del aeropuerto de origen: ").upper()
    while not validate_airport_code(origin):
        origin = input("Código de aeropuerto de origen inválido. Inténtelo de nuevo: ").upper()
    
    destination = input("Ingrese el código del aeropuerto de destino: ").upper()
    while not validate_airport_code(destination):
        destination = input("Código de aeropuerto de destino inválido. Inténtelo de nuevo: ").upper()
    
    has_visa = input("¿Tiene el pasajero visa? (s/n): ")
    while not validate_visa(has_visa):
        has_visa = input("Respuesta de visa inválida. Inténtelo de nuevo (s/n): ")
    has_visa = has_visa.lower() == 's'
    
    cost, path = dijkstra(graph, origin, destination, has_visa)
    if cost == float('inf'):
        print("No se encontró una ruta válida.")
    else:
        print(f"Ruta más corta: {' -> '.join(path)}")
        print(f"Costo total: ${cost:.2f}")
    
    print()

# Mostrar las rutas
print("Rutas guardadas:")
for route, paths in routes.items():
    print(f"\n{route}:")
    for path in paths:
        print(" -> ".join(path))