# Still in progres, not working

import matplotlib.pyplot as plt
from New.Evo_object_new import ImageClass
import time

I_PATH = "test.jpg"
x = ImageClass(I_PATH, 7, 3)
x.print_poly_image()
start = time.time()
fit_vec = []
print('test test')

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
