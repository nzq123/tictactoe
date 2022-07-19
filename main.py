tab = []
for j in range(3):
    tab.append([j * 3 + 1, j * 3 + 2, j * 3 + 3])

field = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

def p1_is_win():
    if field[0][0] == "X" and field[0][1] == "X" and field[0][2] == "X":
        return True
    elif field[0][0] == "X" and field[1][0] == "X" and field[2][0] == "X":
        return True
    elif field[0][0] == "X" and field[1][1] == "X" and field[2][2] == "X":
        return True
    elif field[1][0] == "X" and field[1][1] == "X" and field[1][2] == "X":
        return True
    elif field[2][0] == "X" and field[2][1] == "X" and field[2][2] == "X":
        return True
    elif field[2][0] == "X" and field[1][1] == "X" and field[0][2] == "X":
        return True
    elif field[0][1] == "X" and field[1][1] == "X" and field[2][1] == "X":
        return True
    elif field[0][2] == "X" and field[1][2] == "X" and field[2][2] == "X":
        return True


def p2_is_win():
    if field[0][0] == "O" and field[0][1] == "O" and field[0][2] == "O":
        return True
    elif field[0][0] == "O" and field[1][0] == "O" and field[2][0] == "O":
        return True
    elif field[0][0] == "O" and field[1][1] == "O" and field[2][2] == "O":
        return True
    elif field[1][0] == "O" and field[1][1] == "O" and field[1][2] == "O":
        return True
    elif field[2][0] == "O" and field[2][1] == "O" and field[2][2] == "O":
        return True
    elif field[2][0] == "O" and field[1][1] == "O" and field[0][2] == "O":
        return True
    elif field[0][1] == "O" and field[1][1] == "O" and field[2][1] == "O":
        return True
    elif field[0][2] == "O" and field[1][2] == "O" and field[2][2] == "O":
        return True


game = 1
while game <= 5:
    a = int(input("Gracz 1 podaję pierwsze pole: "))
    b = int(input("Gracz 1 podaję drugie pole: "))
    while field[a][b] == "X" or field[a][b] == "O":
        print("Nie możesz zagrać na polu przeciwnika")
        a = int(input("Gracz 1 podaję pierwsze pole: "))
        b = int(input("Gracz 1 podaję drugie pole: "))
    else:
        field[a][b] = "X"
    for i in field:
        print(i)
    if p1_is_win() is True:
        print("Gracz 1 wygrał")
        break

    if game == 5:
        break

    a = int(input("Gracz 2 podaję pierwsze pole: "))
    b = int(input("Gracz 2 podaję drugie pole: "))
    while field[a][b] == "X" or field[a][b] == "O":
        print("Nie możesz zagrać na polu przeciwnika")
        a = int(input("Gracz 2 podaję pierwsze pole: "))
        b = int(input("Gracz 2 podaję drugie pole: "))
    else:
        field[a][b] = "O"
    for i in field:
        print(i)
    if p2_is_win() is True:
        print("Gracz 2 wygrał")
        break

    game += 1

