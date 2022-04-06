from typing import Iterator
from matplotlib import pyplot as plt


def linear_congruential_generator(m: int, a: int, c: int, seed: int) -> Iterator[int]:
    """
    This generator implements the Linear Congruential Generator algorithm
    :param m: the modulus, a positive integer constant
    :param a: the multiplier, a non-negative integer constant < m
    :param c: the increment, a non-negative integer constant < m
    :param seed: the starting state of the LCG. It is used to initialize the pseudo-random number sequence
    :return: a non-negative integer in [0, m-1] representing the n-th state of the generator
    """
    x = seed
    while True:
        yield x
        x = (a * x + c) % m


def rand_float_samples(n_samples: int, seed: int = 123_456_789) -> list[float]:
    """
    This function uses an LCG to output float pseudo-random numbers from the uniform distribution on [lower, upper)
    :param n_samples: the number of pseudo-random floats to generate
    :param seed: The starting state of the LCG. It is used to initialize the pseudo-random number sequence
    :return: a list of len n_samples with the pseudo-random numbers generated
    """
    m: int = 2_147_483_648
    a: int = 594_156_893
    c: int = 0
    gen = linear_congruential_generator(m, a, c, seed)
    sequence = []

    for i in range(0, n_samples):
        rand: float = next(gen) / m
        sequence.append(rand)

    return sequence


if __name__ == "__main__":
    n = 1000
    rand_sequence = rand_float_samples(n)

    plt.scatter(rand_sequence, range(0, n))
    plt.show()
     
