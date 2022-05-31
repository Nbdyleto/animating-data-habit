import pandas as pd
import random

# how to work better with dates? 
may_days = [1 + i for i in range(30)]
print(may_days)

habits = [random.randint(0, 4) for i in range(len(may_days))]
print(habits)

plot_steps = [habits[0]]
last_habit = habits[0]

4, 3

for i in range(1, len(habits)):
    differences = habits[i] - last_habit 
    differences /= 50
    for j in range(51):
        plot_steps.append(last_habit + differences * j)
    last_habit = habits[i]

print(plot_steps)
