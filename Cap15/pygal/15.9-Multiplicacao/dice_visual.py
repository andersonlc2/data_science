import pygal
from die import Die

# Cria dois dados D8
die_1 = Die()
die_2 = Die()

# Faz alguns lançamentos e armazena os resultados em uma lista.
results = [die_1.roll() * die_2.roll()
           for roll_num in range(100000)]

# Analiza os resultados
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualiza os resultados
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 100000 times."
hist.x_labels = list(str(item) for item in range(2, max_result+1))
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6 * D6', frequencies)
hist.render_to_file('dice_visual.svg')
