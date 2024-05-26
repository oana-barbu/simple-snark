from scipy.interpolate import lagrange
from numpy import poly1d, polydiv, array


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


def from_poly(p: poly1d, d: int) -> list[int]:
    v = [0] * d
    for i, c in enumerate(p):
        v[i + d - len(p) - 1] = c
    return v


def main():
    indices = [1, 2, 3]
    d = len(indices)

    # a0 * a1 = 0
    # a0 * (a0 - 1) = 0
    # a1 * (a1 - 1) = 0

    left = array([
        [1, 0, 0, ],
        [1, 0, 0, ],
        [0, 1, 0, ]
    ])
    right = array([
        [0, 1,  0, ],
        [1, 0, -1, ],
        [0, 1, -1, ]
    ])

    u = array([
        from_poly(lagrange(indices, left[:, 0]), d),
        from_poly(lagrange(indices, left[:, 1]), d),
        from_poly(lagrange(indices, left[:, 2]), d),
    ]).T
    print(f'u:\n{u}')
    v = array([
        from_poly(lagrange(indices, right[:, 0]), d),
        from_poly(lagrange(indices, right[:, 1]), d),
        from_poly(lagrange(indices, right[:, 2]), d),
    ]).T
    print(f'v:\n{v}\n')

    a = array([0, 1, 1])

    ua = u * a
    print(f'ua:\n{ua}')
    va = v * a
    print(f'va:\n{va}')

    Ua = poly1d(ua.sum(axis=1))
    Va = poly1d(va.sum(axis=1))
    print(f'Ua:\n{Ua}')
    print(f'Va:\n{Va}')

    Wa = Ua * Va

    print(f'Ua*Va:\n{Wa}')
    tau = Wa(33)
    print([Wa(1), Wa(2), Wa(3), Wa(tau), Ua(tau) * Va(tau)])

    tx = poly1d(indices, True)
    print(f't(x):\n{tx}')
    hx, rem = polydiv(Ua * Va, tx)
    assert rem == poly1d([0])
    print(f'h(x):\n{hx}')


if __name__ == '__main__':
    main()
