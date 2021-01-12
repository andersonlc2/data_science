import matplotlib.pyplot as plt
import pygal
from die import Die
from random_walk import RandomWalk


"""Frequencia dados com matplot."""
# Cria dois dados D8
die_1 = Die()
die_2 = Die()

# Faz alguns lançamentos e armazena os resultados em uma lista.
results = [die_1.roll() + die_2.roll()
           for roll_num in range(100000)]

# Analiza os resultados
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

eixo_x = list(item for item in range(2, max_result+1))

plt.plot(eixo_x, frequencies, linewidth=5, c='red')
plt.title("Results of rolling two D6 dice 1000 times")
plt.xlabel("Dies", fontsize='12')
plt.ylabel("Frequency", fontsize='12')

plt.savefig("dice_visual.png")


"""Passeio com pygal."""

rw = RandomWalk()

rw.fill_walk()
x = rw.x_values
y = rw.y_values

hist = pygal.XY(stroke=False)

hist.title = "Random pass with Pygal."
hist.x_labels = list(str(item) for item in range(0, rw.num_points))
# hist.x_title = "Results"
# hist.y_title = "Frequency of Result"

hist.add("Pass", [(30, 5)])
hist.render_to_file('random_pass.svg')
