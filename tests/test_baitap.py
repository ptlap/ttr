import itertools
import unittest
import sympy as sp
from bai1 import tokenize, parse_expression, evaluate
from bai2 import get_bitstring, set_operations
from bai3 import N, solve_recurrence


class TruthTableTests(unittest.TestCase):
    def test_operators(self):
        operations = {'&': lambda a,b:a and b, '|':lambda a,b:a or b,
                      '^':lambda a,b:a != b, '->':lambda a,b:(not a) or b,
                      '<->':lambda a,b:a == b}
        for operator, expected in operations.items():
            tree = parse_expression(tokenize('p ' + operator + ' q'))
            for p,q in itertools.product([False, True], repeat=2):
                self.assertEqual(evaluate(tree, {'p':p, 'q':q}), expected(p,q))

    def test_contraposition(self):
        tree = parse_expression(tokenize('(p -> q) <-> (~q -> ~p)'))
        for p,q in itertools.product([False, True], repeat=2):
            self.assertTrue(evaluate(tree, {'p':p,'q':q}))

    def test_precedence_and_associativity(self):
        values = {'p':False, 'q':True, 'r':False}
        self.assertTrue(evaluate(parse_expression(tokenize('p -> q -> r')), values))
        values = {'p':True, 'q':False, 'r':False}
        self.assertTrue(evaluate(parse_expression(tokenize('p | q & r')), values))

    def test_invalid_input(self):
        for text in ['', 'p q', '(p', 'p)', 'p &', '__import__(p)', 'p && q']:
            with self.subTest(text=text), self.assertRaises(ValueError):
                parse_expression(tokenize(text))


class SetTests(unittest.TestCase):
    def test_operations_and_bits(self):
        u = list('dcba')
        results = list(set_operations(u, set('ac'), set('bc')).values())
        expected = ['0101', '0110', '1010', '1001', '0111', '0100', '0001', '0010', '0011']
        self.assertEqual([get_bitstring(u, result) for result in results], expected)
        self.assertEqual(get_bitstring(u, set()), '0000')
        self.assertEqual(get_bitstring(u, set(u)), '1111')

    def test_invalid_elements(self):
        with self.assertRaises(ValueError):
            set_operations(list('abc'), set('z'), set())


class RecurrenceTests(unittest.TestCase):
    def test_formula_matches_iteration(self):
        cases = [([1,1],[0,1]), ([4,-4],[1,4]), ([0,-1],[1,0]),
                 ([0,0],[2,3]), ([2,0],[3,5]), (['1/2'],[2]),
                 ([11,-7,-147],[384,-64,-963]),
                 ([0,-2,0,-1],[1,2,3,4])]
        for coeffs, initials in cases:
            with self.subTest(coeffs=coeffs):
                solution = solve_recurrence(coeffs, initials)[-1]
                expected = list(map(sp.Rational, initials))
                coefficients = list(map(sp.Rational, coeffs))
                for i in range(len(coeffs), 12):
                    expected.append(sum(c * expected[i-j-1]
                                        for j,c in enumerate(coefficients)))
                for i, value in enumerate(expected):
                    self.assertEqual(sp.simplify(solution.subs(N, i) - value), 0)

    def test_invalid_input(self):
        for coeffs, initials in [([],[]), ([1,1],[0]), (['bad'],[1]), (['1/0'],[1])]:
            with self.assertRaises(ValueError):
                solve_recurrence(coeffs, initials)


if __name__ == '__main__':
    unittest.main()
