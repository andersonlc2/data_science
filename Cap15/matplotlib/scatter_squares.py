import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
# 's' = tamanho da marcação, 'edgecolors' = borda, 'c' = cor, c=('tipo um rgb(de 0 a 1)')
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=40)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Square of Value", fontsize=10)

# Define o tamnho dos rótulos das marcações.
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 1100, 0, 1100000])


# salva altomaticamente os gráficos - 'bbox_inches='tight' = deixa espaços em braco
plt.savefig('squares_plot.png', bbox_inches='tight')
