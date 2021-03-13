# Class defining 2D object which is going to be manipulated by genetics algorithm.
from __future__ import annotations
# IMPORT
import numpy as np
import random
from PIL import Image
from PIL import ImageDraw
import matplotlib.pyplot as plt

random.seed(668554456)
# poly_gene is a variable which purpose it to represent DNA of our object, specified in form of a list and containing:
# [no. polynomial edges(e = 1,..n) , Red color, Green color, Blue color, // using RGB color model
# (X coordinate of vertex with index i = 1, Y coordinate of vertex with index i = 1), ...,
# (X coordinate of vertex with index i = n, Y coordinate of vertex with index i = n]).
# Could be changed to separated lists later.
# Maximum number of edges is to be specified later.


class Polygon:
    def __init__(self, max_edges: int, canvas_size: tuple, poly_gene=None):
        self.canvas_size = canvas_size
        self.poly_image = None
        if poly_gene is not None:
            self.poly_gene = poly_gene
        else:
            no_edges = random.randint(3, max_edges)
            self.poly_gene = [None] * 4
            self.poly_gene[0:4] = [no_edges] + random.sample(range(1, 255), 3)
            for num in range(no_edges):
                coord_xy = (random.randint(0, canvas_size[0]), random.randint(0, canvas_size[1]))
                self.poly_gene = self.poly_gene + [coord_xy]
        self.make_figure()

    def make_figure(self):
        poly = Image.new('RGBA', self.canvas_size, (0, 0, 0, 0))
        pdraw = ImageDraw.Draw(poly)
        pdraw.polygon(self.poly_gene[4:],
                      fill=(self.poly_gene[1], self.poly_gene[2], self.poly_gene[3], 127))
        self.poly_image = poly

    def mutate(self):   # Implementing 3 types of possible mutation in individual.
        # The object can mutate either it's color or it's vertexes placement. The dice will decide.
        mutation_type = random.uniform(0, 1)
        if mutation_type < 0.33:
            #self.poly_gene[1:4] = random.sample(range(1, 255), 3)
            self.poly_gene[random.randint(1, 3)] = random.randint(1, 255)
        elif 0.33 <= mutation_type < 0.66:
            coord_xy = (random.randint(0, self.canvas_size[0]), random.randint(0, self.canvas_size[1]))
            self.poly_gene[4 + random.randint(0, self.poly_gene[0]-1)] = (coord_xy)
            # ran_in = random.randint(0, self.poly_gene[0] - 1)
            # self.poly_gene[4 + ran_in] = (random.randint(0, self.canvas_size[0]),
            #                               (self.poly_gene[4 + ran_in])[1])
        else:
            for num in range(self.poly_gene[0]):
                coord_xy = (random.randint(0, self.canvas_size[0]), random.randint(0, self.canvas_size[1]))
                self.poly_gene[4+num] = (coord_xy)
        self.make_figure()

    def mutate_edge(self):
        ran_in = random.randint(0, self.poly_gene[0] - 1)
        self.poly_gene[4 + ran_in] = (random.randint(0, self.canvas_size[0]),
                                      (self.poly_gene[4 + ran_in])[1])
        self.make_figure()

    def mutate_color(self):
        self.poly_gene[1:4] = random.sample(range(1, 255), 3)

    def change_gene(self, new_gene):
        self.poly_gene = new_gene
        self.make_figure()