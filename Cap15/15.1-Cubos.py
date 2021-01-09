import matplotlib.pyplot as plt

y_eixo = list(range(1, 5))
x_eixo = [x**3 for x in y_eixo]

plt.scatter(x_eixo, y_eixo, s=50, c='red')
plt.title("Cubos dos primeiros 5 numeros")
plt.xlabel("Cubos", fontsize=14)
plt.ylabel("Bases", fontsize=10)

plt.tick_params(axis='both', which='major', labelsize=8)

plt.savefig("cap15_15.1_Cubos.png")
plt.show()

