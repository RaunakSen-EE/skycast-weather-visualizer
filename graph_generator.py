import matplotlib.pyplot as plt

def generate_temperature_graph(temps):

    plt.figure(figsize=(5, 3))

    plt.plot(temps, marker='o')

    plt.title("Temperature Trend")
    plt.xlabel("Search Number")
    plt.ylabel("Temperature °C")

    plt.grid(True)

    plt.savefig("temp_graph.png")

    plt.close()