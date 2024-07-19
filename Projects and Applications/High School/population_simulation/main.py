import matplotlib.pyplot as plt

import population

population = population.Population(1000, 1000, 10, 5, 15, 5)
population.start()
stats = population.get_stats()

print(stats)

plt.plot(list(range(0, 1000)), stats["population"])
plt.xlabel("Year")
plt.ylabel("Population")
plt.show()
