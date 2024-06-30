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

# Función para encontrar la ruta más corta
def dijkstra(graph, start, end, has_visa):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        cost, node, path = heappop(queue)
        if node == end:
            return cost, path + [node]
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph[node].items():
            if neighbor == end or (has_visa and neighbor in ['AUA', 'BON', 'CUR', 'SXM', 'SDQ']):
                heappush(queue, (cost + weight, neighbor, path + [node]))
    return float('inf'), []

# Interfaz de usuario
while True:
    origin = input("Ingrese el código del aeropuerto de origen: ").upper()
    destination = input("Ingrese el código del aeropuerto de destino: ").upper()
    has_visa = input("¿Tiene el pasajero visa? (s/n): ").lower() == 's'
    
    cost, path = dijkstra(graph, origin, destination, has_visa)
    if cost == float('inf'):
        print("No se encontró una ruta válida.")
    else:
        print(f"Ruta más corta: {' -> '.join(path)}")
        print(f"Costo total: ${cost:.2f}")
    
    print()