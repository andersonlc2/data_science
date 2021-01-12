import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]  # Iniciamos uma lista.

# Passa a lista (y), os valores de saída (x)  e o parametro linewidth para a largura da linha.
plt.plot(input_values, squares, linewidth=5)

# Define o título do gráfico e nome os eixos.
plt.title("Squares Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#  Define o tamanho dos rótulos das mascações
plt.tick_params(axis='both', labelsize=10)


plt.show()  # Exibe o gráfico na tela.
