def recursive_sumrange(start, stop):
    '''Recursively adds all integers between, and including, start and stop'''
    # Make sure start <= stop
    if start > stop:
        temp = start
        start = stop
        stop = temp

    if start == stop:
        return start
    return start + recursive_sumrange(start + 1, stop)
