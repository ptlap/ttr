"""Bài 2: Biểu diễn tập hợp bằng xâu bit theo thứ tự của U."""
import random

U_BASE = list('abcdefghlmopqrst')


def get_bitstring(u_seq, target_set):
    return ''.join('1' if element in target_set else '0' for element in u_seq)


def set_operations(u_seq, a_set, b_set):
    universal = set(u_seq)
    if len(universal) != len(u_seq):
        raise ValueError('Các phần tử của U phải khác nhau.')
    invalid = (a_set | b_set) - universal
    if invalid:
        raise ValueError('Phần tử không thuộc U: ' + ', '.join(sorted(invalid)))
    return {
        'A': a_set,
        'B': b_set,
        'Bù A (U \\ A)': universal - a_set,
        'Bù B (U \\ B)': universal - b_set,
        'Hợp A ∪ B': a_set | b_set,
        'Giao A ∩ B': a_set & b_set,
        'Hiệu A \\ B': a_set - b_set,
        'Hiệu B \\ A': b_set - a_set,
        'Hiệu đối xứng A △ B': a_set ^ b_set,
    }


def run_example(u_seq, a_set, b_set):
    results = set_operations(u_seq, a_set, b_set)
    print('\nThứ tự U:', ' '.join(u_seq))
    for name, elements in results.items():
        ordered = [element for element in u_seq if element in elements]
        print(f'\n{name}: ' + '{' + ', '.join(ordered) + '}')
        print('Xâu bit:', get_bitstring(u_seq, elements))
        print('Số phần tử:', len(elements))


if __name__ == '__main__':
    print('BÀI 2: BIỂU DIỄN TẬP HỢP')
    print('U ban đầu:', ' '.join(U_BASE))
    u_seq = U_BASE.copy()
    random.shuffle(u_seq)
    print('U sau hoán vị:', ' '.join(u_seq))
    print('Nhập các phần tử cách nhau bằng khoảng trắng; Enter cho tập rỗng.')
    a_set = set(input('Nhập A: ').split())
    b_set = set(input('Nhập B: ').split())
    try:
        run_example(u_seq, a_set, b_set)
    except ValueError as error:
        print('Lỗi:', error)
