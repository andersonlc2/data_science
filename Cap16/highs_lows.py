import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Obtém as temperaturas máximas do arquivo.
filename = 'sitka_weather_2014.csv'
# filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Fas a plotagem dos dados.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Formata o gráfico.
if (filename == 'death_valley_2014.csv'):
    plt.title(
        "Daily high and low temperatures - 2014\nDeath Valley - CA", fontsize=16)
else:
    plt.title("Daily high and low temperatures - 2014\nSitka - AL", fontsize=16)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.axis([dates[0], dates[-1], 0, 120])

plt.show()
