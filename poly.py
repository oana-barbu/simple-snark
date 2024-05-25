from scipy.interpolate import lagrange
from numpy import poly1d, polydiv


def vanishing(values: list[int]) -> poly1d:
    vanish = poly1d([1])
    for x in values:
        vanish *= poly1d([1, -x])
    return vanish


def to_latex(poly: poly1d, skip_zeros=True) -> str:
    d = len(poly) - 1
    s = ''
    for i, c in enumerate(poly):
        if c == 0 and skip_zeros:
            continue
        front = '+ ' if c >= 0 and s else ''
        if c.is_integer():
            s += front + fr'{int(c)}x^{d-i}'
        else:
            num, denom = c.as_integer_ratio()
            s += front + fr'\frac{{{num}}}{{{denom}}}x^{d-i}'
    return s


def main():
    indices = [1, 2, 3]
    ua = lagrange(indices, [0, 0, 1])
    va = lagrange(indices, [0, -1, 0])
    wa = ua * va

    vanish = vanishing(indices)
    print(f'wa: {wa}')
    print(f'vanish: {vanish}')

    hx = wa / vanish
    print(f'hx: {hx}')

    v2 = lagrange(indices, [1, 0, 1])
    print(f'v2: {v2}')


if __name__ == '__main__':
    main()
