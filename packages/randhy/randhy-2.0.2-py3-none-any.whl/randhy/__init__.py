import random

__author__ = 'Sasho Savkov'
__credits__ = ["Sasho Savkov", "William Morgan"]
__license__ = "MIT"
__version__ = "2.0.0"
__email__ = "me@sasho.io"
__status__ = "Production"


def resample(a, b):
    """
    Pools two lists together and randomly splits them back into two.

    Example:
        [a, b, c] & [1, 2, 3] -> [b, 3, 2] & [c, 1, a]

    :param a: first list
    :param b: second list
    :return: pair of randomly mixed lists
    """
    pool = a + b
    random.shuffle(pool)
    X, Y = pool[:int(len(pool)/2)], pool[int(len(pool)/2):]
    return X, Y


def random_test(o_a, o_b, gold, t, reps=1000, smoothing=False):
    """
    Calculates simple approximate randomisation test.

    :param o_a: first predicted label vector
    :param o_b: second predicted label vector
    :param gold: true (gold) label vector
    :param t: test metric
    :param reps: number of iterations
    :param smoothing: do Laplace smoothing
    :return: proportion of iteration that supported the hypothesis
    """
    r = 0
    t_value = t(o_a, o_b, gold)
    for _ in range(reps):
        X, Y = resample(o_a, o_b)
        t_rand = t(X, Y, gold)
        r += int(t_rand >= t_value)
    smoothing = float(smoothing)
    return (r + smoothing) / (reps + smoothing)


def random_swap(o_a, o_b):
    """
    Randomly swap elements of two observation vectors and return new vectors.

    :param o_a: observation vector a
    :param o_b: observation vector b
    :return: shuffled vectors
    """
    X, Y = [], []
    tf = [True, False]
    for x, y in zip(o_a, o_b):
        if random.choice(tf):
            x, y = y, x
        X.append(x)
        Y.append(y)
    return X, Y


def paired_randomisation_test(o_a, o_b, gold, t, reps=1000, smoothing=False):
    """
    Calculates significance value using paired approximate randomisation.

    Note that `reps` is indicated by `R` in some notations

    An example test statistic (`t`):
            ```
            def f1_t(o_a, o_b, gold, f1_func):
                return abs(f1_func(o_a, gold) - f1_func(o_b, gold))
            ```

    :param o_a: first predicted label vector
    :param o_b: second predicted label vector
    :param gold: true (gold) label vector
    :param t: test metric
    :param reps: number of iterations
    :param smoothing: do Laplace smoothing
    :return: proportion of iteration that supported the hypothesis
    """
    r = 0
    t_score = t(o_a, o_b, gold)
    for i in range(reps):
        sha, shb = random_swap(o_a, o_b)
        if t(sha, shb, gold) >= t_score:
            r += 1
    smoothing = float(smoothing)
    return (r + smoothing) / (reps + smoothing)
