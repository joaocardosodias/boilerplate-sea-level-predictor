import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Leitura do arquivo de dados
    df = pd.read_csv('epa-sea-level.csv')

    # Criação do gráfico de dispersão
    plt.figure(figsize=(10, 6))  # Define o tamanho da figura
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])  # Plota os pontos de dados

    # Primeira linha de tendência com todos os dados
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])  # Calcula a regressão linear
    x_pred = pd.Series(range(1880, 2051))  # Cria série de anos até 2050
    y_pred = result.slope * x_pred + result.intercept  # Calcula os valores previstos
    plt.plot(x_pred, y_pred, 'r')  # Plota a linha em vermelho

    # Segunda linha de tendência apenas com dados a partir de 2000
    df_recent = df[df['Year'] >= 2000]  # Filtra dados a partir de 2000
    result_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])  # Calcula nova regressão
    x_pred_recent = pd.Series(range(2000, 2051))  # Cria série de anos de 2000 até 2050
    y_pred_recent = result_recent.slope * x_pred_recent + result_recent.intercept  # Calcula valores previstos
    plt.plot(x_pred_recent, y_pred_recent, 'g')  # Plota a linha em verde

    # Adição de rótulos e título
    plt.xlabel('Year')  # Rótulo do eixo x
    plt.ylabel('Sea Level (inches)')  # Rótulo do eixo y
    plt.title('Rise in Sea Level')  # Título do gráfico
    
   
    plt.savefig('sea_level_plot.png')
    return plt.gca()