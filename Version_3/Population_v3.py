# Population class of images
from numpy import asarray
from PIL import Image
import numexpr as ne
from Version_3.Evo_object_v3 import ImageClass
import numpy as np
import random
import copy
random.seed(668554456)


class Population:
    def __init__(self, im_path: str, max_poly_edges: int = 4, polygon_number: int = 50):
        self.original_image = asarray(Image.open(im_path))
        self.canvas_size = (self.original_image.shape[1], self.original_image.shape[0])
        self.population_size = 2
        self.polygon_number = polygon_number
        self.fitness_array = []
        self.fitness_best = None
        self.objects = [ImageClass(self.canvas_size, max_poly_edges, polygon_number) for i in range(2)]
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

    def crossover(self, winner: ImageClass, looser: ImageClass):
        looser.change_material(winner.chromosome)

    def do_the_evolution(self):
        if self.fitness_array[0] < self.fitness_array[1]:
            self.crossover(winner=self.objects[0], looser=self.objects[1])
        else:
            self.crossover(self.objects[1], self.objects[0])
        self.fitness_all()

    def print_best_image(self):
        one = np.argsort(self.fitness_array)
        self.objects[one[0]].print_poly_image()

    def get_best_image(self):
        one = np.argsort(self.fitness_array)
        return self.objects[one[0]].created_image
