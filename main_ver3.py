import matplotlib.pyplot as plt
from Version_3.Population_v3 import Population
import time
from PIL import Image


I_PATH = "Test_images/test.jpg"
x = Population(I_PATH, 4, 30)
x.print_best_image()
start = time.time()
fit_vec = []
plot = 0

for i in range(1000):
    x.do_the_evolution()
    fit_vec.append(x.fitness_best)
    if i%100 == 0:
        end = time.time()
        print('Iteration:', i, ' Elapsed time: ', end-start)
        start = time.time()
    if (i%100 == 0) and (plot == 1):
        im = Image.fromarray(x.get_best_image())
        im.save("Out_image2/Out_" + str(i) + ".jpeg")
plt.plot(fit_vec)
plt.show()
x.print_best_image()
