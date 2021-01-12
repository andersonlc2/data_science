import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Continua cirando vários passeios aleatórios.
while True:
    # Cria um passeio aleatório e plota os pontos.
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Define o tamanho da janela de plotagem.
    plt.figure(dpi=128, figsize=(13, 7))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                cmap=plt.cm.Blues, s=1)

    # Enfatiza o primeiro e o último ponto.
    plt.scatter(0, 0, c='green', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

    # Remove os eixos.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
