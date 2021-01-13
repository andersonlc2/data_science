import csv

from datetime import datetime
from matplotlib import pyplot as plt


# Obtém as temperaturas máximas e mínimas do arquivo.
filename_one = 'sitka_weather_2014.csv'
filename_two = 'death_valley_2014.csv'


def apply(file):
    with open(file) as f:
        reader = csv.reader(f)
        reader_row = next(reader)

        dates, highs, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = (int(row[1]))
                low = (int(row[2]))
            except ValueError:
                print(current_date, "missing data")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

    return dates, highs, lows


dates_sitka, highs_sitka, lows_sitka = apply(filename_one)
dates_dvalley, highs_dvalley, lows_dvalley = apply(filename_two)

# Faz a plotagem dos dados.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates_sitka, highs_sitka, c='red', alpha=0.5)
plt.plot(dates_sitka, lows_sitka, c='red', alpha=0.5)
plt.fill_between(dates_sitka, highs_sitka, lows_sitka,
                 facecolor='red', alpha=0.1)

plt.plot(dates_dvalley, highs_dvalley, c='blue', alpha=0.5)
plt.plot(dates_dvalley, lows_dvalley, c='blue', alpha=0.5)
plt.fill_between(dates_dvalley, highs_dvalley, lows_dvalley,
                 facecolor='blue', alpha=0.1)

plt.title(
    "Daily high and low temperatures in \nDeath Valley, CA - Sitka, Alasca", fontsize=16)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=12)

plt.tick_params(axis='both', which='major', labelsize=10)
plt.axis([dates_dvalley[0], dates_dvalley[-1], 0, 120])

plt.savefig("16.2-Comparacao_Sitka_DeathValley.png")
plt.show()
