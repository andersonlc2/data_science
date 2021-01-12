import pygal
from die import Die

# Cria um D6
die = Die()

# Faz alguns lançamentos e armazena os resultados em uma lista.
results = list(die.roll() for roll_num in range(1000))
# Lista original.
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)


# Analiza os resultados
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]
# Lista original.
# for value in range(1, die.num_sides+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

# Visualiza os resultados
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = list(str(item) for item in range(1, die.num_sides+1))
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
