import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Obtém os dados dos arquivos.
filename = "sitka_weather_2014.csv"

with open(filename) as f:
    reader = csv.reader(f)
    read_row = next(reader)

    dates, pulvs = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            pul = float(row[19])
        except ValueError:
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            pulvs.append(pul)

# Plotagem dos dados.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, pulvs, c='blue', alpha=0.4)

title = 'Daily rainfall amounts - 2014 \n Sitka, AK'
plt.title(title, fontsize=16)
plt.xlabel('', fontsize=10)
fig.autofmt_xdate()
plt.ylabel("Rainfall (in)", fontsize=10)

# Configurações.
plt.tick_params(axis='both', which='major', labelsize=8)
plt.axis([dates[0], dates[-1], 0, 4])

plt.savefig("16.3-Pluviometria.png")
plt.show()
