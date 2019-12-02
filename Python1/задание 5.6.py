# Написать ф-ию to_title: принимает строчку, ищет пробелы, первые буквы после них делает заглавными:
def to_title(st):
    st = st.strip(" ")
    dl = len(st)
    st = st[0].upper() + st[1:]
    for i in range(0, dl):
        if st[i] == ' ':
            st = st[:i+1] + st[i+1].upper() + st[i+2:]

    return st
w = to_title(' hello rofgj Dnfys fkj skfk ksjbsk ss ')
print(w)