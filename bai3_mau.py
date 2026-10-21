import math
import sympy as sp



def simplify_angle(rad_val: float) -> str:
  frac = sp.Rational(rad_val / math.pi).limit_denominator(12)
  if frac == 0:
     return "0"
  num, den = frac.p, frac.q
  if den == 1:
     if num == 1:
        return "pi"
     if num == -1:
        return "-pi"
     return f"{num}*pi"

  if num == 1:
     return f"pi/{den}"
  if num == -1:
     return f"-pi/{den}"
  return f"{num}*pi/{den}"



def solve_recurrence(coeff_list: list, init_list: list) -> None:
  k_order = len(coeff_list)
  if len(init_list) != k_order:
      print(
         "\nError: Number of initial conditions must equal "
         "the order of recurrence relation!"
      )
      return
  # Chuyển đổi toàn bộ dữ liệu nhập vào thành số hữu tỷ chính xác trong SymPy
  exact_coeffs = [sp.sympify(c) for c in coeff_list]
  exact_inits = [sp.sympify(i) for i in init_list]

  print("\n" + "=" * 65)
  print("1. INITIAL RECURRENCE RELATION:")
  rec_terms = [
     f"{c}*a_{{n-{i+1}}}" if c >= 0 else f"({c})*a_{{n-{i+1}}}"
     for i, c in enumerate(exact_coeffs)
  ]
  print(f" a_n = {' + '.join(rec_terms)}")
  init_str = ", ".join(
     [f"a_{i} = {val}" for i, val in enumerate(exact_inits)]
  )
  print(f" Initial conditions: {init_str}")

  r_sym = sp.Symbol("r")
  poly = r_sym**k_order
  for i, c in enumerate(exact_coeffs):
     poly -= c * (r_sym ** (k_order - 1 - i))

  print("\n2. CHARACTERISTIC EQUATION:")
  print(f" {poly} = 0")

  # Tìm nghiệm và bội nghiệm chính xác tuyệt đối
  roots_dict_raw = sp.roots(poly, r_sym)

  print("\n3. ROOT ANALYSIS:")
  processed_roots = []

  for root_expr, mult in roots_dict_raw.items():
     # Kiểm tra xem nghiệm là thực hay phức
     if root_expr.is_real:
        r_val = sp.simplify(root_expr)
        print(f" - Real root: r = {r_val} (Multiplicity {mult})")
        processed_roots.append({"type": "real", "r": r_val, "mult": mult})
     else:
        complex_val = complex(sp.N(root_expr))
        if complex_val.imag > 0:
           a_val = sp.re(root_expr)
           b_val = sp.im(root_expr)
           modulus = sp.simplify(sp.Abs(root_expr))
           arg_val = float(sp.N(sp.arg(root_expr)))
           phi1_str = simplify_angle(arg_val)

           print(
              f" - Complex conjugate pair: {a_val} +/- {b_val}i (Multiplicity {mult})"
           )
           print(f" + Modulus R = {modulus}")
           print(f" + Argument phi = {phi1_str} (rad)")

           processed_roots.append(
             {
                "type": "complex",
                "a": a_val,
                "b": b_val,
                "R": modulus,
                "arg_expr": sp.arg(root_expr),
                "arg_str": phi1_str,
                "mult": mult,
             }
           )

  n_sym = sp.Symbol("n")
  c_vars = [sp.Symbol(f"C_{i+1}") for i in range(k_order)]

  an_expr = sp.Integer(0)
  c_idx = 0

  # Lập công thức nghiệm tổng quát chính xác theo lý thuyết
  for root_info in processed_roots:
     if root_info["type"] == "real":
        r_val = root_info["r"]
        mult = root_info["mult"]
        poly_term = sp.Integer(0)
        for m_pow in range(mult):
           # Đúng dạng nghiệm bội: (C_1 + C_2*n + C_3*n^2 + ...) * r^n
           poly_term += c_vars[c_idx] * (n_sym**m_pow)
           c_idx += 1
        an_expr += poly_term * (r_val**n_sym)

     elif root_info["type"] == "complex":
        r_mod = root_info["R"]
        arg_expr = root_info["arg_expr"]
        mult = root_info["mult"]
        for m_pow in range(mult):
           cos_part = c_vars[c_idx] * sp.cos(n_sym * arg_expr)
           sin_part = c_vars[c_idx + 1] * sp.sin(n_sym * arg_expr)
           c_idx += 2
           an_expr += (r_mod**n_sym) * (n_sym**m_pow) * (cos_part + sin_part)

  # Lập hệ phương trình tìm các hằng số C
  eqs = []
  for idx_val, val in enumerate(exact_inits):
     eqs.append(sp.Eq(an_expr.subs(n_sym, idx_val), val))

  sol_dict = sp.solve(eqs, c_vars)
  final_an = sp.simplify(an_expr.subs(sol_dict))

  print("\n4. GENERAL SOLUTION (a_n):")
  print(f" a_n = {final_an}")
  print("=" * 65 + "\n")



if __name__ == "__main__":
 print("=== PROGRAM TO SOLVE HOMOGENEOUS RECURRENCE RELATION ===")
 print("Format: a_n = c1*a_{n-1} + c2*a_{n-2} + ... + ck*a_{n-k}")

 raw_coefficients = input(
   "\nEnter coefficients c1 c2 ... ck separated by spaces (e.g. 11 -7 -147): "
 )
 user_coefficients = [x for x in raw_coefficients.strip().split()]

 raw_initials = input(
   f"Enter {len(user_coefficients)} initial conditions a0 a1 ... "
   f"separated by spaces (e.g. 384 -64 -963): "
 )
 user_initials = [x for x in raw_initials.strip().split()]

 solve_recurrence(user_coefficients, user_initials)
