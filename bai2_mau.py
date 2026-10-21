import random



def get_bitstring(u_seq, target_set):
  return "".join(["1" if elem in target_set else "0" for elem in u_seq])



def run_example_vd148c2(u_seq, a_set, b_set):
  xau_a = get_bitstring(u_seq, a_set)
  xau_b = get_bitstring(u_seq, b_set)

  bu_a = [elem for elem in u_seq if elem not in a_set]
  xau_bu_a = get_bitstring(u_seq, set(bu_a))
  len_bu_a = len(bu_a)

  bu_b = [elem for elem in u_seq if elem not in b_set]
  xau_bu_b = get_bitstring(u_seq, set(bu_b))
  len_bu_b = len(bu_b)
  a_h_b = [elem for elem in u_seq if elem in a_set or elem in b_set]
  xau_a_h_b = get_bitstring(u_seq, set(a_h_b))
  len_a_h_b = len(a_h_b)

  a_g_b = [elem for elem in u_seq if elem in a_set and elem in b_set]
  xau_a_g_b = get_bitstring(u_seq, set(a_g_b))
  len_a_g_b = len(a_g_b)

  a_t_b = [elem for elem in u_seq if elem in a_set and elem not in b_set]
  xau_a_t_b = get_bitstring(u_seq, set(a_t_b))
  len_a_t_b = len(a_t_b)

  b_t_a = [elem for elem in u_seq if elem in b_set and elem not in a_set]
  xau_b_t_a = get_bitstring(u_seq, set(b_t_a))
  len_b_t_a = len(b_t_a)

  sym_diff = [elem for elem in u_seq if elem in set(a_t_b) or elem in set(b_t_a)]
  xau_sym_diff = get_bitstring(u_seq, set(sym_diff))
  len_sym_diff = len(sym_diff)

  print("\n" + "=" * 65)
  print("       SET OPERATIONS AND BITSTRING REPRESENTATION                         ")
  print("=" * 65)
  print(f"1. U (16 elements permuted): {u_seq}")
  print(f"2. Set A:            {list(a_set)}")
  print(f"3. Bitstring A:        {xau_a}")
  print(f"4. Set B:            {list(b_set)}")
  print(f"5. Bitstring B:        {xau_b}")
  print("-" * 65)
  print(f"6. Bitstring BuA (U \\ A): {xau_bu_a}")
  print(f"7. Set BuA:            {bu_a}")
  print(f"8. Length BuA:           {len_bu_a}")
  print("-" * 65)
  print(f"9. Bitstring BuB (U \\ B): {xau_bu_b}")
  print(f"10. Set BuB:            {bu_b}")
  print(f"11. Length BuB:           {len_bu_b}")
  print("-" * 65)
  print(f"12. Bitstring A U B:      {xau_a_h_b}")
  print(f"13. Set A U B:          {a_h_b}")
  print(f"14. Length A U B:          {len_a_h_b}")
  print("-" * 65)
  print(f"15. Bitstring A n B:      {xau_a_g_b}")
  print(f"16. Set A n B:          {a_g_b}")
  print(f"17. Length A n B:          {len_a_g_b}")
  print("-" * 65)
  print(f"18. Bitstring A \\ B:     {xau_a_t_b}")
  print(f"19. Set A \\ B:        {a_t_b}")
  print(f"20. Length A \\ B:       {len_a_t_b}")
  print("-" * 65)
  print(f"21. Bitstring B \\ A:     {xau_b_t_a}")
  print(f"22. Set B \\ A:        {b_t_a}")
  print(f"23. Length B \\ A:       {len_b_t_a}")
  print("-" * 65)
  print(f"24. Bitstring A Delta B:    {xau_sym_diff}")
  print(f"25. Set A Delta B:       {sym_diff}")
  print(f"26. Length A Delta B:      {len_sym_diff}")
  print("=" * 65)



if __name__ == "__main__":
  u_base = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "l",
    "m",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
  ]

  u_permuted = u_base.copy()
  random.shuffle(u_permuted)

  print("=== SET REPRESENTATION PROGRAM ===")
  print(f"Base U: {u_base}")
  print(f"Permuted U: {u_permuted}\n")

  print("Enter elements separated by space (e.g. a c e m):")
  input_a = input("Enter Set A: ").strip().split()
  input_b = input("Enter Set B: ").strip().split()

  parsed_a_set = set(input_a)
  parsed_b_set = set(input_b)

  run_example_vd148c2(u_permuted, parsed_a_set, parsed_b_set)
