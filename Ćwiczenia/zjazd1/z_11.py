
def mean_std(*args):
    n = len(args)

    if n == 0:
        return None, None

    X = sum(args) / n
    var = sum((x - X) ** 2 for x in args) / n

    sigma = var ** 0.5

    return X, sigma


print(mean_std(4, 4, 4, 5, 5, 5))
