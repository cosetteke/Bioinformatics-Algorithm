# https://dodona.ugent.be/nl/courses/359/series/3492/activities/463104583
def color(genotype):
    """
    >>> color('CcDd')
    'seal'
    >>> color('ccdd')
    'lilac'
    """
    if 'C' in genotype:
        return 'seal' if 'D' in genotype else 'blue'

    return 'chocolate' if 'D' in genotype else 'lilac'

def combinations(genotype):
    """
    >>> combinations('CcDd')
    ['CD', 'Cd', 'cD', 'cd']
    >>> combinations('ccdd')
    ['cd', 'cd', 'cd', 'cd']
    """
    return [c + d for c in genotype[:2] for d in genotype[2:]]

def punnett(m, f, pprint = False):
    """
    >>> punnett('CcDd', 'CcDd')
    [['CCDD', 'CCDd', 'CcDD', 'CcDd'], ['CCdD', 'CCdd', 'CcdD', 'Ccdd'], ['cCDD', 'cCDd', 'ccDD', 'ccDd'], ['cCdD', 'cCdd', 'ccdD', 'ccdd']]
    >>> print(punnett('CcDd', 'CcDd', pprint=True))
    CCDD CCDd CcDD CcDd
    CCdD CCdd CcdD Ccdd
    cCDD cCDd ccDD ccDd
    cCdD cCdd ccdD ccdd
    >>> print(punnett('cCDd', 'CcdD', pprint=True))
    cCDd cCDD ccDd ccDD
    cCdd cCdD ccdd ccdD
    CCDd CCDD CcDd CcDD
    CCdd CCdD Ccdd CcdD
    """
    m, f = combinations(m), combinations(f)
    result = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(m[i][0] + f[j][0] + m[i][1] + f[j][1])
        result.append(row)
    return '\n'.join(' '.join(row) for row in result) if pprint else result

def color_distribution(m,f):
    distrubution = {}
    result = punnett(m,f)
    for row in result:
        for item in row:
            phenotype = color(item)
            distrubution[phenotype] = distrubution.get(phenotype, 0) + 1
    return distrubution


if __name__ == '__main__':
    import doctest
    doctest.testmod()
