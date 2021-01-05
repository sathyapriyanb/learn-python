class Puppy:
    n_puppies = 0  # number of created puppies

    # define __new__
    def __new__(cls):
        if cls.n_puppies <= 9:
            cls.n_puppies += 1



