import math
def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    """

    return math.ceil(n/50)


def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """
    suma_neg = 0
    suma_pos = 0

    for i in price_changes:
        if i >=0:
            suma_pos += i
        else:
            suma_neg+= i
    return (suma_pos,suma_neg)


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """
    m = -k
    for i in range(len(L[:k])):
        L[i],L[m] = L[m], L[i]
        m = m +1

    return L




if __name__ == '__main__':
    import doctest
    doctest.testmod()