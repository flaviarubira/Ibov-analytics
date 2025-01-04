# Visualização de dados
import matplotlib.pyplot as plt

def plot_prices(data):
    data['Close'].plot(title="IBOV - Preços de Fechamento")
    plt.show()
