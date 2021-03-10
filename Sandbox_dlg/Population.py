# Class implementation of population
# Original image will be necessary for individual polygon evaluation, at least in this idea.
# Using colors and checking how well created polygon align with corresponding fragments on original image we can see how
# good it's genes are.

import numpy as np
from Evo_object import Polygon
from numpy import asarray
from PIL import Image
import matplotlib.pyplot as plt
import numexpr as ne
import copy


class ImageClass:
    def __init__(self, im_path: str, max_poly_edges: int = 4, population_size: int = 60):
        self.original_image = asarray(Image.open(im_path))
        self.canvas_size = (self.original_image.shape[1], self.original_image.shape[0])
        self.max_edges = max_poly_edges
        self.created_image = None
        self.population_size = population_size
        self.individuals = [Polygon(self.max_edges, self.canvas_size) for i in range(self.population_size)]
        self.chromosome = []
        self.fitness = None

        self.get_poly_image()
        self.fitness_all()

    def get_poly_image(self):
        back = Image.new("RGBA", self.canvas_size[0:2], (0, 0, 0, 0))
        object_index = 0
        for individual in self.individuals:
            self.chromosome.append(individual.poly_gene)
            self.chromosome.append(individual.poly_gene)
            back.paste(individual.poly_image, mask=individual.poly_image)
            object_index = object_index + 1

        self.created_image = np.asarray(back)[..., :3]

    def print_poly_image(self):
        self.get_poly_image()
        plt.imshow(self.created_image)
        plt.show()

    def fitness_all(self):
        a0 = self.original_image[..., 0]
        a1 = self.original_image[..., 1]
        a2 = self.original_image[..., 2]
        b0 = self.created_image[..., 0]
        b1 = self.created_image[..., 1]
        b2 = self.created_image[..., 2]
        self.fitness = float(ne.evaluate('sum((a0/255-b0/255)**2 + (a1/255-b1/255)**2 + (a2/255-b2/255)**2)'))

    def mutate(self):
        pass

    def crossover(self, mate):
        pass