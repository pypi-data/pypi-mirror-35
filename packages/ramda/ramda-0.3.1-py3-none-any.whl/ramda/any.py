from ramda.curry import curry


@curry
def any(p, xs):
    for x in xs:
        if p(x):
            return True
    return False
