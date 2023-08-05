# -*- coding: utf-8 -*-

"""Main module."""
class Beamformer:
    def __init__(self, structure = 'Linear', number_of_antennas = 8, antenna_space = 0.5):
        self.structure = structure
        self.number_of_antennas = number_of_antennas
        self.antenna_space = antenna_space

    def get_array_response(self, angle = 0, weight = 0, format = 'Radian'):
        return 0

    def common_weight(self, constraints):
        return 0
