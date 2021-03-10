# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
from Population import ImageClass
import time

I_PATH = "test.jpg"
x = ImageClass(I_PATH, 7, 3)
x.print_poly_image()
start = time.time()
fit_vec = []


for i in range(1000):
    x.do_the_evolution()
    if i%100 == 0:
        end = time.time()
        print('Iteration:', i, ' Elapsed time: ', end-start)
        start = time.time()

    if i%10 == 0:
        summ = x.fitness_sum
        fit_vec.append(summ)

plt.plot(fit_vec)
plt.show()
x.print_poly_image()
x.print_values()
