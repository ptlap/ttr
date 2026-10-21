import itertools
import re



def parse_and_eval(expr, var_dict):
  expr = expr.replace("<->", " == ").replace("->", " <= ")
  expr = expr.replace("^", " != ")
  expr = expr.replace("&", " and ").replace("|", " or ").replace("~", " not ")

  for var, val in var_dict.items():
     expr = re.sub(rf"\b{var}\b", str(val), expr)

  return bool(eval(expr))



def print_truth_table(expression_str):
  found_vars = re.findall(r"\b[a-zA-Z]\b", expression_str)
  variables = sorted(list(set(found_vars)))

  if not variables:
     print("No valid variables found.")
     return

  # Convert all headers and widths explicitly to string/int
  headers = [str(v) for v in variables] + [str(expression_str)]
  col_widths = [max(len(str(var)), 5) for var in variables] + [
    max(len(str(expression_str)), 10)
  ]

  header_row = " | ".join(
    f"{str(h):^{int(w)}}" for h, w in zip(headers, col_widths)
  )
  separator = "-+-".join("-" * int(w) for w in col_widths)

  print("\n" + "=" * len(header_row))
  print(header_row)
  print(separator)

  combinations = itertools.product([False, True], repeat=len(variables))

  for values in combinations:
     var_dict = dict(zip(variables, values))

     try:
        result = parse_and_eval(expression_str, var_dict)
        res_str = "TRUE" if result else "FALSE"
     except Exception as e:
        print(f"Error: {e}")
        return

     row_vals = ["TRUE" if v else "FALSE" for v in values] + [res_str]
     row_str = " | ".join(
        f"{str(val):^{int(w)}}" for val, w in zip(row_vals, col_widths)
     )
     print(row_str)

  print("=" * len(header_row) + "\n")



if __name__ == "__main__":
   user_expr = input("Enter logic expression: ")
   print_truth_table(user_expr)
