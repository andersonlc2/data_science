import matplotlib.pyplot as plt

x_cub = list(range(1, 5000))
y_cub = [x**3 for x in x_cub]

plt.scatter(x_cub, y_cub, c=y_cub, cmap=plt.cm.Greys, s=10)
plt.title("Cubo dos 5000 primeiros numeros")
plt.xlabel("Bases", fontsize=10)
plt.ylabel("Cubos", fontsize=8)

plt.tick_params(axis="both", which="major", labelsize=10)
plt.axis([0, 5100, 0, 125000000000])

plt.savefig("cap15_15.2_Cubos_coloridos.png")
plt.show()
