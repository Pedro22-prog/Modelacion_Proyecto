from Datos.Data import Data
from Grafico import Grafico
from App import App
from Datos.SeleccionArch import start_file_selector

def main():
    archivo_vuelos, archivo_visas, archivo_aeropuertos = start_file_selector()
    
    if not (archivo_vuelos and archivo_visas and archivo_aeropuertos):
        print("Ningún archivo fue seleccionado. Saliendo del programa.")
        return

    datos = Data(archivo_vuelos, archivo_visas, archivo_aeropuertos)
    grafico = Grafico(len(datos.vertices), datos.visas, datos.codes)

    for vuelo in datos.vuelos:
        origen = datos.vertices[vuelo[0]]
        destino = datos.vertices[vuelo[1]]
        costo = vuelo[2]
        grafico.add_edge(origen, destino, costo)

    app = App(grafico)
    app.run()

if __name__ == "__main__":
    main()