import matplotlib.pyplot as plt


elements = ["H", "C", "O", "N", "S", "Cl", "F", "Na", "Mg", "K"]
electronegativities = [2.20, 2.55, 3.44, 3.04, 2.58, 3.16, 3.98, 0.93, 1.31, 0.82]
molar_masses = [1.01, 12.01, 16.00, 14.01, 32.06, 35.45, 18.998, 22.99, 24.305, 39.098]

# Gráfica 1: Electronegatividad vs Elemento
def plot_electronegativity():
    plt.figure(figsize=(8, 5))
    plt.bar(elements, electronegativities, color='skyblue')
    plt.title("Relación entre elementos y electronegatividad")
    plt.xlabel("Elemento")
    plt.ylabel("Electronegatividad")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Gráfica 2: Masa molar vs Elemento
def plot_molar_mass():
    plt.figure(figsize=(8, 5))
    plt.plot(elements, molar_masses, marker='o', color='green')
    plt.title("Relación entre elementos y su masa molar")
    plt.xlabel("Elemento")
    plt.ylabel("Masa Molar (g/mol)")
    plt.grid(alpha=0.7)
    plt.show()

# Gráfica 3: Viscosidad vs Temperatura
def plot_viscosity_temperature():
  
    temperatures = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]  
    viscosities = [150, 130, 110, 95, 80, 65, 50, 40, 30, 20]  
    
    plt.figure(figsize=(8, 5))
    plt.plot(temperatures, viscosities, marker='o', color='red')
    plt.title("Relación entre viscosidad y temperatura (Aceite de Motor)")
    plt.xlabel("Temperatura (°C)")
    plt.ylabel("Viscosidad relativa")
    plt.grid(alpha=0.7)
    plt.show()
