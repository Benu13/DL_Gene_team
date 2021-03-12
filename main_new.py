# Still in progres, not working

import matplotlib.pyplot as plt
from New.Population_new import Population
import time

I_PATH = "Test_images/ml.jpg"
x = Population(I_PATH, 5, 20, 80)
x.print_best_image()
start = time.time()
fit_vec = []

for i in range(1000):
    x.do_the_evolution()
    fit_vec.append(x.fitness_best)
    if i%10 == 0:
        end = time.time()
        print('Iteration:', i, ' Elapsed time: ', end-start)
        start = time.time()

plt.plot(fit_vec)
plt.show()
x.print_best_image()
