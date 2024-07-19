import sim

import matplotlib.pyplot as plt

simulation = sim.Sim(500, 10, 0.5)
simulation.run()

print(simulation.stats)

plt.plot(range(0, 501), simulation.stats["total_queue"])
plt.title("People in queue per minute")
plt.xlabel("Time (min)")
plt.ylabel("People waiting")
plt.show()
