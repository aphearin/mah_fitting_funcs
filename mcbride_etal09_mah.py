"""
"""
import numpy as np


def mah(z, beta, gamma):
    assert gamma >= 0, "gamma must be non-negative"
    return np.exp(-gamma*z)*(1 + z)**beta


def average_beta(halo_type):
    if str(halo_type) == 'overall':
        return 0.1
    elif halo_type == 1:
        return 0.
    elif halo_type == 2:
        return -0.9
    elif halo_type == 3:
        return 0.64
    elif halo_type == 4:
        return 1.4


def average_beta_minus_gamma(mass, halo_type):
    """
    """
    x = np.log10(mass/1e12)
    if str(halo_type) == 'overall':
        return -0.25*x - 0.29
    elif halo_type == 1:
        return -0.22*x - 0.45
    elif halo_type == 2:
        return -0.12*x - 1.15
    elif halo_type == 3:
        return -0.03*x - 0.20
    elif halo_type == 4:
        return 0.03*x + 0.15


def average_beta_gamma(mass, halo_type):
    beta = average_beta(halo_type)
    gamma = max(beta - average_beta_minus_gamma(mass, halo_type), 0.1)
    return beta, gamma
