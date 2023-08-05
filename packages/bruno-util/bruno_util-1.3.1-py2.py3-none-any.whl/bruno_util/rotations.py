"""Utilities for dealing with rotations, in 3D by default."""
import pandas as pd
import numpy as np


def random_rotation_matrix(shape=(1,)):
    """Fill an array of size shape with uniformly randomly distribution 3D
    rotation matrices, to get a final output of size (shape + (3,3)). Use James
    Arvo's fast method of generating a rotation about the z axis, then "moving
    the north pole" to a random point on the sphere through two conveniently
    fast (householder) reflections to uniformly sample SO(3)."""
    pass

def random_versor(shape=(1,)):
    """Use the 4 normal random numbers, normalized, to get a uniformly randomly
    distributed versor, isomorphic to an element of SO(3)."""
    pass

def versor_to_matrix(v):
    pass

def matrix_to_versor(m):
    pass
