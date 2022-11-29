import matplotlib.pyplot as plt
import numpy as np
import csv

data_by_year = {}

for i in range(19):
    data_by_year[i*10 + 1840] = []

with open("populations.csv") as f:
    reader = csv.reader(f, delimiter=',')
    f.readline()
    for row in reader:
        data_by_year[int(row[0])].append((row[1], int(row[2])))

# print(data_by_year)

data_by_city = {}

for year in data_by_year:
    for i in data_by_year[year]:
        if i[0] in data_by_city:
            data_by_city[i[0]].append([year, i[1]])
        else:
            data_by_city[i[0]] = []
            data_by_city[i[0]].append([year, i[1]])

# print(data_by_city)

x = np.arange(1840, 2030, 10)
for i, k in data_by_city.items():
    years = [j[0] for j in k]
    pop = [j[1] for j in k]
    plt.plot(years, pop, c=np.random.rand(3, ), label = i)

plt.xlabel("Years")
plt.ylabel("Population (in hundreds of thousands)")
plt.title("Most Populous Cities from 1840 - 2020")
plt.legend()
plt.show()