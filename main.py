import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt

# how to work better with dates? 
may_days = [1 + i for i in range(10)]
print(may_days)

habits = [random.randint(0, 4) for i in range(len(may_days))]
print(habits)

plot_steps = np.array([habits[0]])
last_habit = habits[0]

4, 3

for i in range(1, len(habits)):
    differences = habits[i] - last_habit 
    differences /= 50
    for j in range(51):
        plot_steps = np.append(plot_steps, [last_habit + differences * j], 0)
    last_habit = habits[i]

print(plot_steps)

# plotting:

may_days = iter(may_days)
day = next(may_days)

for i, step in enumerate(plot_steps):
    if i%50==0:
        # i%50 represents that program passed for all steps of a transition
        day = next(may_days)
    plt.xlim(0,4)
    plt.barh('May Habits', step)
    plt.text(0.8, 0.2, f'day {day} is conclude {habits[day-1]} habits', fontsize=10)
    plt.pause(0.000000000000000000000000001)
    plt.clf()
plt.show

