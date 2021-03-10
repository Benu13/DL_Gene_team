# Class implementation of population
# Original image will be necessary for individual polygon evaluation, at least in this idea.
# Using colors and checking how well created polygon align with corresponding fragments on original image we can see how
# good it's genes are.

import numpy as np
from Original.Evo_object import Polygon
from numpy import asarray
from PIL import Image
import matplotlib.pyplot as plt
import numexpr as ne


class PopulationClass:
    def __init__(self, im_path: str, max_poly_edges: int = 4, population_size: int = 50):
        self.original_image = asarray(Image.open(im_path))  # Normalised to [0-1]
        self.canvas_size = (self.original_image.shape[1], self.original_image.shape[0])
        self.max_edges = max_poly_edges
        self.created_image = None
        self.fitness = np.zeros(population_size)
        self.fitness_sum = None
        self.population_size = population_size
        self.individuals = [Polygon(self.max_edges, self.canvas_size) for i in range(self.population_size)]
        self.fitness_individual()

    def print_values(self) -> None:     # Nie robi za wiele
        print('Population size = ', self.population_size)
        print('Maximum no. polygon edges = ', self.max_edges)
        print('Canvas size = ', self.canvas_size[0:2])

    def get_poly_image(self):   # Na przezroczyste tło wklejamy utworzone wielokąty z kanałem alfa = 50% (transparency)
        back = Image.new("RGBA", self.canvas_size[0:2], (0, 0, 0, 0))
        object_index = 0
        for individual in self.individuals:
            back.paste(individual.poly_image, mask=individual.poly_image)
            object_index = object_index + 1

        self.created_image = np.asarray(back)[..., :3]      # Wybieramy tylko kanały RGB obrazu bez przezroczystości

    def print_poly_image(self):     # Wyświetlanie obrazu
        self.get_poly_image()
        plt.imshow(self.created_image)
        plt.show()

    def fitness_individual(self):   # Funkcja celu dla każdego wielokąta z osobna
        # Obliczamy odległość Euklidesową między punktami w przestrzeni 3D dla współrzędnych złożonych z wartości RGB
        # obrazu oryginalnego oraz obrazu zawierającego dany wielokąt. Dla każdego piksela w obrazach.
        i = 0
        for individual in self.individuals:
            poly_cre = (np.asarray(individual.poly_image))  # Obraz wielokąta
            true_cre = self.original_image  # Obraz oryginalny
            true_cre2 = 1*(self.individuals[i].poly_mask) # Maska binarna wielokąta
            aa0 = np.multiply(true_cre[..., 0], true_cre2)    # kolor R fragmentu obrazu oryginalnego (obraz org * maska)
            aa1 = np.multiply(true_cre[..., 1], true_cre2)    # kolor G fragmentu obrazu oryginalnego (obraz org * maska)
            aa2 = np.multiply(true_cre[..., 2], true_cre2)    # kolor B fragmentu obrazu oryginalnego (obraz org * maska)
            a0 = true_cre[..., 0]   # kolor R org
            a1 = true_cre[..., 1]   # kolor G org
            a2 = true_cre[..., 2]   # kolor B org
            b0 = poly_cre[..., 0]   # kolor R wielokąta
            b1 = poly_cre[..., 1]   # kolor G wielokąta
            b2 = poly_cre[..., 2]   # kolor B wielokąta

            fitness_local = np.int(ne.evaluate('sum((aa0/255-b0/255)**2 + (aa1/255-b1/255)**2 + (aa2/255-b2/255)**2)'))
            #fitness_local = np.int(ne.evaluate('sqrt(fitness_local)'))
            fitness = np.int(ne.evaluate('sum((a0/255-b0/255)**2 + (a1/255-b1/255)**2 + (a2/255-b2/255)**2)'))  # * fitness_local
            #fitness = np.int(ne.evaluate('sqrt(fitness)'))
            self.fitness[i] = fitness
            individual.fitness = self.fitness[i]
            i = i + 1

    def do_the_evolution(self):     # Ewolucja
        # Wybrane zostają tylko najlepsze osobniki (najlepiej dopasowane). Każda para daje 4 dzieci, do końcowej listy
        # dodane zostają tylko rodzice oraz ich dzieci
        sorted_fitness = (np.argsort(self.fitness))
        passing_size = 4
        self.fitness_sum = sum(self.fitness[sorted_fitness[0:4]])
        #print(self.fitness_sum)
        children_list = []
        parents_list = []
        for number in range(int(passing_size/2)):
            kid1, kid2, kid3, kid4 = self.individuals[sorted_fitness[number*2]].crossover(self.individuals[sorted_fitness[number*2+1]])
            children_list = children_list + [kid1, kid2, kid3, kid4]
            parents_list = parents_list + [self.individuals[sorted_fitness[number*2]], self.individuals[sorted_fitness[number*2+1]]]

        #self.individuals = parents_list+children_list+self.individuals[passing_size:passing_size+10]
        self.individuals = parents_list[0:passing_size] + children_list
        self.population_size = np.size(self.individuals)
        self.fitness = np.zeros(self.population_size)
        self.fitness_individual()
