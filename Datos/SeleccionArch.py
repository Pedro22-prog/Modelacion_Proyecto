import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv

class FileSelector:
    def __init__(self, root):
        self.root = root
        self.root.title("Seleccionar Archivos CSV")
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.flights_label = ttk.Label(frame, text="No seleccionado")
        self.visas_label = ttk.Label(frame, text="No seleccionado")
        self.airports_label = ttk.Label(frame, text="No seleccionado")

        ttk.Label(frame, text="Seleccionar archivos CSV:").grid(row=0, column=0, columnspan=3, pady=10)

        ttk.Button(frame, text="Seleccionar Vuelos", command=lambda: self.select_file("Vuelos", self.flights_label)).grid(row=1, column=0, pady=5)
        self.flights_label.grid(row=1, column=1, columnspan=2, sticky=tk.W)

        ttk.Button(frame, text="Seleccionar Visas", command=lambda: self.select_file("Visas", self.visas_label)).grid(row=2, column=0, pady=5)
        self.visas_label.grid(row=2, column=1, columnspan=2, sticky=tk.W)

        ttk.Button(frame, text="Seleccionar Aeropuertos", command=lambda: self.select_file("Aeropuertos", self.airports_label)).grid(row=3, column=0, pady=5)
        self.airports_label.grid(row=3, column=1, columnspan=2, sticky=tk.W)

        ttk.Button(frame, text="Continuar", command=self.validate_files).grid(row=4, column=0, columnspan=3, pady=10)

    def select_file(self, file_type, label):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        label.config(text=file_path if file_path else f"No seleccionado ({file_type})")

    def validate_files(self):
        expected_headers = {
            'Vuelos': ['origin', 'destination', 'cost'],
            'Visas': ['airport', 'visa_required'],
            'Aeropuertos': ['code', 'name']
        }

        for file_type, label in [('Vuelos', self.flights_label), ('Visas', self.visas_label), ('Aeropuertos', self.airports_label)]:
            file_path = label.cget("text")
            if file_path == f"No seleccionado ({file_type})":
                messagebox.showerror("Error", f"Debe seleccionar el archivo CSV de {file_type}.")
                return

            if not self.validate_csv(file_path, expected_headers[file_type]):
                messagebox.showerror("Error", f"El archivo CSV de {file_type} no tiene el formato esperado.")
                return

        self.root.destroy()

    def validate_csv(self, file_path, expected_headers):
        try:
            with open(file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                headers = reader.fieldnames
                return headers == expected_headers
        except (FileNotFoundError, csv.Error):
            return False

def start_file_selector():
    root = tk.Tk()
    selector = FileSelector(root)
    root.mainloop()
    return (selector.flights_label.cget("text"),
            selector.visas_label.cget("text"),
            selector.airports_label.cget("text"))