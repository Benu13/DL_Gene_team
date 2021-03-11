# Population class of images
from numpy import asarray
from PIL import Image
import numexpr as ne
from New.Evo_object_new import ImageClass
import numpy as np


class Population:
    def __init__(self, im_path: str, max_poly_edges: int = 4, population_size: int = 40, polygon_number: int = 50):
        self.original_image = asarray(Image.open(im_path))
        self.canvas_size = (self.original_image.shape[1], self.original_image.shape[0])
        self.population_size = population_size
        self.fitness_array = []
        self.fitness_best = None
        self.objects = [ImageClass(self.canvas_size, max_poly_edges, polygon_number) for i in range(population_size)]
        self.fitness_all()

    def fitness_all(self):
        self.fitness_array = []
        for image in self.objects:
            a0 = self.original_image[..., 0]
            a1 = self.original_image[..., 1]
            a2 = self.original_image[..., 2]
            b0 = image.created_image[..., 0]
            b1 = image.created_image[..., 1]
            b2 = image.created_image[..., 2]
            self.fitness_array.append(float(ne.evaluate('sum((a0/255-b0/255)**2 '
                                                        '+ (a1/255-b1/255)**2 + (a2/255-b2/255)**2)')))
        self.fitness_best = min(self.fitness_array)

    def do_the_evolution(self, tournament_size: int = 4):
        parents_list = []
        kids_list = []
        tournaments_number = int(self.population_size/tournament_size)
        last_tournament = self.population_size % 4
        for i in range(tournaments_number):
            fight_fitness = self.fitness_array[i*tournament_size:i*tournament_size+tournament_size]
            best_two = np.argsort(fight_fitness)
            a = best_two[0]+tournament_size*i
            b = best_two[1]+tournament_size*i
            parents_list.append(self.objects[best_two[0]+tournament_size*i])
            parents_list.append(self.objects[best_two[1]+tournament_size*i])
            kid1, kid2 = self.objects[best_two[0]].crossover(self.objects[best_two[1]])
            kids_list.append(kid1)
            kids_list.append(kid2)
        self.objects = parents_list + kids_list
        self.fitness_all()

    def print_best_image(self):
        one = np.argsort(self.fitness_array)
        self.objects[one[0]].print_poly_image()
