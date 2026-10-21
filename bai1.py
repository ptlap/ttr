"""Bài 1: Lập bảng giá trị chân lý của công thức mệnh đề."""
import itertools
import re

PRIORITY = {"<->": 1, "->": 2, "|": 3, "^": 4, "&": 5}


def tokenize(expression):
    tokens = []
    position = 0
    while position < len(expression):
        if expression[position].isspace():
            position += 1
            continue
        match = re.match(r"<->|->|[A-Za-z]|[~&|^()]", expression[position:])
        if match is None:
            raise ValueError(f"Ký tự không hợp lệ tại vị trí {position + 1}.")
        tokens.append(match.group())
        position += len(match.group())
    return tokens


def parse_expression(tokens):
    """Phân tích công thức theo thứ tự ưu tiên, không dùng eval()."""
    position = 0

    def parse_operand():
        nonlocal position
        if position >= len(tokens):
            raise ValueError("Công thức thiếu toán hạng.")
        token = tokens[position]
        position += 1
        if token == "~":
            return ("~", parse_operand())
        if token == "(":
            node = parse_binary(1)
            if position >= len(tokens) or tokens[position] != ")":
                raise ValueError("Thiếu dấu đóng ngoặc ')'.")
            position += 1
            return node
        if re.fullmatch(r"[A-Za-z]", token):
            return token
        raise ValueError(f"Không thể đặt '{token}' ở vị trí này.")

    def parse_binary(min_priority):
        nonlocal position
        left = parse_operand()
        while position < len(tokens):
            operator = tokens[position]
            priority = PRIORITY.get(operator, 0)
            if priority < min_priority:
                break
            position += 1
            # Kéo theo kết hợp phải: p -> q -> r = p -> (q -> r).
            next_priority = priority if operator == "->" else priority + 1
            right = parse_binary(next_priority)
            left = (operator, left, right)
        return left

    tree = parse_binary(1)
    if position != len(tokens):
        raise ValueError(f"Thừa hoặc đặt sai ký hiệu '{tokens[position]}'.")
    return tree


def evaluate(tree, values):
    if isinstance(tree, str):
        return values[tree]
    operator = tree[0]
    left = evaluate(tree[1], values)
    if operator == "~":
        return not left
    right = evaluate(tree[2], values)
    if operator == "&":
        return left and right
    if operator == "|":
        return left or right
    if operator == "^":
        return left != right
    if operator == "->":
        return (not left) or right
    return left == right


def print_truth_table(expression):
    tokens = tokenize(expression)
    tree = parse_expression(tokens)
    variables = sorted({t for t in tokens if re.fullmatch(r"[A-Za-z]", t)})
    headers = variables + [expression]
    widths = [max(5, len(header)) for header in headers]

    def print_row(items):
        print(" | ".join(str(item).center(width)
                         for item, width in zip(items, widths)))

    print_row(headers)
    print("-+-".join("-" * width for width in widths))
    for combination in itertools.product([False, True], repeat=len(variables)):
        values = dict(zip(variables, combination))
        result = evaluate(tree, values)
        print_row(["TRUE" if v else "FALSE" for v in (*combination, result)])


if __name__ == "__main__":
    print("BÀI 1: BẢNG GIÁ TRỊ CHÂN LÝ")
    print("Ký hiệu: ~  &  |  ^  ->  <->")
    print("Mỗi biến là một chữ cái, ví dụ: p, q, r.")
    expression = input("Nhập công thức: ").strip()
    try:
        print_truth_table(expression)
    except ValueError as error:
        print("Lỗi:", error)
