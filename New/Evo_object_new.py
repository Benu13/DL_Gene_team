# Still in testing, now instead of single polygon a whole created image is taken as an object.
# Then: Polygon -> Population -> Image
# Now: Polygon -> Image -> Population

from __future__ import annotations
import numpy as np
from New.PolyClass import Polygon
from PIL import Image
import matplotlib.pyplot as plt
import random
from copy import deepcopy

class ImageClass:
    def __init__(self, canvas_size: tuple, max_poly_edges: int = 4, polygon_number: int = 50, chromosome=None):
        self.canvas_size = canvas_size
        self.max_edges = max_poly_edges
        self.created_image = None
        self.polygon_number = polygon_number
        if chromosome is not None:
            self.chromosome = chromosome
        else:
            self.chromosome = [Polygon(self.max_edges, self.canvas_size) for i in range(self.polygon_number)]
        self.get_poly_image()

    def get_poly_image(self):
        back = Image.new("RGBA", self.canvas_size[0:2], (0, 0, 0, 0))
        object_index = 0
        for individual in self.chromosome:
            back.paste(individual.poly_image, mask=individual.poly_image)
            object_index = object_index + 1

        self.created_image = np.asarray(back)[..., :3]

    def change_material(self, chromosome):
        i = 0
        for polygon in self.chromosome:
            polygon.change_gene(chromosome[i].poly_gene)
            i = i + 1
        self.mutate()

    def print_poly_image(self):
        self.get_poly_image()
        plt.imshow(self.created_image)
        plt.show()

    def mutate(self):
        for gene in self.chromosome:
            raa = 1 #random.uniform(0, 1)
            if raa >= 0:
                gene.mutate()
        self.get_poly_image()

