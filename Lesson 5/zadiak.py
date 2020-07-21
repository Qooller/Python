symb = [chr(i) for i in range(9800,9811)]
sym_j = "".join(symb)
for i in range(12):
    print(sym_j[i:]+sym_j[:i])