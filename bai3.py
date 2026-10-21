"""Bài 3: Giải hệ thức truy hồi tuyến tính thuần nhất hệ số hằng."""
import sympy as sp

N = sp.Symbol('n', integer=True, nonnegative=True)
R = sp.Symbol('r')


def exact_numbers(items):
    """Đọc số nguyên, phân số, số thập phân thành số hữu tỷ chính xác."""
    try:
        return [sp.Rational(str(item)) for item in items]
    except (ValueError, TypeError, ZeroDivisionError) as error:
        raise ValueError('Chỉ nhập số hữu tỷ, ví dụ: 2, -3, 1/2, 0.25.') from error


def solve_recurrence(coeff_list, init_list):
    coeffs = exact_numbers(coeff_list)
    initials = exact_numbers(init_list)
    order = len(coeffs)
    if not order or len(initials) != order:
        raise ValueError('Cần k hệ số và đúng k giá trị đầu a0, ..., a(k-1).')

    polynomial = sp.Poly(
        R**order - sum(c * R**(order-i-1) for i, c in enumerate(coeffs)), R
    )
    roots = sp.roots(polynomial.as_expr(), R)
    if sum(roots.values()) != order:
        # all_roots bao gồm cả nghiệm đại số không biểu diễn được bằng căn thức.
        roots = dict(polynomial.all_roots(multiple=False))

    basis = []
    processed = set()
    for root, multiplicity in roots.items():
        if root in processed:
            continue
        if root == 0:
            # n^j * 0^n không tạo đủ nghiệm khi 0 là nghiệm bội.
            basis.extend(sp.KroneckerDelta(N, j) for j in range(multiplicity))
        elif root.is_real is True:
            basis.extend(N**j * root**N for j in range(multiplicity))
        else:
            conjugate = sp.conjugate(root)
            if conjugate in roots and conjugate != root:
                radius = sp.Abs(root)
                angle = sp.arg(root)
                for j in range(multiplicity):
                    basis.extend([
                        N**j * radius**N * sp.cos(N * angle),
                        N**j * radius**N * sp.sin(N * angle),
                    ])
                processed.add(conjugate)
            else:
                basis.extend(N**j * root**N for j in range(multiplicity))
        processed.add(root)

    constants = sp.symbols(f'C1:{order+1}')
    general = sum(c * term for c, term in zip(constants, basis))
    matrix = sp.Matrix([
        [sp.simplify(term.subs(N, i)) for term in basis]
        for i in range(order)
    ])
    values = matrix.inv() * sp.Matrix(initials)
    solution = sp.simplify(sum(c * term for c, term in zip(values, basis)))
    return polynomial.as_expr(), roots, general, dict(zip(constants, values)), solution


def main():
    print('BÀI 3: GIẢI HỆ THỨC TRUY HỒI')
    print('Dạng: a_n = c1*a_(n-1) + ... + ck*a_(n-k), n >= k.')
    print('Nhập số nguyên, phân số hoặc thập phân, cách nhau bằng khoảng trắng.')
    coeffs = input('Nhập c1 ... ck (ví dụ: 1 1): ').split()
    initials = input('Nhập a0 ... a(k-1) (ví dụ: 0 1): ').split()
    try:
        polynomial, roots, general, constants, solution = solve_recurrence(coeffs, initials)
        print('\nPhương trình đặc trưng:', polynomial, '= 0')
        for root, multiplicity in roots.items():
            print(f'Nghiệm r = {root}, bội {multiplicity}')
        print('\nNghiệm tổng quát: a_n =', general)
        print('Các hằng số:', constants)
        print('Nghiệm theo điều kiện đầu: a_n =', solution)
        print('Áp dụng với n nguyên không âm. KroneckerDelta(n, j) bằng 1 khi n = j, ngược lại bằng 0.')
        print('10 số hạng đầu:', [sp.simplify(solution.subs(N, i)) for i in range(10)])
    except (ValueError, sp.matrices.exceptions.NonInvertibleMatrixError) as error:
        print('Lỗi:', error)


if __name__ == '__main__':
    main()
