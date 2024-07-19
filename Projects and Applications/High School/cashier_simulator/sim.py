import cashier
import customer

import random


class Sim:
    def __init__(self, t, num_cashiers, rate):
        self._num_cashiers = num_cashiers
        self._rate = rate
        self.min = t
        self.stats = {"total_queue": []}
        self._total_queue = 0

        self._cashiers = []
        for _ in range(self._num_cashiers):
            self._cashiers.append(cashier.Cashier())

    def _update_stats(self):
        self.stats["total_queue"].append(self._total_queue)

    def run(self):
        while self.min >= 0:
            self.min -= 1

            sorted_cashiers = sorted(self._cashiers, key=lambda x: x.line)

            if random.random() < self._rate:
                for _ in range(random.randint(1, 4)):
                    sorted_cashiers[0].line += 1
                    sorted_cashiers[0].customers.append(customer.Customer())
                    self._total_queue += 1

            for staff in self._cashiers:
                if len(staff.customers) > 0:
                    if staff.customers[0].items <= 0:
                        staff.customers.pop(0)
                        staff.line -= 1
                        self._total_queue -= 1
                    else:
                        staff.customers[0].items -= staff.speed

            self._update_stats()
