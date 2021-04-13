# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import numpy as np
from Version_1.Population_v1 import PopulationClass
import time


I_PATH = "Test_images/test4.jpg"
x = PopulationClass(I_PATH,4,12)
x.print_poly_image()
x.print_values()
start = time.time()
fit_vec = []
fitt = 100000000
for i in range(2000):
    x.do_the_evolution()
    if i%100 == 0:
        end = time.time()
        print('Iteration:', i, ' Elapsed time: ', end-start)
        start = time.time()
        summ = x.fitness_sum
        fit_vec.append(summ)
        if summ < fitt and i >200:
            fitt = summ
            # a = copy.deepcopy(x)
        #print(summ)
        # x.print_poly_image()

plt.plot(fit_vec)
plt.show()
x.print_poly_image()
# a.print_poly_image()
x.print_values()